# 人类使用说明 · 游戏制作项目经理

## 这份岗位解决什么问题

把主策、制作人、主美或技术负责人的目标、计划、策略和反馈，拆成团队真正看得懂的 SOW、资产清单、工作包、岗位任务、里程碑和验收目标。它是协调与执行契约岗位，不是自动生成游戏、代码或美术资产。

## 30 秒开始

1. 给 Agent 原始需求、已确认决定、限制、已有研究/拆解和反馈。
2. 要求它先读 `SKILL.md`，再运行：

   ```text
   python scripts/production.py validate examples/merge-package.json
   python scripts/production.py render examples/merge-package.json --out outputs/merge-sow
   python scripts/production.py impact examples/merge-package.json --changed D-ORDER
   ```

3. 先审目标、范围和验收，再把工作包交给对应执行者。
4. 收到提交后补证据和评审决定；范围变化进入新版本，不偷偷改旧任务。

## 你需要提供

产品目标、玩家体验、已确认规则、资源和时间限制、需要交付什么、谁接收、什么算完成，以及已知反馈。未知项可以保留，但必须成为负责人或执行者可处理的待决事项。

## 你会收到

SOW、需求到交付物到任务的追踪、资产/状态/规格拆分、岗位视图、依赖和里程碑、验收条件、反馈影响分析与回执模板。

## 关键边界

- 计划完成不等于制作完成；没有实际产物、测试证据和验收 authority，不得标记 accepted。
- 设计意见和美术判断归主策/主美；项目经理记录、澄清和追踪，不暗中替他们批准。
- Agent 执行需要单独的工具、权限、预算、停止条件和回执；本仓库默认只产出契约。
- 示例是 Merge／社区方向的格式案例，不是已经批准的游戏范围。
