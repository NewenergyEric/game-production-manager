# Depth cases / 深度案例审查 · 2026-10-11

Comparison baseline: origin/main before the depth-case branch. Three independent Darwin judges compared the previous and revised protocols using nine shared scenarios. This is paired dry-run review plus direct tool checks, not nine completed production jobs or a benchmark of different models.

基线为更新前 main。三位独立评审对九个相同场景进行前后对照，并实际调用校验、影响追踪和公式复算；不把协议审查包装成生产任务完成。

| Scope / 范围 | Findings / 结论 |
|---|---|
| Market / 市场 | Cross-genre, IP, region, language and payment comparisons improved; language support does not establish revenue. Judge 3 marked the existing missing-data safeguard as a tie; all judged the overall role better. / 跨维度比较更具体；缺失数据保护原本已有，第3位对此单项判平。 |
| Reverse / 拆解 | Code flow, merge boundary, spawn formulas and asset counting improved. All three independently recomputed the pinned case successfully. / 三位均核对18个输入哈希与公式，未执行目标。 |
| PM / 项目 | Twelve explicit handoffs and the six-task impact example improved clarity. Initial review found incomplete execution gates; repaired and rechecked. / 初审发现的执行放行缺口已修复并复核。 |

## Repairs / 修复

- Reject blank outputs, entry and stop conditions. / 拒绝空白产物、进入与停止条件。
- Require exact, unique declared-input/version matching and valid internal references. / 版本记录与输入一一对应，无重复、无悬空内部引用。
- Require accepted prerequisites before ready/in_progress/submitted execution states. / 未完成前置任务不能放行。
- Review design deliverables as documents or specifications; leave runtime verification to implementation and QA. / 设计任务验收文档，运行行为交给实现与 QA。
- Separate human-facing report sections from CLI JSON fields in both language guides. / 双语说明明确区分报告栏目和工具字段。
- A final duplicate-declared-input edge case found by judge 1 was corrected and added to the regression check. / 第1位追加的重复输入边界已补入回归检查。

## Actual checks / 实际验证

- Market: 8 tests; 18 comparison cells exported, missing-axis/dangling-evidence rejection. / 市场8项测试。
- Reverse: 9 tests; 18 pinned input hashes; calculated 2.2, 0.6513215599 and 106.25. / 拆解9项测试，公式实算。
- PM: 10 tests; legacy and detailed fixtures remain valid; D-CONFIG affects T-02/T-07/T-08/T-10/T-11/T-12 only in this example. / PM10项测试。
- Target game execution remains false. All detailed production tasks remain planned. / 未执行目标游戏；制作任务全部planned。

Windows sandbox restrictions on temporary paths required running the reverse test suite outside the sandbox; the full suite then passed. CI runs the same core tests independently. Presentation bytes, frame timing, faststart metadata and hashes are checked by scripts/check_presentation.py; that validation is separate from this content review.
