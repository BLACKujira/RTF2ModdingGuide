# Tool List

This article lists the tools that are needed during the *R-Type Final 2* Mod development process.

These are only a part of the *UE4/5* Mod development ecosystem. You can refer to [UE-Modding-Tools](https://github.com/Buckminsterfullerene02/UE-Modding-Tools) for more information on tools that might be used in *UE4/5* Mod development.

Many of these tools are hard to find information about through regular search engines. It is highly recommended to join the [Unreal Engine Modding Discord](https://discord.gg/VYjh4vSq) to learn more details.

## Essential Tools for Mod Development

### ![Tool_UE4SS](../image/Tool_UE4SS.png) (Important) UE4SS

The core technology used in this tutorial, fundamental and crucial, is used in almost all tutorials.

---

It integrates important functions such as exporting *`.usmap`* mapping files, exporting *UHT header files*, and exporting Actor information from maps.

### ![Tool_UE](../image/Tool_UE.png) (Important) Unreal Engine 4.26

This is the engine used by *R-Type Final 2*, and it is required for developing *Blueprint Mods* and *PAK Mods that require baking*. The recommended version is `4.26.2`.

---

### ![Tool_VS](../image/Tool_VS.png) ![Tool_Cplus](../image/Tool_Cplus.png) (Important) Visual Studio 2019 & C++ Development Environment

To use Unreal Header Tool (UHT) files, you need to have a *C++* development environment for *Unreal Engine 4.26*. This requires installing *Visual Studio 2019* with *C++* development support.

Due to the limitations of *Unreal Engine 4.26*, *Visual Studio 2022* is not recognized, but you can still easily install *Visual Studio 2019* from a backup installation program discovered from [a Reddit post](https://www.reddit.com/r/VisualStudio/comments/171cncs/how_to_download_an_old_released_version_of_visual/?rdt=62270) using the *Wayback Machine*.

(It seems you can also modify configuration files or code to make *Unreal Engine 4.26* support *Visual Studio 2022*.)

---

### ![AESKeyFinder](../image/Tool_AESKeyFinder.png) (Important) AES Key Finder

Used to automatically discover the AES key of the game. A correct key is required to unpack game resources.

In *R-Type Final 2* version `2.0.3`, four potential keys are discovered, and only one is correct.

---

### ![Tool_FModel](../image/Tool_FModel.png) (Important) FModel

Currently the most popular *PAK unpacker*. In addition to basic unpacking functionality, it can preview models, textures, and some music. Most importantly, it can convert *.uasset* files into *JSON*, which can be easily read to see their properties.

You will need an *AES key* and a *.usmap* mapping file to use it. The AES key can be obtained using *AES Key Finder*, and the *.usmap* file can be exported using *UE4SS* or *dumper-7*.

In terms of model and animation extraction, it seems inferior to *UModel*.

---

### ![UAssetGUI](../image/Tool_UAssetGUI.png) (Important) UAssetGUI

A specialized software for editing *.uasset* files, often used in conjunction with *FModel* and *UnrealPak*. It can be used to modify in-game values and add new rows to data tables. It is an essential tool for creating *PAK Mods that don’t require baking* and *Level Mods*.

After adding new rows to data tables, you need to save and reload the file before you can edit the row content.

---

### ![Tool_UnrealPak](../image/Tool_UnrealPak.png) (Important) UnrealPak

Used to repackage folders and resource files into `.pak` files. It is often used in combination with *FModel* and *UAssetGUI*. It is also an essential tool for creating *PAK Mods that don’t require baking*.

Typically, `UnrealPak-With-Compression.bat` is used for packing. The impact of using `UnrealPak-Without-Compression.bat` is still uncertain.

---

### ![KismetAnalyzer](../image/Tool_KismetAnalyzer.png) Kismet Analyzer

A tool used to analyze *.uasset* files and *.umap* files containing blueprint logic, converting the blueprint logic into a flowchart. By referencing the flowchart, the blueprint logic can be restored in Unreal Engine.

It needs to be used with *FModel* to get detailed properties such as parameters, variables, and functions.

## Decompilation, Hooking C++ Code

This section comes from my earlier failed attempts. In the current Mod development process, these tools are rarely needed.

### dumper-7

It can convert *UFunction* into callable and hookable C++ functions and generate an SDK for the project. Other functions are similar to *UE4SS*, such as exporting *.usmap* mapping files. It is important because it can export symbol sets for use with IDA.

In most cases, *UE4SS* can be used as a substitute, and it is rarely used. The generated SDK is often used in conjunction with *DLL injection libraries* (such as Detours).

Note: Hooks in asynchronous threads (e.g., the game save thread) will not be triggered.

---

### IDA

Disassembler & Debugger, used to uncover the game’s runtime logic from the game’s DLL files. Due to the symbol set only covering a small portion, the discovery process can be very difficult.

To use with the symbol set exported by *dumper-7*, make sure the version is higher than `8.3`, or the plugin will not work.

---

### X64DBG

Debugger, used to view the game’s memory and assembly, to check whether the hook has hooked the function. It can also show some output information when the game crashes.

Compared to IDA’s debugging functionality, it is much faster, but it cannot load the symbol set.
