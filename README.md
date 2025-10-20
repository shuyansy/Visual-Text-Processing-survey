# Survey-of-Visual-Text-Processing
The official project of paper "[Visual Text Processing: A Comprehensive Review and Unified Evaluation](https://arxiv.org/abs/2504.21682 )"

![LOGO](logo.png)

This repository contains a paper collection of recent works for visual text processing tasks.

## 📚 VTPBench
![LOGO](vtpbench_2.png)
We propose VTPBench, a multi-task benchmark comprising 4,305 samples across six visual text processing tasks.

### Dataset
We release the dataset of VTPBench in [Data](https://huggingface.co/datasets/sy1998/VTP_Bench)

### Evaluation
VTPBech utilizes GPT-4 as the evaluation method, which provides an easy implementation for unified VTP evaluation. Please see the evaluation code [here](VTP_Bench). 

(1) Infer your visual text processing models (e.g., Scene Text Removal Models) on the provided dataset. Then, concatenate the predicted one with the GT, like the [examples](VTP_Bench/STR/STR_data/viteraser) we provide. 

(2) Run the following code to get evaluation results.
```bash
cd STR
python gpt_str.py
python get_str_score.py
```

## 📖 Table of Contents 👀
- [Text Image Super-resolution](#text-image-Super-resolution)
- [Document Image Dewarping](#Document-Image-Dewarping)
- [Text Image Denosing](#Text-Image-Denosing)
- [Scene Text Removal](#Scene-Text-Removal)
- [Scene Text Editing](#Scene-Text-Editing)
- [Scene Text Generation](#Scene-Text-Generation)
##

### Text Image Super-resolution
+ Boosting Optical Character Recognition: A Super-Resolution Approach (**2015 arxiv**) [paper](https://arxiv.org/pdf/1506.02211.pdf)
+ ICDAR2015 competition on Text Image Super-Resolution
 (**2015 ICDAR**) [paper](https://ieeexplore.ieee.org/document/7333951)
+ Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network (**2017 CVPR**) [paper](https://openaccess.thecvf.com/content_cvpr_2017/html/Ledig_Photo-Realistic_Single_Image_CVPR_2017_paper.html)
+ TextSR: Content-Aware Text Super-Resolution Guided by Recognition (**2019 arxiv**) [paper](https://arxiv.org/pdf/1909.07113.pdf) [code](https://github.com/xieenze/TextSR)
+ Selective Super-Resolution for Scene Text Images (**2019 ICDAR**) [paper](https://ieeexplore.ieee.org/abstract/document/8977974)
+ Text-Attentional Conditional Generative Adversarial Network for Super-Resolution of Text Images (**2019 ICME**) [paper](https://ieeexplore.ieee.org/abstract/document/8784962)
+ Collaborative Deep Learning for Super-Resolving Blurry Text Images (**2020 TCI**) [paper](https://ieeexplore.ieee.org/abstract/document/9040515)
+ PlugNet: Degradation Aware Scene Text Recognition Supervised by a Pluggable Super-Resolution Unit (**2020 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-58555-6_10)
+ Scene Text Image Super-Resolution in the Wild (**2020 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-58607-2_38) [code](https://github.com/WenjiaWang0312/TextZoom)
+ Scene Text Telescope: Text-Focused Scene Image Super-Resolution (**2021 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Chen_Scene_Text_Telescope_Text-Focused_Scene_Image_Super-Resolution_CVPR_2021_paper.pdf)
+ Scene Text Image Super-Resolution via Parallelly Contextual Attention Network (**2021 CVPR**) [paper](https://dl.acm.org/doi/abs/10.1145/3474085.3475469)
+ Text Prior Guided Scene Text Image Super-Resolution (**2021 TIP**) [paper](https://ieeexplore.ieee.org/abstract/document/10042236) [code](https://github.com/mjq11302010044/TPGSR)
+ A text attention network for spatial deformation robust scene text image super-resolution  (**2022 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Ma_A_Text_Attention_Network_for_Spatial_Deformation_Robust_Scene_Text_CVPR_2022_paper.pdf) [code](https://github.com/mjq11302010044/TATT)
+ C3-STISR: Scene Text Image Super-resolution with Triple Clues (**2022 IJCAI**) [paper]
+ Text gestalt: Stroke-aware scene text image super-resolution (**2022 AAAI**) [paper](https://ojs.aaai.org/index.php/AAAI/article/download/19904/19663) [code](https://github.com/FudanVI/FudanOCR/tree/main/text-gestalt)
+ A Benchmark for Chinese-English Scene Text Image Super-Resolution (**2023 ICCV**) [paper](https://openaccess.thecvf.com/content/ICCV2023/html/Ma_A_Benchmark_for_Chinese-English_Scene_Text_Image_Super-Resolution_ICCV_2023_paper.html) [code](https://github.com/mjq11302010044/Real-CE)
+ Text Image Super-Resolution Guided by Text Structure and Embedding Priors (**2023 ACM MM**) [paper](https://dl.acm.org/doi/abs/10.1145/3595924)
+ Towards robust scene text image super-resolution via explicit location enhancement (**2023 ACM MM**) [paper](https://arxiv.org/pdf/2307.09749.pdf) [code](https://github.com/csguoh/LEMMA)
+ Improving Scene Text Image Super-Resolution via Dual Prior Modulation Network (**2023 AAAI**) [paper](https://arxiv.org/pdf/2302.10414.pdf) [code](https://github.com/jdfxzzy/DPMN)
+ Learning Generative Structure Prior for Blind Text Image Super-Resolution (**2023 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Learning_Generative_Structure_Prior_for_Blind_Text_Image_Super-Resolution_CVPR_2023_paper.html) [code](https://github.com/csxmli2016/MARCONet)
+ Scene Text Image Super-resolution based on Text-conditional Diffusion Models (**2024 WACV**) [paper](https://openaccess.thecvf.com/content/WACV2024/papers/Noguchi_Scene_Text_Image_Super-Resolution_Based_on_Text-Conditional_Diffusion_Models_WACV_2024_paper.pdf) [code](https://github.com/ToyotaInfoTech/stisr-tcdm)
+ GARDEN: Generative prior guided network for scene text image super-resolution (**2024 ICDAR**) [paper](https://link.springer.com/chapter/10.1007/978-3-031-70549-6_12)
+ Scene text image super-resolution through multi-scale interaction of structural and semantic priors (**2024 TAI**) [paper](https://ieeexplore.ieee.org/document/10473520)
+ PEAN: A Diffusion-Based Prior-Enhanced Attention Network for Scene Text Image Super-Resolution (**2024 ACM MM**) [paper](https://arxiv.org/abs/2311.17955) [code](https://github.com/jdfxzzy/PEAN)
+ Diffusion-based blind text image super-resolution (**2024 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Diffusion-based_Blind_Text_Image_Super-Resolution_CVPR_2024_paper.pdf) [code](https://github.com/YuzheZhang-1999/DiffTSR)
+ Diffusion-conditioned-diffusion model for scene text image super-resolution (**2024 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-031-72633-0_17)
+ QT-TextSR: Enhancing scene text image super-resolution via efficient interaction with text recognition using a query-aware transformer (**2024 Neurocomputing**) [paper](https://dl.acm.org/doi/10.1016/j.neucom.2024.129241) [code](https://github.com/lcy0604/QT-TextSR)



### Document Image Dewarping
+ A Fast Page Outline Detection and Dewarping Method Based on Iterative Cut and Adaptive Coordinate Transform (**2019 ICDARW**) [paper](https://ieeexplore.ieee.org/abstract/document/8892891)
+ DocUNet: Document Image Unwarping via a Stacked U-Net （**2018 CVPR**）[paper](https://openaccess.thecvf.com/content_cvpr_2018/papers/Ma_DocUNet_Document_Image_CVPR_2018_paper.pdf)
+ DewarpNet: Single-Image Document Unwarping With Stacked 3D and 2D Regression Networks (**2019 ICCV**) [paper](https://openaccess.thecvf.com/content_ICCV_2019/papers/Das_DewarpNet_Single-Image_Document_Unwarping_With_Stacked_3D_and_2D_Regression_ICCV_2019_paper.pdf) [code](https://www.cs.stonybrook.edu/%E2%88%BCcvl/dewarpnet.html)
+ Document rectification and illumination correction using a patch-based CNN (**2019 TOG**) [paper](https://dl.acm.org/doi/abs/10.1145/3355089.3356563)
+ Dewarping Document Image by Displacement Flow Estimation with Fully Convolutional Network (**2020 IAPR**) [paper](https://arxiv.org/pdf/2104.06815)
+ Geometric rectification of document images using adversarial gated unwarping network (**2020 PR**) [paper](https://www.sciencedirect.com/science/article/abs/pii/S0031320320303794)
+ DocScanner: Robust Document Image Rectification with Progressive Learning (**2021 arxiv**) [paper](https://arxiv.org/pdf/2110.14968.pdf)
+ End-to-End Piece-Wise Unwarping of Document Images (**2021 ICCV**) [paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Das_End-to-End_Piece-Wise_Unwarping_of_Document_Images_ICCV_2021_paper.pdf)
+ Document Dewarping with Control Points (**2021 ICDAR**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-86549-8_30) [paper](https://github.com/gwxie/Document-Dewarping-with-Control-Points)
+ DocTr: Document Image Transformer for Geometric Unwarping and Illumination Correction (**2021 ACM MM**) [paper](https://arxiv.org/pdf/2110.12942.pdf) [code](https://github.com/fh2019ustc/DocTr)
+ Revisiting Document Image Dewarping by Grid Regularization (**2022 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Jiang_Revisiting_Document_Image_Dewarping_by_Grid_Regularization_CVPR_2022_paper.pdf)
+ Fourier Document Restoration for Robust Document Dewarping and Recognition (**2022 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2022/html/Xue_Fourier_Document_Restoration_for_Robust_Document_Dewarping_and_Recognition_CVPR_2022_paper.html)
+ Learning an Isometric Surface Parameterization for Texture Unwrapping (**2022 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-031-19836-6_33) [code](https://github.com/cvlab-stonybrook/Iso-UVField)
+ Geometric Representation Learning for Document Image Rectification (**2022 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-031-19836-6_27)
+ Learning From Documents in the Wild to Improve Document Unwarping (**2022 SIGGRAPH**) [paper](https://dl.acm.org/doi/abs/10.1145/3528233.3530756) [code](https://github.com/cvlab-stonybrook/PaperEdge)
+ Marior: Margin Removal and Iterative Content Rectification for Document Dewarping in the Wild (**2023 ACM MM**) [paper](https://arxiv.org/pdf/2207.11515.pdf) [code](https://github.com/ZZZHANG-jx/Marior)
+ DocAligner: Annotating Real-world Photographic Document Images by Simply Taking Pictures (**2023 arxiv**) [paper](https://arxiv.org/pdf/2306.05749.pdf)
+ DocMAE: Document Image Rectification via Self-supervised Representation Learning (**2023 ICME***) [paper](https://arxiv.org/pdf/2304.10341.pdf)
+ Deep Unrestricted Document Image Rectification (**2023 TMM**) [paper](https://arxiv.org/pdf/2304.08796.pdf) [code](https://github.com/fh2019ustc/DocTr-Plus)
+ Layout-aware Single-image Document Flattening (**2023 TOG**) [paper](https://dl.acm.org/doi/abs/10.1145/3627818) [code](https://github.com/BunnySoCrazy/LA-DocFlatten)
+ Polar-Doc: One-Stage Document Dewarping with Multi-Scope Constraints under Polar Representation (**2023 arxiv**) [paper](https://arxiv.org/pdf/2312.07925.pdf)
+ DocReal: Robust Document Dewarping of Real-Life Images via Attention-Enhanced Control Point Prediction (**2023 WACV**) [paper](https://openaccess.thecvf.com/content/WACV2024/papers/Yu_DocReal_Robust_Document_Dewarping_of_Real-Life_Images_via_Attention-Enhanced_Control_WACV_2024_paper.pdf) [code](https://github.com/irisXcoding/DocReal)
+ Rethinking Supervision in Document Unwarping: A Self-consistent Flow-free Approach (**2023 TCSVT**) [paper](https://ieeexplore.ieee.org/abstract/document/10327775)
+ Am I readable? Transfer learning based document image rectification (**2024 IJDAR**) [paper](https://link.springer.com/article/10.1007/s10032-024-00476-9)
+ Efficient Joint Rectification of Photometric and Geometric Distortions in Document Images (**2024 ICASSP**) [paper](https://ieeexplore.ieee.org/abstract/document/10447446)

  

### Text Image Denosing
+ Shading Removal of Illustrated Documents (**2013 ICDAR**) [paper](https://link.springer.com/chapter/10.1007/978-3-642-39094-4_35)
+ Nonparametric illumination correction for scanned document images via convex hulls (**2013 TPAMI**) [paper](https://ieeexplore.ieee.org/abstract/document/6361405)
+ Removing shadows from images of documents (**2016 ACCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-319-54187-7_12)
+ Document enhancement using visibility detection (**2018 CVPR**) [paper](https://openaccess.thecvf.com/content_cvpr_2018/papers/Kligler_Document_Enhancement_Using_CVPR_2018_paper.pdf)
+ Water-Filling: An Efficient Algorithm for Digitized Document Shadow Removal (**2018 ACCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-20887-5_25)
+ Learning to Clean: A GAN Perspective (**2018 ACCVW**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-21074-8_14)
+ Deeperase: Weakly supervised ink artifact removal in document text images (**2020 WACV**) [paper](https://openaccess.thecvf.com/content_WACV_2020/papers/Qi_DeepErase_Weakly_Supervised_Ink_Artifact_Removal_in_Document_Text_Images_WACV_2020_paper.pdf)
+ From Shadow Segmentation to Shadow Removal (**2020 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-58621-8_16)
+ BEDSR-Net: A Deep Shadow Removal Network From a Single Document Image (**2020 CVPR**) [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Lin_BEDSR-Net_A_Deep_Shadow_Removal_Network_From_a_Single_Document_CVPR_2020_paper.pdf)
+ Light-Weight Document Image Cleanup Using Perceptual Loss (**2021 ICDAR**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-86334-0_16)
+ RecycleNet: An Overlapped Text Instance Recovery Approach (**2021 ACM MM**) [paper](https://dl.acm.org/doi/abs/10.1145/3474085.3481536)
+ End-to-End Unsupervised Document Image Blind Denoising (**2021 ICCV**) [paper](https://openaccess.thecvf.com/content/ICCV2021/papers/Gangeh_End-to-End_Unsupervised_Document_Image_Blind_Denoising_ICCV_2021_paper.pdf)
+ Bijective mapping network for shadow removal (**2022 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Zhu_Bijective_Mapping_Network_for_Shadow_Removal_CVPR_2022_paper.pdf)
+ Style-guided shadow removal (**2022 ECCV**) [paper](https://link.springer.com/chapter/10.1007/978-3-031-19800-7_21) [code](https://github.com/jinwan1994/SG-ShadowNet)
+ UDoc-GAN: Unpaired Document Illumination Correction with Background Light Prior (**2022 ACM MM**) [paper](https://dl.acm.org/doi/abs/10.1145/3503161.3547916) [code](https://github.com/harrytea/UDoc-GAN)
+ LP-IOANet: Efficient High Resolution Document Shadow Removal (**2023 ICASSP**) [paper](https://ieeexplore.ieee.org/abstract/document/10095920)
+ Shadow Removal of Text Document Images Using Background Estimation and Adaptive Text Enhancement (**2023 ICASSP**) [paper](https://ieeexplore.ieee.org/abstract/document/10096115)
+ Mask-Guided Stamp Erasure for Real Document Image (**2023 ICME**) [paper](https://ieeexplore.ieee.org/abstract/document/10219771)
+ Document Image Shadow Removal Guided by Color-Aware Background (**2023 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2023/papers/Zhang_Document_Image_Shadow_Removal_Guided_by_Color-Aware_Background_CVPR_2023_paper.pdf)
+ DocDiff: Document Enhancement via Residual Diffusion Models (**2023 ACM MM**) [paper](https://dl.acm.org/doi/abs/10.1145/3581783.3611730) [code](https://github.com/Royalvice/DocDiff)
+ DocNLC: A Document Image Enhancement Framework with Normalized and Latent Contrastive Representation for Multiple Degradations (**2024 AAAI**) [paper](https://ojs.aaai.org/index.php/AAAI/article/view/28366) [code](https://github.com/RylonW/DocNLC)
+ DocRes: A Generalist Model Toward Unifying Document Image Restoration Tasks (**2024 CVPR**) [paper](https://arxiv.org/pdf/2405.04408.pdf) [code](https://github.com/ZZZHANG-jx/DocRes)


### Scene Text Removal
+ Image-to-Image Translation with Conditional Adversarial Networks<sup>*</sup> (**2017 CVPR**)  [paper](https://openaccess.thecvf.com/content_cvpr_2017/papers/Isola_Image-To-Image_Translation_With_CVPR_2017_paper.pdf)
+ Scene text eraser (**2017 ICDAR**) [paper](https://arxiv.org/pdf/1705.02772.pdf)
+ Automatic Semantic Content Removal by Learning to Neglect (**2018 BMVC**) [paper](https://arxiv.org/pdf/1807.07696.pdf)
+ Ensnet: Ensconce text in the wild (**2019 AAAI**) [paper](https://ojs.aaai.org/index.php/AAAI/article/download/3859/3737) [code](https://github.com/HCIILAB/Scene-Text-Removal)
+ Mtrnet: A generic scene text eraser (**2019 ICDAR**) [paper](https://arxiv.org/pdf/1903.04092)
+ Erasenet: End-to-end text removal in the wild (**2020 TIP**) [paper](https://ieeexplore.ieee.org/abstract/document/9180003) [code](https://github.com/HCIILAB/SCUT-EnsText)
+ Mtrnet++: One-stage mask-based scene text eraser (**2020 CVIU**) [paper](https://arxiv.org/pdf/1912.07183.pdf)
+ Erasing scene text with weak supervision (**2020 WACV**) [paper](https://openaccess.thecvf.com/content_WACV_2020/papers/Zdenek_Erasing_Scene_Text_with_Weak_Supervision_WACV_2020_paper.pdf)
+ Stroke-Based Scene Text Erasing Using Synthetic Data for Training (**2021 TIP**) [paper](https://ieeexplore.ieee.org/abstract/document/9609970)
+ Text region conditional generative adversarial network for text concealment in the wild (**2021 TCSVT**) [paper](https://ieeexplore.ieee.org/abstract/document/9509541)
+ Two-Stage Seamless Text Erasing On Real-World Scene Images (**2021 ICIP**) [paper](https://ieeexplore.ieee.org/abstract/document/9506394)
+ Scene text removal via cascaded text stroke detection and erasing (**2022 CVM**) [paper](https://link.springer.com/content/pdf/10.1007/s41095-021-0242-8.pdf)
+ Self-supervised text erasing with controllable image synthesis (**2022 ACM MM**) [paper](https://arxiv.org/pdf/2204.12743.pdf)
+ Multi-branch network with ensemble learning for text removal in the wild (**2022 ACCV**) [paper](https://openaccess.thecvf.com/content/ACCV2022/papers/Hou_Multi-Branch_Network_with_Ensemble_Learning_for_Text_Removal_in_the_ACCV_2022_paper.pdf)
+ The Surprisingly Straightforward Scene Text Removal Method with Gated Attention and Region of Interest Generation: A Comprehensive Prominent Model Analysis (**2022 ECCV**) [paper](https://arxiv.org/pdf/2210.07489) [code](https://github.com/naver/garnet)
+ Don’t forget me: accurate background recovery for text removal via modeling local-global context (**2022 ECCV**) [paper](https://arxiv.org/pdf/2207.10273) [code](https://github.com/lcy0604/CTRNet.)
+ Psstrnet: progressive segmentation-guided scene text removal network (**2022 ICME**) [paper](https://arxiv.org/pdf/2306.07842)
+ Fetnet: Feature erasing and transferring network for scene text removal (**2023 PR**) [paper](https://arxiv.org/pdf/2306.09593)
+ Modeling stroke mask for end-to-end text erasing (**2023 WACV**) [paper](https://openaccess.thecvf.com/content/WACV2023/papers/Du_Modeling_Stroke_Mask_for_End-to-End_Text_Erasing_WACV_2023_paper.pdf)
+ Viteraser: Harnessing the power of vision transformers for scene text removal with segmim pretraining (**2023 arxiv**) [paper](https://arxiv.org/pdf/2306.12106) [code](https://github.com/shannanyinxiang/ViTEraser)
+ Progressive scene text erasing with self-supervision (**2023 CVIU**) [paper](https://arxiv.org/pdf/2207.11469.pdf)
+ What is the Real Need for Scene Text Removal? Exploring the Background Integrity and Erasure Exhaustivity Properties (**2023 TIP**) [paper](https://ieeexplore.ieee.org/abstract/document/10214243) [code](https://github.com/wangyuxin87/PERT)
+ PERT: A Progressively Region-based Network for Scene Text Removal (**2023 TIP**) [paper](https://ieeexplore.ieee.org/document/10214243) [code](https://github.com/wangyuxin87/PERT)
+ Selective scene text removal (**2023 BMVC**) [paper](https://arxiv.org/pdf/2309.00410.pdf) [code](https://github.com/mitanihayato/Selective-Scene-Text-Removal)
+ FETNet: Feature Erasing and Transferring Network for Scene Text Removal (**2023 PR**) [paper](https://arxiv.org/abs/2306.09593) [code](https://github.com/GuangtaoLyu/FETNet)
   
 

### Scene Text Editing
+ Scene text magnifier (**2019 ICDAR**) [paper](https://arxiv.org/pdf/1907.00693.pdf)
+ Selective style transfer for text (**2019 ICDAR**) [paper](https://arxiv.org/pdf/1906.01466.pdf) [code](https://github.com/furkanbiten/SelectiveTextStyleTransfer)
+ Editing text in the wild (**2019 ACM MM**) [paper](https://arxiv.org/pdf/1908.03047.pdf) [code](https://github.com/youdao-ai/SRNet)
+ Swaptext: Image based texts transfer in scenes (**2020 CVPR**) [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Yang_SwapText_Image_Based_Texts_Transfer_in_Scenes_CVPR_2020_paper.pdf)
+ Scene text transfer for cross-language (**2021 ICIG**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-87355-4_46)
+ Mask-guided gan for robust text editing in the scene (**2021 Neurocomputing**) [paper](https://www.sciencedirect.com/science/article/abs/pii/S092523122100299X)
+ Stefann: scene text editor using font adaptive neural network (**2020 CVPR**) [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Roy_STEFANN_Scene_Text_Editor_Using_Font_Adaptive_Neural_Network_CVPR_2020_paper.pdf)
+ Deep learning-based forgery attack on document images (**2021 TIP**) [paper](https://arxiv.org/pdf/2102.00653)
+ Strive: Scene text replacement in videos (**2021 ICCV**) [paper](https://openaccess.thecvf.com/content/ICCV2021/papers/G_STRIVE_Scene_Text_Replacement_in_Videos_ICCV_2021_paper.pdf)
+ RewriteNet: Reliable Scene Text Editing with Implicit Decomposition of Text Contents and Styles (**2022 CVPRW**) [paper](https://arxiv.org/pdf/2107.11041.pdf) [code](https://github.com/clovaai/rewritenet)
+ Fast: Font-agnostic scene text editing (**2023 arxiv**) [paper](https://arxiv.org/abs/2308.02905)
+ Letter Embedding Guidance Diffusion Model for Scene Text Editing (**2023 ICME**) [paper](http://ercdm.sdu.edu.cn/__local/1/D6/7E/7C1DDDEFCDC240906F00E254B02_354743F8_1C042B.pdf)
+ Exploring stroke-level modifications for scene text editing (**2023 AAAI**) [paper](https://ojs.aaai.org/index.php/AAAI/article/view/25305/25077) [code](https://github.com/qqqyd/MOSTEL) 
+ Textstylebrush: Transfer of text aesthetics from a single example (**2023 TPAMI**) [paper](https://arxiv.org/pdf/2106.08385.pdf)
+ Self-Supervised Cross-Language Scene Text Editing (**2023 ACM MM**) [paper](https://dl.acm.org/doi/abs/10.1145/3581783.3612174)
+ Scene style text editing (**2023 arxiv**) [paper](https://arxiv.org/pdf/2304.10097.pdf)
+ Improving Diffusion Models for Scene Text Editing with Dual Encoders (**2023 arxiv**) [paper](https://arxiv.org/pdf/2304.05568.pdf) [code](https://github.com/UCSB-NLP-Chang/DiffSTE)
+ Towards scene-text to scene-text translation (**2023 arxiv**) [paper](https://arxiv.org/pdf/2308.03024.pdf)
+ DiffUTE: Universal Text Editing Diffusion Model (**2023 NIPS**) [paper](https://arxiv.org/abs/2305.10825) [code](https://github.com/chenhaoxing/DiffUTE)
+ On manipulating scene text in the wild with diffusion models (**2024 WACV**) [paper](https://arxiv.org/pdf/2311.00734.pdf) 
+ AnyText: Multilingual Visual Text Generation And Editing (**2024 ICLR**) [paper](https://arxiv.org/pdf/2311.03054) [code](https://github.com/tyxsspa/AnyText)
+ Choose What You Need: Disentangled Representation Learning for Scene Text Recognition, Removal and Editing (**2024 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2024/papers/Zhang_Choose_What_You_Need_Disentangled_Representation_Learning_for_Scene_Text_CVPR_2024_paper.pdf)
+ TextCtrl: Diffusion-based Scene Text Editing with Prior Guidance Control (**2024 NIPS**) [paper](https://arxiv.org/pdf/2410.10133) [code](https://github.com/weichaozeng/TextCtrl)
+ How Control Information Influences Multilingual Text Image Generation and Editing? (**2024 NIPS**) [paper](https://arxiv.org/pdf/2407.11502) [code](https://github.com/CyrilSterling/TextGen)
+ TextMaster: Universal Controllable Text Edit (**2024 arxiv**) [paper](https://arxiv.org/pdf/2410.09879)
+ AnyText2: Visual Text Generation and Editing With Customizable Attributes (**2024 arxiv**) [paper](https://arxiv.org/pdf/2411.15245) [code](https://github.com/tyxsspa/AnyText2)
+ Recognition-Synergistic Scene Text Editing (**2025 CVPR**) [paper](https://arxiv.org/pdf/2503.08387) [code](https://github.com/ZhengyaoFang/RS-STE) 
+ GlyphMastero: A Glyph Encoder for High-Fidelity Scene Text Editing (**2025 CVPR**) [paper](https://arxiv.org/pdf/2505.04915)
+ Type-R: Automatically Retouching Typos for Text-to-Image Generation(**2025 CVPR**) [paper](https://arxiv.org/pdf/2411.18159) [code](https://github.com/CyberAgentAILab/Type-R)
+ FLUX-Text: A Simple and Advanced Diffusion Transformer Baseline for Scene Text Editing (**2025 arxiv**) [paper](https://arxiv.org/abs/2505.03329) [code](https://amap-ml.github.io/FLUX-text/)

### Scene Text Generation
+ Synthetic Data and Artificial Neural Networks for Natural Scene Text Recognition (**2014 arxiv**) [paper](https://arxiv.org/pdf/1406.2227.pdf)
+ Synthetic data for text localisation in natural images (**2016 CVPR**) [paper](https://openaccess.thecvf.com/content_cvpr_2016/papers/Gupta_Synthetic_Data_for_CVPR_2016_paper.pdf) [paper](https://openaccess.thecvf.com/content_cvpr_2016/papers/Gupta_Synthetic_Data_for_CVPR_2016_paper.pdf) [code](https://github.com/ankush-me/SynthText)
+ Text detection in traffic informatory signs using synthetic data (**2017 ICDAR**) [paper](https://ieeexplore.ieee.org/abstract/document/8270075)
+ Verisimilar image synthesis for accurate detection and recognition of texts in scenes (**2018 ECCV**) [paper](https://openaccess.thecvf.com/content_ECCV_2018/papers/Fangneng_Zhan_Verisimilar_Image_Synthesis_ECCV_2018_paper.pdf)  [code](https://github.com/GodOfSmallThings/Verisimilar-Image-Synthesis-for-Accurate-Detection-and-Recognition-of-Texts-in-Scenes)
+ Spatial Fusion GAN for Image Synthesis (**2019 CVPR**) [paper](https://openaccess.thecvf.com/content_CVPR_2019/papers/Zhan_Spatial_Fusion_GAN_for_Image_Synthesis_CVPR_2019_paper.pdf)
+ Learning to draw text in natural images with conditional adversarial networks (**2019 IJCAI**) [paper](https://www.ijcai.org/Proceedings/2019/0101.pdf)
+ ScrabbleGAN: Semi-Supervised Varying Length Handwritten Text Generation (**2020 CVPR**) [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Fogel_ScrabbleGAN_Semi-Supervised_Varying_Length_Handwritten_Text_Generation_CVPR_2020_paper.pdf)
+ SynthText3D: synthesizing scene text images from 3D virtual worlds (**2020 Science China Information Sciences**) [paper](https://link.springer.com/article/10.1007/s11432-019-2737-0)
+ UnrealText: Synthesizing Realistic Scene Text Images from the Unreal World (***2020 arxiv***) [paper](https://arxiv.org/pdf/2003.10608.pdf) [code](https://github.com/Jyouhou/UnrealText/)
+ Synthtiger: Synthetic text image generator towards better text recognition models (**2021 ICDAR**) [paper](https://link.springer.com/chapter/10.1007/978-3-030-86337-1_8) [code](https://github.com/clovaai/synthtiger)
+ Vector Quantized Diffusion Model for Text-to-Image Synthesis (**2022 CVPR**) [paper](https://openaccess.thecvf.com/content/CVPR2022/papers/Gu_Vector_Quantized_Diffusion_Model_for_Text-to-Image_Synthesis_CVPR_2022_paper.pdf)
+ Photorealistic text-to-image diffusion models with deep language understanding (**2022 NIPS**) [paper](https://proceedings.neurips.cc/paper_files/paper/2022/file/ec795aeadae0b7d230fa35cbaf04c041-Paper-Conference.pdf)
+ eDiff-I: Text-to-Image Diffusion Models with an Ensemble of Expert Denoisers (**2022 arxiv**) [paper](https://arxiv.org/pdf/2211.01324.pdf) [code](https://deepimagination.cc/eDiff-I/)
+ Character-Aware Models Improve Visual Text Rendering (**2023 ACL**) [paper](https://arxiv.org/pdf/2212.10562.pdf)
+ Deepfloyd (**2023**) [code](https://github.com/deep-floyd/if)
+ GlyphDraw: Seamlessly Rendering Text with Intricate Spatial Structures in Text-to-Image Generation (**2023 arxiv**) [paper](https://arxiv.org/pdf/2303.17870.pdf) [code](https://1073521013.github.io/glyph-draw.github.io/)
+ TextDiffuser: Diffusion Models as Text Painters (**2023 NIPS**) [paper](https://arxiv.org/pdf/2305.10855.pdf) [code](https://aka.ms/textdiffuser)
+ Glyphcontrol: Glyph conditional control for visual text generation (**2023 NIPS**) [paper](https://arxiv.org/pdf/2305.10855.pdf) [code](https://aka.ms/textdiffuser)
+ AnyText: Multilingual Visual Text Generation And Editing (**2024 ICLR**) [paper](https://arxiv.org/pdf/2311.03054) [code](https://github.com/tyxsspa/AnyText)
+ How Control Information Influences Multilingual Text Image Generation and Editing? (**2024 NIPS**) [paper](https://arxiv.org/pdf/2407.11502) [code](https://github.com/CyrilSterling/TextGen)
+ First Creating Backgrounds Then Rendering Texts: A New Paradigm for Visual Text Blending (**2024 ECAI**) [paper](https://arxiv.org/pdf/2410.10168)
+ Glyph-ByT5: A Customized Text Encoder for Accurate Visual Text Rendering (**2024 ECCV**) [paper](https://arxiv.org/pdf/2403.09622) [code](https://github.com/AIGText/Glyph-ByT5)
+ TextDiffuser-2: Unleashing the Power of Language Models for Text Rendering (**2024 ECCV**) [paper](https://arxiv.org/pdf/2311.16465) [code](https://github.com/microsoft/unilm/tree/master/textdiffuser-2)
+ AnyText2: Visual Text Generation and Editing With Customizable Attributes (**2024 arxiv**) [paper](https://arxiv.org/pdf/2411.15245) [code](https://github.com/tyxsspa/AnyText2)
+ Type-R: Automatically Retouching Typos for Text-to-Image Generation (**2024 arxiv**) [paper](https://arxiv.org/pdf/2411.18159)
+ Geometric-Aware Control in Diffusion Model for Handwritten Chinese Font Generation (**2024 ICDAR**) [paper](https://link.springer.com/chapter/10.1007/978-3-031-70536-6_1)
+ DiffusionPen: Towards Controlling the Style of Handwritten Text Generation (**2024 ECCV**) [paper](https://arxiv.org/pdf/2409.06065.pdf) [code](https://github.com/koninik/DiffusionPen)
+ Visual Text Generation in the Wild (**2024 ECCV**) [paper](https://arxiv.org/pdf/2407.14138.pdf) [code](https://github.com/AlibabaResearch/AdvancedLiterateMachinery/tree/main/OCR/SceneVTG)
+ One-Shot Diffusion Mimicker for Handwritten Text Generation (**2024 ECCV**) [paper](https://arxiv.org/pdf/2409.04004.pdf) [code](https://github.com/dailenson/One-DM)
+ Beyond Flat Text: Dual Self-inherited Guidance for Visual Text Generation (**2025 arxiv**) [paper](https://arxiv.org/pdf/2501.05892.pdf)
+ FonTS: Text Rendering with Typography and Style Controls (**2025 arxiv**) [paper](https://arxiv.org/pdf/2412.00136)
+ TextFlux: An OCR-Free DiT Model for High-Fidelity Multilingual Scene Text Synthesis (**2025 arxiv**) [paper](https://arxiv.org/pdf/2505.17778.pdf) [code](https://github.com/yyyyyxie/textflux)
+ Seedream 2.0: A Native Chinese-English Bilingual Image Generation Foundation Model (**2025 arxiv**) [paper](https://arxiv.org/pdf/2503.07703.pdf)
+ GlyphDraw2: Automatic Generation of Complex Glyph Posters with Diffusion Models and Large Language Models (**2025 AAAI**) [paper](https://arxiv.org/pdf/2407.02252.pdf) [code](https://github.com/OPPO-Mente-Lab/GlyphDraw2)
+ POSTA: A Go-to Framework for Customized Artistic Poster Generation (**2025 CVPR**) [paper](https://arxiv.org/pdf/2503.14908.pdf) [code](https://haoyuchen.com/POSTA)
+ PosterMaker: Towards High-Quality Product Poster Generation with Accurate Text Rendering (**2025 CVPR**) [paper](https://arxiv.org/pdf/2504.06632.pdf) [code](https://poster-maker.github.io)
+ BizGen: Advancing Article-level Visual Text Rendering for Infographics Generation (**2025 CVPR**) [paper](https://arxiv.org/pdf/2503.20672.pdf) [code](https://github.com/1230young/bizgen)
+ TextCrafter: Accurately Rendering Multiple Texts in Complex Visual Scenes (**2025 arxiv**) [paper](https://arxiv.org/pdf/2503.23461.pdf) [code](https://github.com/NJU-PCALab/TextCrafter)
+ Glyph-ByT5-v2: A Strong Aesthetic Baseline for Accurate Multilingual Visual Text Rendering (**2024 arxiv**) [paper](https://arxiv.org/pdf/2406.10208.pdf) [code](https://glyph-byt5-v2.github.io/)
+ AMO Sampler: Enhancing Text Rendering with Overshooting (**2025 CVPR**) [paper](https://arxiv.org/pdf/2411.19415.pdf) [code](https://github.com/hxixixh/amo-release)


### Cite
If you are interested in it, please star our project! And cite our paper as follows:
```
@article{shu2025visual,
  title={Visual Text Processing: A Comprehensive Review and Unified Evaluation},
  author={Shu, Yan and Zeng, Weichao and Zhao, Fangmin and Chen, Zeyu and Li, Zhenhang and Yang, Xiaomeng and Zhou, Yu and Rota, Paolo and Bai, Xiang and Jin, Lianwen and Yin Xu-Cheng and Sebe, Nicu},
  journal={arXiv preprint arXiv:2504.21682},
  year={2025}
}
```


