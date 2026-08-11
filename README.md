# Paper Demystifier Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/OpenAI-Skills-111111)](https://developers.openai.com/plugins/build/skills)

把论文从术语高台上请下来：**看清领域位置，拆开方法机关，核对关键证据，分出真贡献与水分。**

![论文祛魅地图：快速导读与完整精读的信息层级](assets/paper-demystifier-map-v2.png)

> 当前版本：`v0.1`。两个 Skill 已通过结构校验，并持续用不同学科与文章类型回归。

## 🧭 选哪个？

| 你的需求 | 使用的 Skill | 你会得到什么 |
| --- | --- | --- |
| ⚡ “快速读懂、评价创新、看看有没有水分” | [`clear-eyed-paper-reading`](skills/clear-eyed-paper-reading/SKILL.md) | 紧凑导读、关键证据、五维简评与一句总评 |
| 🔬 “精读、逐图逐表、讲懂公式和实验” | [`clear-eyed-paper-deep-reading`](skills/clear-eyed-paper-deep-reading/SKILL.md) | 领域地图、方法心智模型、完整证据链与最终判断 |

一句话选择：**只想知道值不值得读，用快速导读；想读完后能讲给别人听，用完整精读。**

两个 Skill 刻意分开，避免简单请求被冗长流程拖慢，也避免真正的精读退化成摘要。

## ✨ 它们怎么祛魅？

两条路线共用一把尺子：

1. 🌍 **放回领域**：独立寻找直接前例，不照抄作者的 Related Work。
2. ⚙️ **拆开方法**：还原成普通部件，查清新能力有没有外包给提示、标签或外部模型。
3. 📊 **核对证据**：区分“系统赢了”“模块有效”“作者解释成立”。
4. ⚖️ **收束判断**：直接说明哪句大话应收回，以及收回后还剩什么价值。

“毒舌”只针对主张、证据和推理。每个判断都应落回原文、图表、公式或领域前例。

## 🚀 安装

每个 Skill 都是独立目录，核心文件为 `SKILL.md`。

### ChatGPT

在支持个人 Skills 的 ChatGPT 中，分别上传两个 `SKILL.md`；具体入口以当前界面为准。

- [文章祛魅导读](skills/clear-eyed-paper-reading/SKILL.md)
- [文章祛魅精读](skills/clear-eyed-paper-deep-reading/SKILL.md)

### Codex

把需要的 Skill 目录复制到个人 skills 目录：

```bash
cp -R skills/clear-eyed-paper-reading ~/.codex/skills/
cp -R skills/clear-eyed-paper-deep-reading ~/.codex/skills/
```

## 💬 使用示例

快速导读：

```text
使用 $clear-eyed-paper-reading 读懂并评价这篇论文：<链接或附件>
```

完整精读：

```text
使用 $clear-eyed-paper-deep-reading 祛魅精读这篇论文，讲清背景、方法、公式、全部图表和实验：<链接或附件>
```

## 🗂️ 项目结构

```text
paper-demystifier-skills/
├── assets/
│   ├── paper-demystifier-map.png
│   └── paper-demystifier-map-v2.png
├── skills/
│   ├── clear-eyed-paper-reading/
│   │   ├── SKILL.md
│   │   └── agents/openai.yaml
│   └── clear-eyed-paper-deep-reading/
│       ├── SKILL.md
│       └── agents/openai.yaml
├── evals/cases.yaml
├── CONTRIBUTING.md
└── LICENSE
```

## ✅ 开发与验证

修改后重点检查：

- 两个 description 仍互斥，不争抢同一句请求；
- ⚡快速导读保持紧凑，不自动展开逐节精读；
- 🔬完整精读覆盖全部图表、关键公式与附录；
- 创新性与意义来自独立领域定位，而非作者自评；
- 结论清楚、具体、可追溯，不用空泛“局限”凑批判感。

基础回归用例见 [`evals/cases.yaml`](evals/cases.yaml)。贡献前请阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，安全问题见 [`SECURITY.md`](SECURITY.md)。

本项目使用 [MIT License](LICENSE)。

## 🔗 参考

- [OpenAI：Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI：Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins)
