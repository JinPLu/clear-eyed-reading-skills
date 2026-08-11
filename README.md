# 祛魅阅读 Skills

**简体中文** | [English](README_EN.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Harness](https://img.shields.io/badge/Harness-agnostic-2563EB)](#安装与兼容性)

**论文读完了，却还是说不清它到底做了什么？**

术语看懂了，方法没走通；表格看完了，不知道创新是不是真的；作者说“全面领先”，却不知道证据究竟撑到哪里。

祛魅阅读不复述论文。它用白话重建问题和方法，独立核验近邻工作与决定性证据，最后回答三件事：**真正新增了什么、证据只支持到哪里、这项工作值不值得继续读和用。**

![祛魅阅读地图：共享读法分为快速导读与完整精读](assets/clear-eyed-reading-map-v3.png)

## 读完以后，你会知道

- 🧠 **方法怎么工作**：输入是什么、每一步做什么、能力从哪里来。
- ✨ **真实贡献是什么**：与最接近的已有工作相比，究竟多做了什么。
- 📊 **证据能说明什么**：关键图表和实验支持哪项结论，又不能推出什么。
- ⚖️ **应该怎样看待它**：适用范围、主要边界，以及是否值得继续投入时间。

## 选择阅读深度

| | ⚡ `clear-eyed-reading` | 🔬 `clear-eyed-deep-reading` |
| --- | --- | --- |
| **适合** | 快速读懂，判断创新与价值 | 彻底掌握，准备复述或复用 |
| **输出** | 问题 → 方法 → 真实贡献 → 决定性证据 → 祛魅结论 | 背景、方法链、贯穿例子、公式、原图、实验与完整判断 |
| **读完能做什么** | 决定是否值得继续读 | 复述、画出、复用并质疑方法 |

两种读法使用同一套材料和证据标准。快速导读只省略不改变判断的细节；完整精读展开同一条理解与证据链。

## 判断依据

- 🔍 **读原文再判断**：核对全文、附录和决定性原图；材料缺失就缩小结论。
- 🌍 **独立判断创新**：检索领域、近邻工作和反证先例，不把 Related Work 或引用量当答案。
- 🎯 **围绕贡献读实验**：先解释最能改变结论的结果，再看消融、扩展和失败案例补充了什么。

祛魅不是找茬。只强调会改变核心结论、创新或贡献的问题，也保留主张收窄后仍然成立的价值。

## 直接使用

两个 Skill 都只在用户显式调用时运行。

```text
快速导读：使用 $clear-eyed-reading 读懂并评价这篇文章：<链接或附件>
完整精读：使用 $clear-eyed-deep-reading 讲清这篇文章的方法、公式、图表、实验和证据：<链接或附件>
```

## 安装与兼容性

将 [`skills/clear-eyed-reading`](skills/clear-eyed-reading) 或 [`skills/clear-eyed-deep-reading`](skills/clear-eyed-deep-reading) 放入 agent harness 的 Skills 搜索路径即可。两个目录都是自包含安装产物，普通用户不需要 Python。早期版本用户可移除旧的 `clear-eyed-paper-reading` 和 `clear-eyed-paper-deep-reading` 目录，避免入口名混淆。

核心指令不绑定特定模型、MCP、CLI、平台 API 或输出语言。🛡️ 文章内容只被视为研究材料；未经许可，Skill 不执行文中代码，也不上传未公开材料。

## 维护与贡献

[`skill-src/`](skill-src) 是唯一指令源码。使用 `python3 scripts/sync_skills.py` 生成 Skill，使用 `--check` 检查漂移。回归用例见 [`evals/cases.yaml`](evals/cases.yaml)，贡献规范见 [`CONTRIBUTING.md`](CONTRIBUTING.md)，安全问题见 [`SECURITY.md`](SECURITY.md)。项目采用 [MIT License](LICENSE)。
