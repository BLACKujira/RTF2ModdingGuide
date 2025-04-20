# R-Type Final 2 Mod安装与开发教程

## Chapter 1.0 ：R-Type Final 2 Modding 基础

在这一章中，你将学会如何为 *R-Type Final 2* 安装 *UE4SS* 和不同类型的Mod。无论你是Mod开发者还是Mod玩家，都需要学习这一章的内容。

本章节的内容与通用的 *虚幻引擎4*、*虚幻引擎5* 游戏Modding教程没有区别，但针对 *R-Type Final 2* 做了更具体的说明。

- [安装UE4SS](Chapter1_TheBasics/zhs/安装UE4SS.md)
- [手动注入UE4SS](Chapter1_TheBasics/zhs/手动注入UE4SS.md)
- [安装蓝图Mod](Chapter1_TheBasics/zhs/安装蓝图Mod.md)
- [安装PAK Mod](Chapter1_TheBasics/zhs/安装PAKMod.md)
- [安装LUA Mod](Chapter1_TheBasics/zhs/安装LUAMod.md)
- [进入Mod关卡](Chapter1_TheBasics/zhs/进入Mod关卡.md)

## Chapter 2.0：解包 R-Type Final 2

通常来说，解包游戏是Mod开发的第一步。对于大多数 *UE4/5* 游戏， [FModel](https://github.com/iAmAsval/FModel/) 是最佳的资源预览/解包工具，*R-Type Final 2* 也不例外。不过由于游戏开发时的一些设置，需要提供 *AES密钥* 和 *`.usmap`映射文件* 才能解包。

- [获取AES密钥和.usmap映射文件](Chapter2_0_Unpack/zhs/获取AES密钥和usmap映射文件.md)
- [使用FModel查看和解包游戏资源](Chapter2_0_Unpack/zhs/使用FModel查看和解包游戏资源.md)

## Chapter 2.1：R-Type Final 2 的项目构成

这是Mod开发的基础之一，粗略地介绍了一下游戏内部的构成。

- [认识资源文件目录](Chapter2_1_ProjectStructure/zhs/认识资源文件目录.md)
- [资源文件的前缀](Chapter2_1_ProjectStructure/zhs/资源文件的前缀.md)
- [重要的枚举](Chapter2_1_ProjectStructure/zhs/重要的枚举.md)
- [重要的数据表](Chapter2_1_ProjectStructure/zhs/重要的数据表.md)
- [重要的运行时对象](Chapter2_1_ProjectStructure/zhs/重要的运行时对象.md)

## Chapter 2.2：速查表

这一章列举了一些数据表、枚举及其关联的内容，方便开发者快速查询所需内容的ID。

由于敌人的数量太多，暂不详细列举，但这一章会介绍一种寻找敌人ID的方法。

- [通过BydoLab中敌人的图片定位敌人ID](Chapter2_2_QuickReference/zhs/通过BydoLab中敌人的图片定位敌人ID.md)
- [关卡列表](Chapter2_2_QuickReference/zhs/关卡列表.md)
- [R战机列表](Chapter2_2_QuickReference/zhs/R战机列表.md)
- Force列表

## Chapter 3.0：Mod开发的通用知识

从这一章开始，我不会像之前那样详细地介绍每个步骤，也不打算重复说明别人已经介绍过的内容。一些教程会有指向 [工具列表] 的引用，请参照列表中的内容下载需要的工具和学习需要的技能。

- [工具列表](Chapter3_0_DeveBasics/zhs/工具列表.md)
- [文章和社区](Chapter3_0_DeveBasics/zhs/文章和社区.md)
- [游戏内控制台指令](Chapter3_0_DeveBasics/zhs/游戏内控制台指令.md)

## Chapter 4.0：蓝图Mod

这是一种流行的、充分利用虚幻引擎的Mod，借助Mod加载器，可以在每一个关卡加载时将 *含有自定义逻辑的Actor* 生成到关卡中。

如果你是新手，可以参考 [这个经典的教程](https://docs.ue4ss.com/dev/feature-overview/blueprint-modloader.html) 学习 *蓝图Mod* 的开发方式，创建一个简单的显示 `模组已加载` 的 *蓝图Mod*，在此基础上再增加更复杂的内容。
 
- 开发蓝图Mod的基本流程
- [版本选择：4.26.2 还是 4.26 Chaos](Chapter4_0_BPMod/zhs/UE4版本选择.md)
- [解决动画蓝图更新事件导致的崩溃](Chapter4_0_BPMod/zhs/解决动画蓝图更新事件导致的崩溃.md)
- [解决自定义材质无法显示或崩溃的问题](Chapter4_0_BPMod/zhs/解决自定义材质无法显示或崩溃的问题.md)
- 解决内存不足导致的编译问题
- [使用kismet-analyzer分析蓝图](Chapter4_0_BPMod/zhs/使用KismetAnalyzer分析蓝图.md)
- [将委托作为函数的参数](Chapter4_0_BPMod/zhs/将委托作为函数的参数.md)

## Chapter 4.1：PAK Mod

*PAK Mod* 是蓝图Mod的一个超集，它通常不具备扩展游戏系统的功能。其中有两种类型，使用 *UAssetGUI* + *UnrealPak* 制作不需要烘焙的 *PAK Mod* ,这种通常用于修改数据。或者使用 *虚幻引擎* 制作需要烘焙的 *PAK Mod*，这种通常用于替换音乐或贴图。

- 示例：替换背景音乐（需要烘焙）
- 示例：修改武器数据（不需要烘焙）

## Chapter 5.0：关卡Mod

这一章介绍的是 *关卡Mod* 的通用知识，关于每个 *关卡Mod模板* 的细节请参考各自的文档。制作 *关卡Mod* 同样需要制作 *蓝图Mod* 和 *PAK Mod* 的知识。

- 关卡加载逻辑
- 关卡的构成
- 关卡初始化逻辑
- CountAsset（卷轴事件）

## Chapter 5.1：敌人信息

这一章主要介绍游戏原版敌人的一些技术信息，方便关卡Mod的开发者在关卡中生成它们。

- [E000_PowArmor](Chapter5_1_EnemyData/zhs/E000_PowArmor.md)

## 特殊章节：解包 R-Type Tactics II

由于复刻版 *R-Type Tactics I & II Cosmos* 不久后就要发售了，到时候可能有更简便的方式解包出更精细的内容。所以这章的内容也许没有太大价值。

- [解包主资源文件](EX_UnpackRTT2/zhs/解包主资源文件.md)
- [资源打包方式分析](EX_UnpackRTT2/zhs/资源打包方式分析.md)
- [使用Photoshop生成法线贴图](EX_UnpackRTT2/zhs/使用Photoshop生成法线贴图.md)
- [使用PPSSPP导出纹理](EX_UnpackRTT2/zhs/使用PPSSPP导出纹理.md)

## 特殊章节：研究中的问题

这一章的内容尚未研究完成，即便按照这些指南操作也不一定能达到想要的效果。因为这些指南的研究路线是否正确、研究的问题是否可以被解决都是未知的。

这一章是为了方便同样在研究这些问题的人共享已经获得的信息，并共同协作解决这些问题。

- [创建镜像游戏项目](EX_UnderInvestigation/zhs/创建镜像游戏项目.md)