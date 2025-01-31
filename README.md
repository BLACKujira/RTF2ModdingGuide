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

## Chapter 2.0: R-Type Final 2 Project Structure
This chapter covers the basics of mod development and is accessible even to non-developers who are interested in learning about the structure.

- [Understanding Resource File Directories](Chapter2_0_ProjectStructure/en/ResourceFileDirectory.md)
- [Prefixes of Resource Files](Chapter2_0_ProjectStructure/en/ResourceFilePrefixes.md)
- Important Enumerations
- Important Data Tables
- Important Runtime Objects
- Using UE4SS to Manipulate Runtime Objects

## Chapter 2.1: Quick Reference
This chapter lists some data tables, enumerations, and their related content, making it easy for developers to quickly locate the necessary ID.

While there are too many enemies to list in detail, this chapter will introduce a method to locate enemy IDs.

- Locate Enemy IDs via Images in BydoLab
- Stage List
- R-Craft List
- Force List

## Chapter 3.0: General Knowledge for Mod Development
Starting from this chapter, I will not cover every step in detail as I did in Chapter 1, nor will I repeat content that has already been covered by others. Some tutorials will reference [Tool List] and [Skill List], so please refer to them for the necessary tools and skills.

- Tool List
- Skill List
- [In-Game Console Commands](Chapter3_0_DeveBasics/en/InGameConsoleCommands.md)

## Chapter 4.0: Blueprint Mods
Blueprint Mods are a popular modding method that fully utilizes Unreal Engine. With the mod loader, you can generate *custom logic Actors* for each level.

Refer to [this classic tutorial](https://docs.ue4ss.com/dev/feature-overview/blueprint-modloader.html) to learn the basics of *Blueprint Mods*.

- [Choosing UE4 Version: 4.26.2 or 4.26 Chaos](Chapter4_0_BPMod/en/UE4VersionSelection.md)
- Fix Animation Blueprint Update Event Crashes
- Fix Custom Materials Not Displaying or Crashing
- Fix Memory Issues during Compilation
- [Analyze Blueprints with Kismet Analyzer](Chapter4_0_BPMod/en/KismetAnalyzer.md)
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

- [E000_E1940_PowArmor](Chapter5_1_EnemyData/en/E000_E1940_PowArmor.md)

## Special Chapter: Researching Issues
This chapter is still under research, and following these guidelines may not necessarily yield the desired results. The research directions and the solvability of the problems are still unknown.

The purpose of this chapter is to facilitate the sharing of information among those researching these issues and collaborate to solve them.

- [Create Mirror Game Project](/UnderInvestigation/en/CreatingMirrorGameProject.md)
