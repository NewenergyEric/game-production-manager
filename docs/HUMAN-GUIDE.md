# 游戏制作项目经理 · 使用说明

[English](HUMAN-GUIDE.en.md)

把需求、决定和反馈，整理成团队或 Agent 能接手的工作包。

## 准备资料

把原要求、已有决定和限制一起交给 Agent。
资料不齐也可以开始；影响下一步的缺项会单列，不以猜测填充。

## 需求已经有了，帮团队开始工作

> 使用 `$game-production-manager`。这些是已有策划、主美要求和制作限制。先整理共同理解与待决事项，再把这条社区订单拆成工作范围、交付物、岗位任务和验收条件。保留已经确认的决定。

SOW、交付物和资产拆分、岗位任务、依赖，以及需要负责人决定的问题。

## 把任务交给成员或另一个 Agent

> 把这个工作包按岗位整理。每项任务说明输入版本、要做的动作、输出、依赖、什么算完成，以及遇到什么情况要停下询问。

能够接手的任务约定。人或 Agent 使用同一套输入和验收标准，专业执行者负责实际制作并提交制品。

## 主策改了一条规则，哪些工作要跟着改

> 订单规则调整了。沿着原交付物与任务检查影响，列出需要主美、程序和 QA 复核的内容。先给变更清单，确认后形成新版本。

关联任务、输入和验收条件的变更影响。旧任务保留原版本，避免做到一半要求悄悄变化。

## 如何复核

这个岗位组织和追踪工作。实际代码、美术、音频、测试与构建由对应的人或 Agent 执行，并返回制品和证据。

计划生成不会把任务标为完成。进入 accepted 需要实际制品、复核证据和有权限的验收记录；外部工单、人员指派和消息发送按明确授权进行。

## 输出与交接

- **范围与交付：** SOW、需求追踪、资产基础件／变体／状态与验收。
- **岗位工作：** 责任、输入、动作、产物、依赖与停止条件。
- **版本与反馈：** 影响分析、实际提交、复核决定和交接记录。

[市场研究](https://github.com/NewenergyEric/game-market-intelligence)提供证据与建议；[拆解分析师](https://github.com/NewenergyEric/game-reverse-analyst)提供结构与未知；[Art Director](https://github.com/NewenergyEric/art-director-skill)负责专业美术规则；项目经理把确认后的工作交给合适的执行岗位。

## 给 Agent 的技术入口

Python 3.10+，核心工具仅用标准库。7 项确定性测试覆盖任务与交付覆盖、依赖环、变更传播、输出保护和验收证据。

```sh
python scripts/production.py validate examples/merge-package.json
python scripts/production.py render examples/merge-package.json --out outputs/merge-sow
python scripts/production.py impact examples/merge-package.json --changed D-ORDER
```
