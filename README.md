[English](README.en.md)

# 游戏制作项目经理

### 把制作意图，交成能开工的任务。

把制作意图变成逐项可交接的工作：谁做、从哪个版本开始、做哪些动作、提交什么文件、依赖谁，以及怎样验收。规则、数值、程序、美术、本地化、QA 与集成沿同一组 ID 关联。

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=depth-v4">
  <img src="assets/readme/hero-zh.webp?v=depth-v4" width="100%" alt="把需求、决定和反馈，整理成团队或 Agent 能接手的工作包。">
</picture>

[下载完整介绍 · 24 秒 MP4](assets/readme/hero-zh.mp4?raw=true) · [GIF](assets/readme/hero-zh.gif) · [文字版](assets/readme/transcript-zh.md)

## 装好，然后直接说

```sh
npx skills add https://github.com/NewenergyEric/game-production-manager
```

在支持 Agent Skills 的工具中安装，例如 Codex、Claude Code、Cursor；将资料放进 Agent 能读取的位置，再描述问题。

### 把一句要求拆细

> 玩家交付物品后改造社区角落。拆成程序、美术、数值、文案、QA 能接手的任务。

得到 12 个任务、12 个交付物、依赖关系、版本输入和逐项验收；物品链、奖励、尺寸和工期不凭空补全。

### 点开一个具体任务

> 把 T-07 展开，说明事务、存档和重复提交如何检查，什么时候不能开工。

输入 D-CONFIG 与 D-TECH；明确校验、扣除、发奖、存档动作；重复提交只生效一次。输入未确认时保持 planned。

### 处理反馈与变更

> 订单配置改了，哪些任务需要重新检查？场景美术要全部重做吗？

工具实际追踪到 T-02、T-07、T-08、T-10、T-11、T-12；当前依赖下 T-06 场景制作不受影响，外观改动需另补关系。

## 看一个具体案例

**原创制作计划：社区订单改造角落。** 已真实运行校验、工作包导出和变更影响工具。示例包含 12 个 Given/When/Then 验收用例、3 行资产家族 BOM，并保留正式输入待定。

[完整分析与可下载底稿](case-studies/community-order/README.md)

[![游戏制作项目经理](case-studies/community-order/dashboard-zh.png?v=depth-v4)](case-studies/community-order/dashboard-zh.png)

## 最后交给团队什么

- 范围与交付约定 — `SOW.md`
- 12 个任务与版本输入 — `tasks.csv`
- 验收用例与资产清单 — `acceptance.csv · asset-bom.csv`

<details>
<summary>能力边界、说明书与验证</summary>

这是执行计划案例，功能尚未制作，所有任务仍为 planned。任务数量和逻辑状态不等于导出文件数或工期。真实制品、复核证据与有权限的验收记录齐备后，才可标记 accepted。

核心工具使用 Python 3.10+ 标准库；动画源码是可选的 Remotion 工程。

[人类说明书](docs/HUMAN-GUIDE.md) · [Agent guide](docs/AGENT-GUIDE.md) · [SKILL.md](SKILL.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
