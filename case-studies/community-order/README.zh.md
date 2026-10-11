# 一条订单，拆到能够逐项接手

[English](README.en.md)

**制作人的问题：** “玩家交付物品后改造角落，策划、程序、美术、QA 各自拿到什么？如果从交一件改成两件，哪里要一起改？”

本例实际运行了计划校验、SOW/任务/资产/验收导出和变更追踪。它是原创规划案例，不是已开发功能：12 项任务全部 planned，正式数值、美术包、引擎和工期均未伪造。

| ID | 岗位 | 要做的具体工作 | 依赖 |
|---|---|---|---|
| T-01 | 主策 | 说明 unmet/ready/submitting/completed/failed 的合法转换、重复提交与重进预期。 | — |
| T-02 | 数值策划 | 定义 item_id、required_count、reward_ref、corner_ref；数值保留待确认，不硬编码到表现层。 | T-01 |
| T-03 | 技术负责人 | 确定库存扣除、完成标记、奖励和存档的事务边界；记录重复请求键与失败恢复策略。 | T-01 |
| T-04 | 主美 | 拆清基础组件、状态复用、角落前后资产与规格缺口，引用有效美术包。 | T-01 |
| T-05 | UI设计师 | 为订单面板、按钮、数量和反馈定义五态组合，给出交互与禁用规则。 | T-01, T-04 |
| T-06 | 场景美术 | 交付一个角落的前后状态及锚点/遮挡/组合检查；复用与新制单列。 | T-04 |
| T-07 | 玩法程序 | 按契约实现验证、扣除、完成与奖励；提供非法输入与重复提交的测试证据。 | T-02, T-03 |
| T-08 | 客户端程序 | 绑定库存、订单状态、文本键和表现；处理提交中、失败与重进。 | T-05, T-07, T-09 |
| T-09 | 本地化负责人 | 用文本键替代硬编码；数量和长文本按各语言检查，确认字体覆盖。 | T-01, T-05 |
| T-10 | QA工程师 | 执行不足/刚好/超额库存、重复提交、失败、恢复与无效配置场景。 | T-07, T-08 |
| T-11 | 集成程序 | 将角落表现与订单完成状态集成，检查顺序、中断、恢复和资源引用。 | T-06, T-08, T-10 |
| T-12 | 游戏制作项目经理 | 核对输入版本、制品、验收与未决项，组织接包并记录负责人决定。 | T-09, T-10, T-11 |

## 一次真实运行的变更追踪

将 `D-CONFIG`（物品与奖励配置）列为变更输入，工具追到 `T-02 → T-07 → T-08 → T-10 → T-11 → T-12`。场景制作 `T-06` 不因这条配置变更自动重做；若出现新的视觉要求，应另列变更。任务与旧基线均未被修改。

## 具体验收与资产颗粒度

重复提交只能结算一次；库存不足不扣除；重进显示已保存状态；中断恢复后外观与订单一致；长文本和字体需逐语言检查。五种 UI 状态属于一个组件家族，不假报为五张纹理。

[完整执行包 / Full package](../../examples/community-order-detailed.json) · [任务 / Tasks](tasks.csv) · [验收 / Acceptance](acceptance.csv) · [资产 BOM](asset-bom.csv) · [变更影响 / Impact](impact.json)

```sh
python scripts/production.py validate examples/community-order-detailed.json
python scripts/production.py render examples/community-order-detailed.json --out outputs/community-order
python scripts/production.py impact examples/community-order-detailed.json --changed D-CONFIG
```
