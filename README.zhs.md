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

## Chapter 2.0：R-Type Final 2 的项目构成

这是Mod开发的基础之一，但没有涉及到太多技术内容，即便作为非开发者也可以作为兴趣阅读。

- [认识资源文件目录](Chapter2_0_ProjectStructure/zhs/认识资源文件目录.md)
- [资源文件的前缀](Chapter2_0_ProjectStructure/zhs/资源文件的前缀.md)
- 重要的枚举
- 重要的数据表
- 重要的运行时对象
- 使用UE4SS操控运行时对象

## Chapter 2.1：速查表

这一章列举了一些数据表、枚举及其关联的内容，方便开发者快速查询所需内容的ID。

由于敌人的数量太多，暂不详细列举，但这一章会介绍一种寻找敌人ID的方法。

- 通过BydoLab中敌人的图片定位敌人ID
- 关卡列表
- R战机列表
- Force列表

## Chapter 3.0：Mod开发的通用知识

从这一章开始，我不会像第一章那样详细地介绍每个步骤，也不打算重复说明别人已经介绍过的内容。在一些教程的开头会有指向 [工具列表] 和 [技能列表] 的引用，请参照列表中的内容下载需要的工具和学习需要的技能。

- 工具列表
- 技能列表
- [控制台指令](Chapter3_0_DeveBasics/zhs/控制台指令.md)

## Chapter 4.0：蓝图Mod

这是一种流行的、充分利用虚幻引擎的Mod，借助Mod加载器，可以在每一个关卡加载时将 *含有自定义逻辑的Actor* 生成到关卡中。

请参考 [这个经典的教程](https://docs.ue4ss.com/dev/feature-overview/blueprint-modloader.html) 学习 *蓝图Mod* 的基础。
 
- [版本选择：4.26.2 还是 4.26 Chaos](Chapter4_BPMod/zhs/UE4版本选择.md)
- 解决动画蓝图更新事件导致的崩溃
- 解决自定义材质无法显示或崩溃的问题
- 解决内存不足导致的编译问题
- [使用kismet-analyzer分析蓝图](Chapter4_BPMod/zhs/使用kismet-analyzer分析蓝图.md)
- [将委托作为函数的参数](Chapter4_BPMod/zhs/将委托作为函数的参数.md)

## Chapter 4.1：PAK Mod

*PAK Mod* 是蓝图Mod的一个超集，它通常不具备扩展游戏系统的功能。其中有两种类型，使用 *UAssetGUI* + *UnrealPak* 制作不需要烘焙的 *PAK Mod* ,这种通常用于修改数据。或者使用 *虚幻引擎* 制作需要烘焙的 *PAK Mod*，这种通常用于替换音乐或贴图。

- 示例：替换背景音乐（需要烘焙）
- 示例：修改武器数据（不需要烘焙）

## Chapter 5.0：关卡Mod

这一章介绍的是 *关卡Mod* 的通用知识，关于每个 *关卡Mod模板* 的细节请参考各自的文档。

- 关卡加载逻辑
- 关卡的构成
- 关卡初始化逻辑
- CountAsset（卷轴事件）

# Chapter 5.1：敌人信息

这一章主要介绍游戏原版敌人的一些技术信息，方便关卡Mod的开发者在关卡中生成它们。

- [E000_E1940_PowArmor](Chapter5_1_EnemyData/zhs/E000_E1940_PowArmor.md)

## 特殊章节：研究中的问题

这一章的内容尚未研究完成，即便按照这些指南操作也不一定能达到想要的效果。因为这些指南的研究路线是否正确、研究的问题是否可以被解决都是未知的。

这一章存在的意义是，方便同样在研究这些问题的人共享已经获得的信息，并共同协作解决这些问题。

- [创建镜像游戏项目](/UnderInvestigation/zhs/创建镜像游戏项目.md)