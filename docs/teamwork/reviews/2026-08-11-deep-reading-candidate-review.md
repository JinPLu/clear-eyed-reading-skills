# clear-eyed-deep-reading 当前候选的 Ordinary Review

## Candidate, scope, and criteria

本次 Review 覆盖以下稳定候选及其安装同步版本：

- `skills/clear-eyed-deep-reading/SKILL.md`；
- `skills/clear-eyed-deep-reading/agents/openai.yaml`；
- `evals/cases.yaml`；
- `README.md` 与 `README_EN.md`；
- 上述候选的当前 diff，以及对应的安装同步版本。

Review 只检查当前候选的语义一致性、回归契约和同步结果，不修改候选文件，也不重新设计已选方向。接受标准是：精读主线、实现细节、公式命名、实验覆盖和祛魅边界之间保持一致；对应 eval 能观察到约定行为；安装同步版本不保留已修复的冲突。

## Direct evidence and findings

Ordinary Review 只有一个 finding：**公式作者命名规则、局部标签表达与 eval 约定曾不一致**。具体边界位于 `SKILL.md` 的公式功能命名/式号局部标签规则与 `evals/cases.yaml` 的 `deep-equation-semantic-names` 期望之间；候选还包含安装同步版本，因此该规则不能只在项目源文件中成立。

修复已将公式的作者已有功能名称、必要时按计算作用生成的名称，以及“功能名称 + 式号仅作定位”的局部标签约定对齐到同一行为契约，并同步更新对应 eval 口径与安装版本。Bounded recheck 重新读取了候选中的公式规则、对应 eval 条目和安装同步副本，确认该唯一 finding 已闭合；本次 Review 未发现其他需要改变 verdict 的问题。

## Verdict

**ACCEPT**。唯一 finding 已修复，并通过上述 bounded recheck；候选范围内的 skill、接口提示、README、eval 和安装同步版本现在共享同一公式命名/局部标签契约，未引入需要阻止接受的其他语义问题。

## Residual risk and next action

目标 harness 尚未实际运行本次回归用例，因此运行时行为和目标宿主中的最终呈现仍未被直接验证。这是剩余验证不确定性，不改变当前静态 Review 的 ACCEPT verdict。下一步仅需在目标 harness 可用时运行相关 deep-reading 回归，重点确认公式标题不再退化为“公式几”以及 eval 能捕获功能命名和式号定位的组合要求。
