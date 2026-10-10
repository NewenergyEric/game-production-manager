# 游戏制作项目经理

**Game Production Manager · game-production-manager**

确保策划与制作人的目标、计划、策略和反馈被团队理解，拆成 SOW、资产、任务和可验收目标。

这是面向 Agent 的岗位 Skill 与轻量工具包，版本 **0.1.0**。入口是 [SKILL.md](SKILL.md)；协作开发先读 [AGENTS.md](AGENTS.md)。本仓库公开方法、代码与原创测试例，实际游戏材料放在使用者自己的工作区。

## 立即使用

将本仓库交给能读取 GitHub/本地文件的 Agent，要求它阅读 SKILL.md 并结合你的材料执行该岗位。也可克隆到本地，或将完整仓库放入宿主支持的 Skill 目录；保留 scripts、references 和 data 等配套文件。

```text
git clone https://github.com/NewenergyEric/game-production-manager.git
cd game-production-manager
```

Python 3.10+，核心 Python 工具只使用标准库。REA 项目另需满足 package.json 的 Node 版本和 npm 依赖。

```text
python scripts/production.py validate examples/merge-package.json
python scripts/production.py render examples/merge-package.json --out outputs/demo-sow
python scripts/production.py impact examples/merge-package.json --changed D-ORDER
```

输出到新目录，示例可直接运行。示例中的游戏规则、数值和任务只用于格式/行为验证，不代表某个实际游戏的批准要求。

## 交接关系

| 岗位 | 仓库 | 交付 |
|---|---|---|
| 游戏市场研究总监 | [game-market-intelligence](https://github.com/NewenergyEric/game-market-intelligence) | 证据、经营判断与验证建议 |
| 游戏拆解与逆向分析师 | [game-reverse-analyst](https://github.com/NewenergyEric/game-reverse-analyst) | 玩法/架构/资产拆解与局限 |
| 游戏制作项目经理 | [game-production-manager](https://github.com/NewenergyEric/game-production-manager) | SOW、工作包、任务与变更 |
| 美术总监 | [art-director-skill](https://github.com/NewenergyEric/art-director-skill) | 专业规范、家族与样板、团队规则包 |


市场给依据，拆解给结构，制作项目经理把我方意图转成执行合同，Art Director 保证专业美术体系能被团队采用。程序、美术、音频、QA 或未来 Agent 执行者接任务并返回真实交付物；项目经理负责理解、协调和验收追踪。

## 验证与参与

```text
python -m unittest discover -s tests -v
```

[验证摘要](evals/verification.md) 区分已运行路径和未验证范围；[下一步](ROADMAP.md) 提供可以接手的工作。用分支与 PR 提交，附问题、行为变化和验证证据。新数据适配器应附真实访问范围与样例，不把平台候选变成已实现能力。

本仓库使用 MIT；REA 等依赖保留其各自许可证。私人导出、原始应用包、账号配置和分析结果不随仓库发布。
