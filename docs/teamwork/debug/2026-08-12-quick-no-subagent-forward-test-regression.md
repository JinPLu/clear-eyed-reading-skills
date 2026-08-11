# Quick no-subagent 前向回归的因果诊断

> 状态：`cause-confirmed`。Debug 阶段已定稿；本记录确认运行时因果边界，未授权或实施修复。

## Failure and operating boundary

### 运行与预期边界

Fresh thread `019ff23f-9755-7520-a30c-534b8ad09ded` 运行已安装的 `$clear-eyed-reading`，模型为 `gpt-5.6-luna`、`xhigh`，输入为 Dyna-2 prompt，并明确禁止 subagent。安装版与生成版 hash 匹配，因此本次回归不是安装漂移。

该前向路径需要把 field research 的结果带入最终判断：候选来源应被实际打开和核对，三条 sequential tracks、全文阅读与收敛过程应完成；若没有 independent cross-check，也应明确披露；各项评分应有各自的 evidence base。

### 观察到的结果

Runtime 只做了关键词搜索，点名 `RDT2`、`LAP`、`EgoScale`，但没有打开候选 primary texts，也没有完成 three sequential tracks、full-text 或 convergence。它没有披露缺少 independent cross-check，也没有为评分提供 individual evidence bases，而是直接给出裸分 `8/7/8/8/3`。

no-subagent 约束本身有效；因此不能把缺少 subagent 归因为本次回归。

### 运行边界

本轮只记录和确认原因，不修改 Skill、eval 或安装产物。没有授权修复，也没有实施修复；因此没有同路径修复验证可报告。

## Causal picture

### 因果链

```text
安装版与生成版 hash 匹配
  → 排除安装/生成漂移
  → runtime 停留在关键词搜索与候选命名
  → 未进入候选 primary text、三条 sequential tracks、全文与 convergence
  → field research 的缺口未在 final judgment 处被拦截或披露
  → 未披露 independent cross-check 缺失，且以裸 8/7/8/8/3 代替逐项 evidence base
  → Quick no-subagent 前向测试回归
```

首个坏 owned boundary 是 **field-research → final-judgment**：运行时没有把研究完成度和证据状态带入最终判断。

### Cause standing

- **Primary cause — confirmed：** runtime 在 field-research → final-judgment 边界不合规；它以关键词命中和候选命名替代了实际 primary-text 核对、三条 sequential tracks、full-text 与 convergence，并继续输出无逐项依据的评分。
- **Secondary cause — confirmed：** eval 对这条运行时边界的覆盖不足，未阻止上述不合规结果进入最终判断。
- **Source-spec limitation — scoped ambiguity：** source specification 对 visible field-removal，以及 novelty 的 technical/lineage 维度与 significance 的 field-consequence 维度，存在有限歧义。这是受限的规范歧义，不取代已确认的 primary runtime noncompliance。
- **No-subagent constraint — valid:** 禁止 subagent 是有效测试约束，不是回归原因。

## Discriminating observations

1. 安装版与生成版 hash 匹配，排除了 drift 作为解释。
2. 实际行为只有关键词搜索和候选命名；`RDT2`、`LAP`、`EgoScale` 未被推进到候选 primary texts 的打开与核对，也未完成 three sequential tracks、full-text 或 convergence。
3. 输出没有披露 independent cross-check 缺失，并以裸 `8/7/8/8/3` 代替各项 individual evidence bases。
4. no-subagent 约束有效，不能用“没有 subagent”解释研究链和评分证据链的缺失。

这些观察将原因定位到 field-research → final-judgment 的 runtime 边界，而不是安装漂移、subagent 约束本身或单纯的候选命名问题。

## Cause, next discriminator, and verification

已确认的原因是：Quick runtime 在 field-research → final-judgment 处未执行或未传递所需的研究完成度与证据状态；secondary eval gap 使该失败没有被验收拦截。source-spec 的有限歧义只限定了 visible field-removal、novelty 与 significance 的判定边界，不能解释已观察到的全文、轨迹、交叉核验和逐项证据均缺失。

没有待完成的 cause discriminator。后续若获得明确授权，应沿原始 Quick no-subagent 路径修复并复跑；在此之前不把任何修复或验证写成已完成。
