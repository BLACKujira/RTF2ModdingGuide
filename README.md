[简体中文](README.zhs.md) | [日本語](README.ja.md)

# R-Type Final 2 Mod Installation and Development Guide

## Chapter 1.0: Basics of R-Type Final 2 Modding
In this chapter, you will learn how to install *UE4SS* and various types of mods for *R-Type Final 2*. Whether you are a mod developer or a mod player, this chapter is essential.

The content in this chapter is consistent with general *Unreal Engine 4* and *Unreal Engine 5* modding tutorials but includes specific details for *R-Type Final 2*.

- [Install UE4SS](Chapter1_TheBasics/en/InstallingUE4SS.md)
- [Manually Inject UE4SS](Chapter1_TheBasics/en/ManuallyInjectingUE4SS.md)
- [Install Blueprint Mods](Chapter1_TheBasics/en/InstallingBlueprintMods.md)
- [Install PAK Mods](Chapter1_TheBasics/en/InstallingPAKMods.md)
- [Install LUA Mods](Chapter1_TheBasics/en/InstallingLUAMods.md)
- [Enter Mod Stages](Chapter1_TheBasics/en/EnterModLevels.md)
- [Backup Save Files](Chapter1_TheBasics/en/BackupSaveFiles.md)

## Chapter 2.0: Unpacking R-Type Final 2

Generally, unpacking the game is the first step in mod development. For most *UE4/5* games, [FModel](https://github.com/iAmAsval/FModel/) is the best tool for previewing and extracting game assets, and *R-Type Final 2* is no exception. However, due to the way the game was packaged during development, an *AES key* and *`.usmap` mapping files* are required for extraction.

- [Obtaining AES Key and .usmap Mapping Files](Chapter2_0_Unpack/en/GettingAESKeyAndUsmap.md)
- [Using FModel to View and Extract Game Assets](Chapter2_0_Unpack/en/UsingFModelToExtractAssets.md)

## Chapter 2.1: R-Type Final 2 Project Structure

This chapter provides a basic overview of the internal structure of the game, which is one of the foundations for mod development.

- [Understanding Resource File Directories](Chapter2_1_ProjectStructure/en/ResourceFileDirectory.md)
- [Prefixes of Resource Files](Chapter2_1_ProjectStructure/en/ResourceFilePrefixes.md)
- [Important Enumerations](Chapter2_1_ProjectStructure/en/ImportantEnumerations.md)
- [Important Data Tables](Chapter2_1_ProjectStructure/en/ImportantDataTables.md)
- [Important Runtime Objects](Chapter2_1_ProjectStructure/en/ImportantRuntimeObjects.md)

## Chapter 2.2: Quick Reference

This chapter lists some data tables, enumerations, and their related information to help developers quickly locate relevant IDs.

Due to the large number of enemies, this section won’t list all of them in detail, but it introduces a method for locating enemy IDs.

- [Locating Enemy IDs via Images in BydoLab](Chapter2_2_QuickReference/en/FindEnemyIDBydoLabImage.md)
- [Stage List](Chapter2_2_QuickReference/en/StageList.md)
- [R-Craft List](Chapter2_2_QuickReference/en/RCraftList.md)
- Force List

## Chapter 3.0: General Knowledge for Mod Development

Starting from this chapter, I will not cover every step in detail as I did in earlier chapters, nor will I repeat content that has already been covered by others. Some tutorials may refer to the [Tool List], so please check that for the required tools and relevant learning resources.

- [Tool List](Chapter3_0_DeveBasics/en/ToolList.md)
- [Articles and Communities](Chapter3_0_DeveBasics/en/ArticlesAndCommunities.md)
- [In-Game Console Commands](Chapter3_0_DeveBasics/en/InGameConsoleCommands.md)

## Chapter 4.0: Blueprint Mods

This is a popular type of mod that takes full advantage of Unreal Engine's Blueprint system. With the help of a mod loader, it's possible to spawn *custom logic-based Actors* into each level during load.

If you're a beginner, you can start by following [this classic tutorial](https://docs.ue4ss.com/dev/feature-overview/blueprint-modloader.html) to create a simple Blueprint mod that shows a “mod loaded” message — and then build more complex features on top of that.

- Basic Blueprint Mod Development Workflow
- [UE4 Version Selection: 4.26.2 vs 4.26 Chaos](Chapter4_0_BPMod/en/UE4VersionSelection.md)
- [Fixing Animation Blueprint Update Event Crashes](Chapter4_0_BPMod/en/FixABPUpdateCrash.md)
- [Fixing Custom Materials Not Displaying or Crashing](Chapter4_0_BPMod/en/FixCustomMaterialIssues.md)
- Fixing Compilation Errors Due to Memory Limits
- [Analyzing Blueprints Using Kismet Analyzer](Chapter4_0_BPMod/en/KismetAnalyzer.md)
- [Using Delegates as Function Parameters](Chapter4_0_BPMod/en/UsingDelegatesAsFuncParam.md)


## Chapter 4.1: PAK Mods
*PAK Mods* are a superset of Blueprint Mods. They typically do not extend the game system's functionality. There are two types: 
1. PAK Mods that do not require baking, created using *UAssetGUI* and *UnrealPak*, often for data modification.
2. PAK Mods that require baking, created using *Unreal Engine*, typically for replacing music or textures.

- Example: Replacing Background Music (requires baking)
- Example: Modifying Weapon Data (does not require baking)

## Chapter 5.0: Stage Mods
This chapter introduces general knowledge about *Stage Mods*. For specific details on each *Stage Mod Template*, refer to their respective documentation.

- Stage Loading Logic
- Structure of a Stage
- Stage Initialization Logic
- CountAsset (Scroll Event)

## Chapter 5.1: Enemy Information
This chapter introduces technical information about the game's original enemies, which will help stage mod developers generate them within their stages.

- [E000_PowArmor](Chapter5_1_EnemyData/en/E000_PowArmor.md)

## Extra Chapter: Unpacking R-Type Tactics II

Since the remastered version *R-Type Tactics I & II Cosmos* is about to be released, there may soon be easier ways to extract higher-quality assets. Therefore, the content in this chapter might become less relevant.

- [Unpacking the Main Resource File](EX_UnpackRTT2/en/UnpackingMainResourceFile.md)
- [Analysis of Resource Packing Format](EX_UnpackRTT2/en/ResourcePackingAnalysis.md)
- [Generating Normal Maps with Photoshop](EX_UnpackRTT2/en/GeneratingNormalMapsWithPhotoshop.md)
- [Exporting Textures Using PPSSPP](EX_UnpackRTT2/en/ExportingTexturesWithPPSSPP.md)

## Extra Chapter: Researching Issues
This chapter is still under research, and following these guidelines may not necessarily yield the desired results. The research directions and the solvability of the problems are still unknown.

The purpose of this chapter is to facilitate the sharing of information among those researching these issues and collaborate to solve them.

- [Create Mirror Game Project](EX_UnderInvestigation/en/CreatingMirrorGameProject.md)
