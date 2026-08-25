# 生成式图像编码

> ✅：训练配置已完成首轮核验；◐：已有完整字段，但仍含 `待核验/NR` 项。详细结构化配置见 [`data/papers.json`](../data/papers.json)。

## 正式发表

| 年份 | 状态 | 论文 | 发表 | 方法族 | 训练数据集 | 训练硬件（卡数） | 中文核心思路 |
|---:|:---:|---|---|---|---|---|---|
| 2023 | ✅ | [Lossy Image Compression with Conditional Diffusion Models](https://arxiv.org/abs/2209.06950) | NeurIPS | 条件扩散 | ImageNet train | NR（未报告） | 熵编码内容 latent，扩散模型在解码端合成未传输纹理。 |
| 2023 | ◐ | [Improving Statistical Fidelity for Neural Image Compression with Implicit Local Likelihood Models](https://proceedings.mlr.press/v202/muckley23a.html) | ICML | GAN / ILLM | OpenImages | NR（未报告） | 以隐式局部似然约束重建分布，形成极低码率强感知基线。 |
| 2024 | ✅ | [Towards Image Compression with Perfect Realism at Ultra-Low Bitrates](https://arxiv.org/abs/2310.10325) | ICLR | 文本 + VQ + 扩散 | OpenImages | NR（未报告） | 局部 VQ token 保结构，全局文本补语义，扩散生成高真实度纹理。 |
| 2024 | ◐ | [Generative Latent Coding for Ultra-Low Bitrate Image Compression](https://openaccess.thecvf.com/content/CVPR2024/html/Jia_Generative_Latent_Coding_for_Ultra-Low_Bitrate_Image_Compression_CVPR_2024_paper.html) | CVPR | 生成式 latent | ImageNet（阶段 I）；OpenImages（阶段 II/III） | NR（未报告） | 在 VQ-VAE 语义 latent 中变换编码，并用类别超先验减少辅助码率。 |
| 2024 | ✅ | [Lossy Image Compression with Foundation Diffusion Models](https://arxiv.org/abs/2404.08580) | ECCV | 基础扩散先验 | Vimeo-90K | NR（未报告） | 将量化误差恢复视为从中间噪声状态开始的短程去噪。 |
| 2024 | ◐ | [Correcting Diffusion-Based Perceptual Image Compression with Privileged End-to-End Decoder](https://proceedings.mlr.press/v235/ma24s.html) | ICML | 特权解码校正 | 论文所列自然图像训练集 | NR（未报告） | 用训练期特权确定性解码器纠正扩散生成的结构与颜色偏差。 |
| 2024 | ◐ | [Toward Extreme Image Compression With Latent Feature Guidance and Diffusion Prior](https://ieeexplore.ieee.org/document/10669055/) | TCSVT | latent 引导扩散 | 待全文核验 | NR（未报告） | 用可传输结构 latent 约束预训练扩散先验，降低内容漂移。 |
| 2025 | ✅ | [PICD: Versatile Perceptual Image Compression with Diffusion Rendering](https://arxiv.org/abs/2505.05853) | CVPR | LoRA + adaptor | 论文所列域数据（含自然图像） | 1×NVIDIA A100 | 域级 LoRA 与轻量条件适配器把通用扩散模型转成可复用渲染解码器。 |
| 2025 | ◐ | [DLF: Extreme Image Compression with Dual-generative Latent Fusion](https://openaccess.thecvf.com/content/ICCV2025/html/Xue_DLF_Extreme_Image_Compression_with_Dual-generative_Latent_Fusion_ICCV_2025_paper.html) | ICCV Highlight | 双生成 latent | OpenImages train 子集 | NVIDIA A100 40GB；卡数 NR | 融合公共语义 token 与实例细节 latent，补足单一码本对个体细节的忽略。 |
| 2025 | ✅ | [StableCodec: Taming One-Step Diffusion for Extreme Image Compression](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_StableCodec_Taming_One-Step_Diffusion_for_Extreme_Image_Compression_ICCV_2025_paper.html) | ICCV | 一步扩散 | DF2K + CLIC2020 Professional | 2×RTX 3090 | 两阶段训练将多步扩散压缩为单次生成，兼顾低码率质量和速度。 |
| 2025 | ◐ | [Compressed Image Generation with Denoising Diffusion Codebook Models](https://proceedings.mlr.press/v267/ohayon25a.html) | ICML | 扩散噪声码本 | 依预训练 DDM；压缩时逐图优化 | NR（未报告） | 把反向扩散噪声选择离散成可传输索引，使生成过程本身成为编码。 |
| 2025 | ◐ | [Ultra Lowrate Image Compression with Semantic Residual Coding and Compression-aware Diffusion](https://proceedings.mlr.press/v267/ke25c.html) | ICML | 语义残差扩散 | 待附录核验 | NR（未报告） | 传输语义残差，并按码率选择扩散时刻，对齐压缩强度和生成难度。 |
| 2025 | ◐ | [One-Step Diffusion-Based Image Compression with Semantic Distillation](https://arxiv.org/abs/2505.16687) | NeurIPS | 一步扩散蒸馏 | GLC/相关工作的自然图像数据 | 4×NVIDIA A100 | 以超先验传语义条件，用教师扩散蒸馏到一步解码器。 |
| 2025 | ◐ | [Diff-ICMH](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5c33e9aedee21daeda9e03f43ec4865d-Abstract-Conference.html) | NeurIPS | 扩散先验 + 语义一致性 | 自然图像集（精确组成待核验） | NR（未报告） | 同一码流兼顾人眼真实性与分类/检测/分割语义，并以少量 tag 比特激活扩散先验。 |
| 2025 | ✅ | [OSCAR](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7b372097a499ce99a4b1e41feb79493a-Abstract-Conference.html) | NeurIPS | 多码率一步扩散 | OpenImages | 1×NVIDIA RTX A6000 | 把码率映射成伪扩散时间步，以单一模型支持多个码率的一步重建。 |
| 2026 | ✅ | [ProGIC: Progressive and Lightweight Generative Image Compression](https://arxiv.org/abs/2603.02897) | CVPR Findings | 渐进 RVQ | ImageNet 全量（每 epoch 采样 1%） | NR（未报告） | 多级残差 token 支持渐进预览，轻量生成器面向移动部署。 |
| 2026 | ◐ | [CoD: A Diffusion Foundation Model for Image Compression](https://arxiv.org/abs/2511.18706) | CVPR | 压缩基础扩散模型 | 开放图像数据混合 | 卡数 NR；约 6,250 A100 GPU-days | 专门预训练面向压缩的扩散基础模型，统一覆盖码率、失真与感知条件。 |
| 2026 | ◐ | [DiffO](https://openaccess.thecvf.com/content/WACV2026/html/Park_Single-step_Diffusion_for_Image_Compression_at_Ultra-Low_Bitrates_WACV_2026_paper.html) | WACV | VQ-residual 一步扩散 | 自然图像集（待配置核验） | 官方命令 1×GPU；型号 NR | 分离结构 base code 与细节 residual，并按码率调节一步去噪强度。 |
| 2026 | ◐ | [CADC](https://openaccess.thecvf.com/content/CVPR2026/html/Sheng_CADC_Content_Adaptive_Diffusion-Based_Generative_Image_Compression_CVPR_2026_paper.html) | CVPR | 内容自适应扩散 | 自然图像集（待补充材料核验） | NR（未报告） | 自适应量化、信息集中与零比特文本条件共同对齐 codec 和生成先验。 |
| 2026 | ◐ | [RDVQ](https://openaccess.thecvf.com/content/CVPR2026/html/Jiang_Differentiable_Vector_Quantization_for_Rate-Distortion_Optimization_of_Generative_Image_Compression_CVPR_2026_paper.html) | CVPR Oral | 可微 VQ + AR 熵模型 | 自然图像集（待配置核验） | NR（4090 仅推理） | 用可微码本分布端到端优化率失真，并以 token 前缀支持测试时码率控制。 |
| 2026 | ✅ | [DiT-IC](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_DiT-IC_Aligned_Diffusion_Transformer_for_Efficient_Image_Compression_CVPR_2026_paper.html) | CVPR | 32× latent 一步 DiT | LSDIR + MLIC-Train-100K | 官方复现 2×GPU；型号 NR | 在深压缩 latent 上以 flow、自蒸馏和 latent 条件完成文本无关的一步 DiT 解码。 |

## 高相关预印本

| 年份 | 状态 | 论文 | 方法族 | 训练数据集 | 训练硬件（卡数） | 中文核心思路 |
|---:|:---:|---|---|---|---|---|
| 2025 | ◐ | [Rate-variable Feature Distribution GIC](https://arxiv.org/abs/2505.20984) | 压缩路径 SDE | NR（未报告） | NR（未报告） | 把压缩视作前向扩散路径，直接从压缩特征少步反演而非从高斯噪声生成。 |
| 2026 | ◐ | [CoD-Lite](https://arxiv.org/abs/2604.12525) | 轻量卷积一步扩散 | 压缩原生预训练集（待核验） | NR（未报告） | 用压缩原生预训练、蒸馏和对抗学习实现 1080p 实时生成式图像压缩。 |
| 2026 | ◐ | [FlowCodec](https://arxiv.org/abs/2606.21030) | 一步 flow prior | NR（未报告） | NR（未报告） | 将 latent 压缩与一步 transport 解耦，以低于 0.54% 参数适配 Qwen-Image/FLUX。 |

## 训练配置阅读建议

- 多阶段方法按阶段比较，不能只看单一学习率。
- “使用 A100 测速度”不等于“使用 A100 训练”；结构化数据中已分开标注。
- 对 Stable Diffusion/视频 DiT 类工作，需区分基础模型预训练成本与压缩适配成本。
