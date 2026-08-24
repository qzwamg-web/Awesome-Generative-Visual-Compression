# 生成式视频编码

> 正式发表与预印本严格分栏。训练卡仅在论文明确说明用于训练时记录；仅用于速度测试的 GPU 不计入训练配置。

## 正式发表

| 年份 | 状态 | 论文 | 发表 | 方法族 | 中文核心思路 |
|---:|:---:|---|---|---|---|
| 2022 | ◐ | [Neural Video Compression Using GANs for Detail Synthesis and Propagation](https://arxiv.org/abs/2107.12038) | ECCV | GAN + 细节传播 | 合成未传输纹理并把生成细节传播到后续帧，是“生成细节复用/误差传播”早期基线。 |
| 2022 | ◐ | [Generative Video Compression with a Transformer-Based Discriminator](https://ieeexplore.ieee.org/document/10018030/) | PCS | GAN + Transformer | Transformer 判别器建模非局部相关性，联合特征匹配与感知损失恢复锐利纹理。 |
| 2024 | ◐ | [CGVC-T](https://ieeexplore.ieee.org/document/10496072/) | IEEE JETCAS | 上下文 GAN | 时序上下文同时服务熵模型与条件生成，降低码率并减轻逐帧闪烁。 |
| 2024 | ◐ | [Extreme Video Compression with Pre-trained Diffusion Models](https://arxiv.org/abs/2402.08934) | PCS | 关键帧 + 扩散预测 | 只传参考帧，以条件扩散生成中间帧，换取极低码率。 |
| 2025 | ✅ | [Generative Latent Coding for Ultra-Low Bitrate Image and Video Compression](https://arxiv.org/abs/2505.16177) | IEEE TCSVT | 生成式 latent | 在 VQ-VAE latent 中做时序预测，以时空类别超先验编码语义动态。 |
| 2025 | ✅ | [GIViC](https://arxiv.org/abs/2503.19604) | ICCV | INR + 生成先验 | 对整 GOP 隐式表示做实例优化，以极慢编码换取高压缩率。 |
| 2025 | ◐ | [Diffusion-based Perceptual NVC with Temporal Diffusion Information Reuse](https://dl.acm.org/doi/10.1145/3761815) | ACM TOMM | 扩散信息复用 | 跨帧复用去噪信息，兼顾生成纹理、时序一致性与计算复用。 |
| 2026 | ✅ | [GVC1D](https://arxiv.org/abs/2603.15302) | CVPR | 1-D latent + memory | 一维 token 消除网格冗余，长期记忆聚合跨帧共同语义。 |
| 2026 | ✅ | [GNVC-VD](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_Generative_Neural_Video_Compression_via_Video_Diffusion_Prior_CVPR_2026_paper.html) | CVPR | VideoDiT + flow matching | Wan2.1 视频先验做序列级生成细化，减少逐帧先验的结构幻觉与闪烁。 |
| 2026 | ◐ | [S2VC](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Single-step_Diffusion-based_Video_Coding_with_Semantic-Temporal_Guidance_CVPR_2026_paper.html) | CVPR | 一步扩散 | 用 codec 上下文构造语义/时间引导，把多步扩散压缩为一步。 |
| 2026 | ✅ | [YODA](https://arxiv.org/abs/2601.01141) | IEEE TCSVT Early Access | TA-AE + linear DiT | 多尺度历史参考、条件 latent coder 与一步 DiT 端到端联合训练。 |
| 2026 | ◐ | [GVC-RT](https://arxiv.org/abs/2608.04891) | ACM MM | LFQ 生成 latent | 训练期对齐 LFQ 空间，推理期移除重分支并用轻量 detokenizer 实时解码。 |

## 高相关预印本

| 年份 | 状态 | 论文 | 方法族 | 中文核心思路 |
|---:|:---:|---|---|---|
| 2025 | ◐ | [DiffVC-OSD](https://arxiv.org/abs/2508.07682) | 一步扩散 | 从无噪重建 latent 一步生成，并用 temporal adapter 注入上下文。 |
| 2025 | ◐ | [GLVC](https://arxiv.org/abs/2510.09987) | 连续 tokenizer + memory | 连续生成 latent 中统一 I/P 帧编码，并用递归记忆聚合长期信息。 |
| 2026 | ◐ | [DiffVC-RT](https://arxiv.org/abs/2601.20564) | 实时扩散 | 剪枝、Online Temporal Shift、异步并行和半精度实现实时推理。 |
| 2026 | ✅ | [Free-GVC](https://arxiv.org/abs/2602.09868) | training-free 视频扩散 | 沿扩散 latent 轨迹编码，以跨 GOP 对齐改善时间一致性。 |
| 2026 | ✅ | [Generation Is Compression](https://arxiv.org/abs/2603.26571) | zero-shot rectified flow | 码本索引直接指定随机 rectified-flow 生成轨迹，支持 I2V/T2V/双锚点。 |
| 2026 | ◐ | [Controllable Generative Video Compression](https://arxiv.org/abs/2604.06655) | 可控视频生成 | 关键帧与逐帧条件共同约束生成，强化结构、颜色和运动忠实度。 |
| 2026 | ✅ | [GenVC / Adaptive Score Distillation](https://arxiv.org/abs/2607.22772) | 压缩原生像素扩散 | 从零训练压缩专用视频扩散，并门控会导致运动停滞的错误 DMD 更新。 |

## P 帧误差传播对照

| 工作 | 参考结构 | 误差传播风险 | 主要缓解机制 |
|---|---|---|---|
| GLC-Video | 递归 latent 残差 | token/结构错误进入后续参考 | 时空类别超先验、code prediction |
| GLVC / GVC-RT | I/P latent + 递归记忆 | 错误 latent 被长期记忆 | 连续/LFQ tokenizer、长序列微调 |
| YODA | IPPP，多尺度历史重建 | 上一帧结构偏差逐帧累积 | TA-AE、渐增长序列训练、一步 DiT |
| S2VC / DiffVC-OSD/RT | 条件 codec + 生成细化 | 历史条件偏差与生成闪烁叠加 | 时间引导、adapter、Temporal Shift/一致性损失 |
| GNVC-VD | 上下文 codec + 序列级 VideoDiT | codec 仍递归，但生成不再逐帧独立 | 整段 flow matching refinement |
| GenVC | DCVC-UF 条件 + 32 帧 GOP | 参考误差与一步蒸馏漂移是两类问题 | ASD 梯度门控 + L1/LPIPS/RAFT 光流锚定 |
| 双锚点/zero-shot GVC | GOP 首尾锚点 | 区段级身份/运动幻觉 | 双边界条件与 GOP 边界共享 |

逐篇训练配置、核验证据和更完整的误差分析见 [`data/papers.json`](../data/papers.json) 与 [2026 新工作审计](../docs/latest-video-audit-2026.md)。
