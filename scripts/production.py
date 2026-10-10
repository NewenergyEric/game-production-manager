#!/usr/bin/env python3
"""Validate, render and trace changes in a production plan; never executes tasks."""
import argparse
import csv
import json
from pathlib import Path

STATES = {'planned', 'ready', 'in_progress', 'submitted', 'accepted', 'blocked', 'cancelled'}


def validate(data):
    if not isinstance(data, dict): return ['package must be an object']
    errors = []
    for key in ['id', 'version', 'goal', 'strategy', 'scope_in', 'scope_out', 'constraints', 'assumptions']:
        if key not in data: errors.append('missing ' + key)
    groups = {}
    all_ids = set()
    for name in ['requirements', 'deliverables', 'tasks', 'milestones']:
        rows = data.get(name)
        if not isinstance(rows, list) or not rows:
            errors.append(name + ' must be a nonempty list'); rows = []
        groups[name] = {}
        for row in rows:
            if not isinstance(row, dict): errors.append(name + ' entries must be objects'); continue
            rid = row.get('id')
            if not isinstance(rid, str) or not rid or rid in all_ids:
                errors.append('missing or duplicate ID in ' + name); continue
            all_ids.add(rid); groups[name][rid] = row
    reqs, deliverables, tasks, milestones = [groups[n] for n in ['requirements','deliverables','tasks','milestones']]

    def refs(row, key, targets, required=True):
        values = row.get(key, [])
        if not isinstance(values, list) or any(not isinstance(x, str) for x in values):
            errors.append(f"{row['id']}: {key} must be a list of IDs"); return []
        if required and not values: errors.append(f"{row['id']}: empty {key}")
        for value in values:
            if value not in targets: errors.append(f"{row['id']}: dangling {key} {value}")
        return values

    for r in reqs.values():
        for key in ['text', 'source', 'acceptance', 'owner_role']:
            if not r.get(key): errors.append(f"{r['id']}: missing {key}")
        if r.get('status') not in ['confirmed','proposed']: errors.append(f"{r['id']}: invalid requirement status")
    covered_req = set(); covered_deliverables = set()
    for d in deliverables.values():
        covered_req.update(refs(d, 'requirement_ids', reqs))
        for key in ['name', 'type', 'spec', 'acceptance', 'reviewer_role']:
            if not d.get(key): errors.append(f"{d['id']}: missing {key}")
    graph = {}
    for t in tasks.values():
        covered_deliverables.update(refs(t, 'deliverable_ids', deliverables))
        graph[t['id']] = refs(t, 'depends_on', tasks, False)
        for key in ['owner_role','inputs','action','acceptance']:
            if not t.get(key): errors.append(f"{t['id']}: missing {key}")
        if t.get('executor_kind') not in ['human','agent','either']: errors.append(f"{t['id']}: invalid executor_kind")
        state = t.get('status')
        if state not in STATES: errors.append(f"{t['id']}: invalid task status")
        if state == 'blocked' and not t.get('blocker'): errors.append(f"{t['id']}: blocked task needs blocker")
        if state in ['submitted','accepted'] and not t.get('artifacts'): errors.append(f"{t['id']}: submission needs artifact references")
        if state == 'accepted':
            review = t.get('review')
            if not isinstance(review, dict) or review.get('result') != 'pass' or not all(review.get(k) for k in ['reviewer','authority_reference','evidence']):
                errors.append(f"{t['id']}: accepted requires a recorded pass review with authority and evidence")
            for dep in graph[t['id']]:
                if dep in tasks and tasks[dep].get('status') != 'accepted': errors.append(f"{t['id']}: dependency {dep} not accepted")
    for rid, r in reqs.items():
        if r.get('status') == 'confirmed' and rid not in covered_req: errors.append(rid + ': confirmed requirement has no deliverable')
    for did in deliverables:
        if did not in covered_deliverables: errors.append(did + ': deliverable has no task')
    for m in milestones.values():
        refs(m, 'task_ids', tasks)
        if not m.get('exit_criteria'): errors.append(m['id'] + ': missing exit criteria')
    visited, active = set(), set()
    def walk(tid):
        if tid in active: errors.append('dependency cycle at ' + tid); return
        if tid in visited: return
        active.add(tid)
        for dep in graph.get(tid, []): walk(dep)
        active.remove(tid); visited.add(tid)
    for tid in graph: walk(tid)
    for f in data.get('feedback', []):
        if not isinstance(f, dict): errors.append('feedback must be an object'); continue
        for ref in f.get('target_ids', []):
            if ref not in all_ids: errors.append(f"feedback {f.get('id')}: unknown target {ref}")
    return errors


