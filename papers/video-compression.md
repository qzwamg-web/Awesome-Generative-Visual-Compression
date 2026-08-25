# 生成式视频编码

> 正式发表与预印本严格分栏。训练卡仅在论文明确说明用于训练时记录；仅用于速度测试的 GPU 不计入训练配置。

## 正式发表

| 年份 | 状态 | 论文 | 发表 | 方法族 | 训练数据集 | 训练硬件（卡数） | 中文核心思路 |
|---:|:---:|---|---|---|---|---|---|
| 2022 | ◐ | [Neural Video Compression Using GANs for Detail Synthesis and Propagation](https://arxiv.org/abs/2107.12038) | ECCV | GAN + 细节传播 | Vimeo-90K 等（待附录细化） | NR（未报告） | 合成未传输纹理并把生成细节传播到后续帧。 |
| 2022 | ◐ | [Generative Video Compression with a Transformer-Based Discriminator](https://ieeexplore.ieee.org/document/10018030/) | PCS | GAN + Transformer | Vimeo-90K（待原文确认） | NR（未报告） | Transformer 判别器建模非局部相关性，以对抗和感知损失恢复锐利纹理。 |
| 2022 | ◐ | [PLVC](https://www.ijcai.org/proceedings/2022/214) | IJCAI | 递归条件 GAN | Vimeo-90K septuplet | NR（未报告） | 判别器联合 latent、运动与递归隐状态，约束空间真实性和长短期时序一致性。 |
| 2024 | ◐ | [CGVC-T](https://ieeexplore.ieee.org/document/10496072/) | IEEE JETCAS | 上下文 GAN | Vimeo-90K 等（待 PDF 核验） | NR（未报告） | 时序上下文同时服务熵模型与条件生成，降低码率并减轻逐帧闪烁。 |
| 2024 | ◐ | [Extreme Video Compression with Pre-trained Diffusion Models](https://arxiv.org/abs/2402.08934) | PCS | 关键帧 + 扩散预测 | 基础扩散数据 + 论文视频数据（待核验） | NR（未报告） | 只传参考帧，以条件扩散生成中间帧，换取极低码率。 |
| 2025 | ✅ | [Generative Latent Coding for Ultra-Low Bitrate Image and Video Compression](https://arxiv.org/abs/2505.16177) | IEEE TCSVT | 生成式 latent | 图像：OpenImages；视频：Vimeo | NR（未报告） | 在 VQ-VAE latent 中做时序预测，以时空类别超先验编码语义动态。 |
| 2025 | ✅ | [GIViC](https://arxiv.org/abs/2503.19604) | ICCV | INR + 生成先验 | 无统一离线训练集；逐 GOP 实例优化 | 训练卡 NR；1×A100 仅复杂度测量 | 对整 GOP 隐式表示做实例优化，以极慢编码换取高压缩率。 |
| 2025 | ◐ | [Diffusion-based Perceptual NVC with Temporal Diffusion Information Reuse](https://dl.acm.org/doi/10.1145/3761815) | ACM TOMM | 扩散信息复用 | 待正式论文核验 | NR（未报告） | 跨帧复用去噪信息，兼顾生成纹理、时序一致性与计算复用。 |
| 2025 | ◐ | [M3-CVC](https://arxiv.org/abs/2411.15798) | ICASSP | 多模态 LMM + 条件扩散 | NR（未报告） | NR（未报告） | 以语义—运动选择关键帧，并用层级文本和条件扩散传输可解释的语义控制信息。 |
| 2025 | ◐ | [DiffVC-OSD](https://arxiv.org/abs/2508.07682) | VCIP | 一步扩散 | Vimeo-90K | NR（训练卡未报告） | 从无噪重建 latent 一步生成，并用 temporal adapter 注入上下文。 |
| 2026 | ✅ | [GVC1D](https://arxiv.org/abs/2603.15302) | CVPR | 1-D latent + memory | Vimeo-90K/扩展 32 帧 Vimeo；OpenVid-HD | NR（未报告） | 一维 token 消除网格冗余，长期记忆聚合跨帧共同语义。 |
| 2026 | ✅ | [GNVC-VD](https://openaccess.thecvf.com/content/CVPR2026/html/Mao_Generative_Neural_Video_Compression_via_Video_Diffusion_Prior_CVPR_2026_paper.html) | CVPR | VideoDiT + flow matching | Vimeo-90K | 2×NVIDIA A800 | Wan2.1 视频先验做序列级生成细化，减少逐帧先验的结构幻觉与闪烁。 |
| 2026 | ◐ | [S2VC](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_Single-step_Diffusion-based_Video_Coding_with_Semantic-Temporal_Guidance_CVPR_2026_paper.html) | CVPR | 一步扩散 | NR（数据集待补充材料核验） | 4×NVIDIA A100 80GB | 用 codec 上下文构造语义/时间引导，把多步扩散压缩为一步。 |
| 2026 | ✅ | [YODA](https://arxiv.org/abs/2601.01141) | IEEE TCSVT Early Access | TA-AE + linear DiT | Vimeo-90K septuplet | NR（训练卡未报告） | 多尺度历史参考、条件 latent coder 与一步 DiT 端到端联合训练。 |
| 2026 | ◐ | [GVC-RT](https://arxiv.org/abs/2608.04891) | ACM MM | LFQ 生成 latent | Vimeo-90K；扩展 29 帧序列微调 | NR（训练卡未报告） | 训练期对齐 LFQ 空间，推理期移除重分支并用轻量 detokenizer 实时解码。 |
| 2026 | ✅ | [T-GVC](https://ojs.aaai.org/index.php/AAAI/article/view/38014) | AAAI | 轨迹引导扩散 | 无 codec 训练（training-free） | 不适用 | 以语义重要的稀疏轨迹在 latent 采样时进行训练外运动引导。 |
| 2026 | ◐ | [PNVC-CR](https://openaccess.thecvf.com/content/CVPR2026/html/Liang_Perceptual_Neural_Video_Compression_with_Color_Separation_and_Rank_Chain_CVPR_2026_paper.html) | CVPR | 色彩分离 + Rank-chain GAN | NR（待补充材料核验） | NR（未报告） | 分离亮/色度编码，并用按码率排序的对抗损失保持感知质量单调性。 |
| 2026 | ✅ | [DiSCo](https://arxiv.org/abs/2512.00408) | CVPR Findings | 语义条件视频扩散 | OpenVid-1M 子集（8,000 视频） | 1×NVIDIA H100 | 传输文本、降质视频和可选草图/姿态，以多模态扩散恢复时空细节。 |

## 高相关预印本

| 年份 | 状态 | 论文 | 方法族 | 训练数据集 | 训练硬件（卡数） | 中文核心思路 |
|---:|:---:|---|---|---|---|---|
| 2025 | ◐ | [Conditional Video Generation for High-Efficiency Video Compression](https://arxiv.org/abs/2507.15269) | 多条件视频扩散 | NR（未报告） | NR（未报告） | 由多粒度稀疏条件生成视频，以模态 dropout 防止模型依赖单一信号。 |
| 2025 | ◐ | [GLVC](https://arxiv.org/abs/2510.09987) | 连续 tokenizer + memory | Vimeo 系列（精确版本待核验） | NR（训练卡未报告） | 连续生成 latent 中统一 I/P 帧编码，并用递归记忆聚合长期信息。 |
| 2025 | ◐ | [Generative Video Compression: Towards 0.01% Compression Rate](https://arxiv.org/abs/2512.24300) | 语义生成式传输 | NR（未报告） | NR（消费级 GPU 仅推理） | 将带宽压力转移到接收端生成计算，并显式权衡压缩率与推理成本。 |
| 2026 | ◐ | [DiffVC-RT](https://arxiv.org/abs/2601.20564) | 实时扩散 | Vimeo-90K（长序列策略待核验） | NR（H800 仅为推理测试） | 剪枝、Online Temporal Shift、异步并行和半精度实现实时推理。 |
| 2026 | ✅ | [Free-GVC](https://arxiv.org/abs/2602.09868) | training-free 视频扩散 | 无（training-free） | 不适用 | 沿扩散 latent 轨迹编码，以跨 GOP 对齐改善时间一致性。 |
| 2026 | ✅ | [Compression as Adaptation](https://arxiv.org/abs/2603.07615) | 隐式适配 + 扩散 | 无统一离线训练集；逐视频拟合 | 8×A100 并行实例；单实例 1×A100 | 把视频编码为冻结扩散模型上的量化 LoRA 适配向量。 |
| 2026 | ✅ | [Generation Is Compression](https://arxiv.org/abs/2603.26571) | zero-shot rectified flow | 无（zero-shot） | 不适用 | 码本索引直接指定随机 rectified-flow 生成轨迹，支持 I2V/T2V/双锚点。 |
| 2026 | ◐ | [Controllable Generative Video Compression](https://arxiv.org/abs/2604.06655) | 可控视频生成 | 待预印本附录核验 | NR（未报告） | 关键帧与逐帧条件共同约束生成，强化结构、颜色和运动忠实度。 |
| 2026 | ✅ | [ZeroGVC](https://arxiv.org/abs/2606.22371) | zero-shot 自回归扩散 | 无额外训练（zero-shot） | 不适用 | 以可复现码本噪声少步重建 P 帧，并可无额外码率使用下一 I 帧抑制误差传播。 |
| 2026 | ✅ | [GenVC / Adaptive Score Distillation](https://arxiv.org/abs/2607.22772) | 压缩原生像素扩散 | OpenVid | 4×NVIDIA A100 80GB | 从零训练压缩专用视频扩散，并门控会导致运动停滞的错误 DMD 更新。 |
| 2026 | ◐ | [ReGenVC](https://arxiv.org/abs/2607.28144) | 姿态条件四步 VideoDiT | talking-head 蒸馏数据 NR | 训练卡 NR；8 卡仅实时解码 | 首帧与姿态构成极小码流，以蒸馏和多卡流水实现 24 fps 解码。 |
| 2026 | ✅ | [DiffVC-ONE](https://arxiv.org/abs/2608.20515) | 一步 VideoDiT + 统一 latent codec | OpenVid-HD（36,971 clips） | NR（型号与卡数均未报告） | U2LC 统一压缩 latent slices，混合条件控制一步 VideoDiT 对整 GOP 做时空增强。 |

逐篇训练配置与核验证据见 [`data/papers.json`](../data/papers.json)。
