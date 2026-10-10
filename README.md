[English](README.en.md)

# 游戏制作项目经理

### 把制作意图，交成能开工的任务。

**方向有人定，工作有人接，完成有依据。**

把制作人、主策、主美和技术负责人的要求、计划与反馈交给 Agent。它整理共同理解，拆清交付物、资产状态、责任岗位、依赖和验收，把既有工作接起来，交给团队或 Agent 执行。

<a href="assets/readme/hero-zh.mp4"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=workflow-v3">
  <img src="assets/readme/hero-zh.gif?v=workflow-v3" width="100%" alt="把需求、决定和反馈，整理成团队或 Agent 能接手的工作包。">
</picture></a>

[24 秒，走完一次完整工作 · 播放 MP4](assets/readme/hero-zh.mp4) · [文字版](assets/readme/transcript-zh.md)

## 装好，然后直接说

在支持 Agent Skills 的工具中安装，例如 Codex、Claude Code 或 Cursor：

```sh
npx skills add https://github.com/NewenergyEric/game-production-manager
```

把资料放进 Agent 能读取的文件夹，再说出要解决的问题。文件整理和命令由 Agent 处理。

### 需求已经有了，帮团队开始工作

> 使用 `$game-production-manager`。这些是已有策划、主美要求和制作限制。先整理共同理解与待决事项，再把这条社区订单拆成工作范围、交付物、岗位任务和验收条件。保留已经确认的决定。

**你会得到：** SOW、交付物和资产拆分、岗位任务、依赖，以及需要负责人决定的问题。

### 把任务交给成员或另一个 Agent

> 把这个工作包按岗位整理。每项任务说明输入版本、要做的动作、输出、依赖、什么算完成，以及遇到什么情况要停下询问。

**你会得到：** 能够接手的任务约定。人或 Agent 使用同一套输入和验收标准，专业执行者负责实际制作并提交制品。

### 主策改了一条规则，哪些工作要跟着改

> 订单规则调整了。沿着原交付物与任务检查影响，列出需要主美、程序和 QA 复核的内容。先给变更清单，确认后形成新版本。

**你会得到：** 关联任务、输入和验收条件的变更影响。旧任务保留原版本，避免做到一半要求悄悄变化。

## 最后交给团队什么

- **范围与交付：** SOW、需求追踪、资产基础件／变体／状态与验收。
- **岗位工作：** 责任、输入、动作、产物、依赖与停止条件。
- **版本与反馈：** 影响分析、实际提交、复核决定和交接记录。

## 看一条社区订单如何交接

[Merge／社区格式样例](examples/merge-package.json)以“交付物品后改造一个角落”为原始意图：主策定义订单规则，主美拆场景与 UI 要求，项目经理组织接包。

它包含 3 个交付物和 3 项计划任务；改变 `D-ORDER` 可追踪到 `T-RULE`、`T-ART` 和 `T-PACK`。这是原创草案，正式物品链、奖励、美术包和规格仍待真实项目确认。

[![看一条社区订单如何交接](assets/readme/workflow-zh.png?v=workflow-v3)](assets/readme/workflow-zh.png)

## 和其他岗位一起用

[市场研究](https://github.com/NewenergyEric/game-market-intelligence)提供证据与建议；[拆解分析师](https://github.com/NewenergyEric/game-reverse-analyst)提供结构与未知；[Art Director](https://github.com/NewenergyEric/art-director-skill)负责专业美术规则；项目经理把确认后的工作交给合适的执行岗位。

<details>
<summary><strong>安装要求、技术文档与验证</strong></summary>

Python 3.10+，核心工具仅用标准库。7 项确定性测试覆盖任务与交付覆盖、依赖环、变更传播、输出保护和验收证据。

[人类详细说明](docs/HUMAN-GUIDE.md) · [Agent 调用说明](docs/AGENT-GUIDE.md) · [Skill 入口](SKILL.md) · [验证与审查](evals/)

```sh
python scripts/production.py validate examples/merge-package.json
python scripts/production.py render examples/merge-package.json --out outputs/merge-sow
python scripts/production.py impact examples/merge-package.json --changed D-ORDER
```

[CI](https://github.com/NewenergyEric/game-production-manager/actions) · [Motion source](motion/README.md)

</details>

<details>
<summary><strong>能力边界与资料使用</strong></summary>

这个岗位组织和追踪工作。实际代码、美术、音频、测试与构建由对应的人或 Agent 执行，并返回制品和证据。

计划生成不会把任务标为完成。进入 accepted 需要实际制品、复核证据和有权限的验收记录；外部工单、人员指派和消息发送按明确授权进行。

</details>

[MIT License](LICENSE) · 由 Eric 与 Agents 一起制作。