def impact(data, changed):
    errors = validate(data)
    if errors: raise ValueError('; '.join(errors))
    known = {x['id'] for g in ['requirements','deliverables','tasks','milestones'] for x in data[g]}
    if not set(changed) <= known: raise ValueError('unknown changed ID')
    affected = set(changed)
    for m in data['milestones']:
        if m['id'] in affected: affected.update(m['task_ids'])
    while True:
        before = set(affected)
        for d in data['deliverables']:
            if set(d['requirement_ids']) & affected: affected.add(d['id'])
        for t in data['tasks']:
            if (set(t['deliverable_ids']) | set(t['depends_on'])) & affected: affected.add(t['id'])
        if affected == before: break
    return {'changed_ids': list(changed), 'affected_task_ids': [t['id'] for t in data['tasks'] if t['id'] in affected],
            'action': 'Review scope, inputs, estimates and acceptance; no tasks or approved decisions were modified.'}


def render(data, out):
    errors = validate(data)
    if errors: raise ValueError('; '.join(errors))
    out.mkdir(parents=True, exist_ok=False)
    lines = [f"# SOW · {data['id']} · {data['version']}", '', '**目标：** ' + data['goal'], '', '**策略：** ' + data['strategy'], '']
    for key, label in [('scope_in','范围内'),('scope_out','范围外'),('constraints','约束'),('assumptions','假设与待定')]:
        lines += ['## ' + label, ''] + ['- ' + str(v) for v in data[key]] + ['']
    lines += ['## 交付物与验收', '']
    for d in data['deliverables']:
        lines += [f"### {d['id']} · {d['name']}", '', '规格：' + json.dumps(d['spec'],ensure_ascii=False), '',
                  '验收：' + json.dumps(d['acceptance'],ensure_ascii=False), '', '接收岗位：' + d['reviewer_role'], '']
    lines += ['## 里程碑', '']
    for m in data['milestones']: lines += [f"- {m['id']}：{m.get('goal','')}；退出条件：{m['exit_criteria']}"]
    lines += ['', '本文件是执行计划。制作、代码和 Build 由任务执行者提交；文档生成不改变任务完成状态。', '']
    (out/'SOW.md').write_text('\n'.join(lines),encoding='utf-8')
    fields = ['id','owner_role','executor_kind','deliverable_ids','depends_on','action','acceptance','status']
    with (out/'tasks.csv').open('w',encoding='utf-8-sig',newline='') as file:
        writer = csv.DictWriter(file,fieldnames=fields); writer.writeheader()
        for t in data['tasks']:
            writer.writerow({k: json.dumps(t[k],ensure_ascii=False) if isinstance(t[k], (dict,list)) else t[k] for k in fields})
    roles = {}
    for t in data['tasks']: roles.setdefault(t['owner_role'], []).append(t)
    (out/'role-views.json').write_text(json.dumps(roles,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (out/'package.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command',required=True)
    for cmd in ['validate','render','impact']:
        p = subs.add_parser(cmd); p.add_argument('input',type=Path)
        if cmd == 'render': p.add_argument('--out',type=Path,required=True)
        if cmd == 'impact': p.add_argument('--changed',nargs='+',required=True)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding='utf-8-sig')); errors = validate(data)
        if errors:
            print(json.dumps({'valid':False,'errors':errors},ensure_ascii=False)); return 1
        if args.command == 'render': render(data,args.out)
        result = impact(data,args.changed) if args.command == 'impact' else {'valid':True,'scope':'Plan structure only; tasks were not executed.'}
        print(json.dumps(result,ensure_ascii=False,indent=2)); return 0
    except (OSError,ValueError,TypeError,KeyError,AttributeError) as exc:
        print(json.dumps({'error':str(exc)},ensure_ascii=False)); return 1


if __name__ == '__main__': raise SystemExit(main())
