# Awesome Generative Visual Compression & Restoration

面向**生成式图像编码（GIC）**、**生成式视频编码（GVC）**与**生成式图像修复（GIR）**的中文论文索引。项目不仅记录论文、代码和发表信息，还逐篇整理训练数据、裁剪尺寸、优化器、学习率、batch size、训练步数、训练硬件，以及可直接用于研究复现的中文方法摘要。

> 时间范围：2016-08-24 至 2026-08-24（滚动十年窗口）。最后检索：2026-08-24。

## 收录原则

- 压缩类工作的核心任务必须是图像或视频的有损压缩/编码；修复类工作的核心任务必须是从退化观测恢复高质量图像。
- 方法必须显式利用 GAN、扩散/score/flow、生成式 tokenizer、自回归模型、预训练生成先验或隐式神经表示；仅把生成模型当作数据增强工具的工作不收录。
- 正式会议/期刊论文进入主表；高度相关但尚未正式发表的论文进入 Preprint 表。
- 训练信息仅来自论文正文、补充材料或官方代码。未披露字段统一写作 `NR（未报告）`，不做推断。

## 状态说明

| 标记 | 含义 |
|---|---|
| ✅ | 元数据、方法摘要与训练配置均已核验 |
| ◐ | 核心信息已核验，仍有论文未披露或待从补充材料确认的字段 |
| 🧪 | 高相关预印本，尚无正式会议/期刊版本 |

## 快速导航

- [生成式图像编码论文](papers/image-compression.md)
- [生成式视频编码论文](papers/video-compression.md)
- [生成式图像修复论文](papers/image-restoration.md)
- [压缩论文结构化数据](data/papers.json)
- [修复论文结构化数据](data/restoration-papers.json)

## 代表性路线

| 路线 | 典型工作 | 核心取舍 |
|---|---|---|
| GAN/对抗生成 | MS-ILLM、CGVC-T | 单步解码快，但训练稳定性与纹理幻觉需重点评估 |
| 条件扩散解码 | CDC、PerCo、PICD | 极低码率感知质量强，代价是多步采样和较高算力 |
| 基础生成模型先验 | FD-LIC、StableCodec、CoD | 借助大模型先验减少从零训练成本，但需解决条件对齐与可控忠实度 |
| 生成 latent/token 编码 | GLC、DLF、GVC1D | 在更语义化的空间中去冗余，适合超低码率；token 预测误差可能引入内容漂移 |
| 隐式神经表示 | GIViC | 模型/参数即码流，随机访问与编码时延通常是主要瓶颈 |
| 生成式图像修复 | DiffBIR、OSEDiff、ResFlow | 生成细节强，但必须约束语义幻觉、结构忠实度和采样成本 |

## 数据字段

每篇论文至少包含：`title`、`year`、`venue`、`publication_status`、`task`、`family`、`paper_url`、`code_url`、`core_idea_zh`、`training`、`evaluation`、`audit`。`training` 内固定包含数据集、输入尺寸、优化器、学习率、batch size、训练步数/epoch、硬件、预训练模型和补充说明。

## 当前覆盖

当前压缩索引共收录 54 篇工作，另收录 25 篇生成式图像修复工作，覆盖 2016–2026。近期编码主线包括 DiffVC-ONE、GenVC/ASD、FlowCodec、CoD-Lite、CADC、DiT-IC、ZeroGVC 与 ReGenVC；修复部分重点覆盖扩散逆问题、生成式超分、统一盲修复与 flow-matching 路线。

## Citation

若本索引帮助了你的研究，请引用原论文。本仓库只提供结构化导航和中文研究笔记，不替代原文。
