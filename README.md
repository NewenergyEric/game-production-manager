[English](README.en.md)

[**Game Dev Skills**](https://github.com/NewenergyEric/NewenergyEric/blob/main/GAME-DEV-SKILLS.md) · [市场研究](https://github.com/NewenergyEric/game-market-intelligence) · [游戏拆解](https://github.com/NewenergyEric/game-reverse-analyst) · [制作管理](https://github.com/NewenergyEric/game-production-manager) · [美术总监](https://github.com/NewenergyEric/art-director-skill)

# 游戏制作项目经理

### 把制作意图，交成能开工的任务。

把制作意图变成逐项可交接的工作：谁做、从哪个版本开始、做哪些动作、提交什么文件、依赖谁，以及怎样验收。规则、数值、程序、美术、本地化、QA 与集成沿同一组 ID 关联。

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=depth-v4">
  <img src="assets/readme/hero-zh.webp?v=depth-v4" width="100%" alt="把需求、决定和反馈，整理成团队或 Agent 能接手的工作包。">
</picture>

[下载完整介绍 · 24 秒 MP4](assets/readme/hero-zh.mp4?raw=true) · [GIF](assets/readme/hero-zh.gif) · [文字版](assets/readme/transcript-zh.md)

## 为什么做这个

**“我们知道要做什么”，和“大家可以开工”，之间还隔着一份具体约定。**

谁提供配置，程序从哪一版开始，美术要交哪些状态，改了规则会影响谁，最后怎样验收——这些问题若留在聊天里，接手的人就得再问一遍。

它是 Game Dev Skills 的制作管理岗位。把研究与拆解资料、策划要求和反馈，整理成有输入、有交付物、有验收依据的工作包。个人用它检查遗漏，团队或 Agent 用它接手执行；实际制作与验收继续由对应角色完成。

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

## 告诉我，你在哪一步卡住

用过一次后，欢迎留下：你想完成什么、给了哪些可公开资料、拿到了什么，以及还缺哪一步。

[分享使用反馈或案例](https://github.com/NewenergyEric/game-production-manager/issues/new?template=use-case.yml)

## 四个岗位，共同做出值得做的游戏

个人制作者可以轮流承担四个岗位；团队通过同一份资料交接：什么值得做、竞对做了什么、资源和体量如何评估，以及如何创作自己的核心美术。

[岗位如何交接证据、范围与美术资产](docs/WORKFLOW.md) · [四岗位总览](https://github.com/NewenergyEric/NewenergyEric/blob/main/GAME-DEV-SKILLS.md)

| 眼前的问题 | 从这个岗位开始 | 带到下一步的资料 |
|---|---|---|
| 什么值得做？ | [市场研究](https://github.com/NewenergyEric/game-market-intelligence) | 机会比较、来源与验证缺口 |
| 竞对做了什么？ | [游戏拆解](https://github.com/NewenergyEric/game-reverse-analyst) | 规则、实现依据与资产 BOM |
| 做得起，也做得完吗？ | [制作管理](https://github.com/NewenergyEric/game-production-manager) | SOW、工作包、依赖与验收 |
| 核心美术如何建立？ | [美术总监](https://github.com/NewenergyEric/art-director-skill) | 共享规范、代表样板与项目包 |

**个人创作者：** 从当前卡住的问题开始，按需要切换岗位。**团队：** 用实际报告、BOM、工作包和美术规范交接；每一步保留来源、版本与未定项。

这是协作方法，当前没有自动串行执行四个 Agent 的编排器。

![市场研究、竞品拆解、项目评估与核心美术创作；样板与成本反馈推动前序决定修订。](assets/readme/workflow-zh.png)
