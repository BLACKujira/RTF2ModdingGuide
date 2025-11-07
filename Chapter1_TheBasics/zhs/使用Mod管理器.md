# 使用Mod管理器

为了解决UE4SS和Mod安装步骤过于繁琐的问题，我制作了 [R-Type Final 2 Mod 管理器](https://github.com/BLACKujira/RTF2ModManager) 。这是一个用于简化 R-Type Final 2 Mod 安装流程的图形化管理工具，支持多语言切换、自动识别游戏目录、安装 UE4SS 以及一键管理常用 Mod。

## 下载Mod管理器

首先从 [RTF2ModManager 的 Releases](https://github.com/BLACKujira/RTF2ModManager/releases) 里下载 `RTF2ModManager.zip`。

![RTF2MM_Releases](../image/RTF2MM_Releases.png)

将压缩包中的所有内容解压到任意目录

运行解压目录中的 `RTF2ModManager.exe`

![RTF2MM_Folder](../image/RTF2MM_Folder.png)

> **请不要直接在压缩包内直接运行 `RTF2ModManager.exe` ，可能会导致找不到Mod文件而出错**

## 设置游戏目录

如果你使用的游戏平台为 *Steam* 且未修改默认安装路径（`\Program Files (x86)\Steam\steamapps\common\R-Type Final 2`），程序在运行时会自动定位到游戏目录。此时 `游戏目录设置` 这一栏会显示当前定位到的游戏目录。

![RTF2MM_AutoSearch](../image/RTF2MM_AutoSearch.png)

否则，如果 `游戏目录设置` 这一栏显示 `请选择游戏目录` ，请点击旁边的 `手动选择`

![RTF2MM_ManualSelect](../image/RTF2MM_ManualSelect.png)

在弹出的窗口中选择游戏安装目录，请选择 `RTypeFinal2.exe` 所在的文件夹，如下图所示，此文件夹中还有 `Engine` 、 `RTypeFinal2` 等文件夹。如果你购买了OST，这里还会有OST的文件夹。

![GameDir](../image/GameDir.png)

## 安装 UE4SS

`UE4SS 管理` 这一栏会显示当前 *UE4SS* 的安装状态，绝大多数Mod需要安装 *UE4SS* 才可以运行。点击这一栏的 `安装` 按钮即可安装 *UE4SS*（附带适用于 `v2.0.4` 的 *AOB脚本*）。

![alt text](../image/RTF2MM_UE4SSInstall.png)

首次安装 *UE4SS* 后，请先 **启动一次游戏** 生成必要的文件和文件夹。如果安装成功，游戏启动时 *UE4SS控制台* 和一个命令行窗口会随着游戏窗口一起出现。并且返回Mod管理器时，`UE4SS 管理` 这一栏的提示中的 `未发现LogicMods文件夹，请在完成UE4SS的安装之后启动一次游戏，如依旧无效，请尝试手动注入` 也会消失，此时就可以安装Mod了。

### 使用静态注入

如果安装 *UE4SS* 后启动游戏并没有见到 *UE4SS控制台* 和命令行窗口中的任意一个，则说明在你的系统环境下，`UE4SS.dll` 不会自动注入游戏进程中。可能需要使用 `静态注入` 来强制解决这一问题。

![RTF2MM_UE4SSInject](../image/RTF2MM_UE4SSInject.png)

点击 `静态注入`，稍等片刻，完成后请尝试再次启动游戏，生成必要的文件和文件夹。

## 安装 Mod

在 `Mod 管理` 这一栏的左侧列表中会显示支持的Mod和安装状态，选择列表中的一项会在右侧显示详细信息。点击下方的 `安装` 按钮即可安装Mod。程序会自动安装Mod的各个模块，并处理所需的依赖。

![RTF2MM_ModInstall](../image/RTF2MM_ModInstall.png)

如果右侧的详细信息下方显示 `未安装UE4SS，无法安装含有非PAK模块的Mod` 或者 `未检测到 LogicMods 文件夹，无法安装含有蓝图模块的Mod` 。请确认 *UE4SS* 已成功安装并且至少启动了一次游戏。

> 此程序仅支持安装 [G-Type Origin](https://github.com/BLACKujira/GTypeOrigin)、[Simple Boss LifeBar](https://github.com/BLACKujira/SimpleBossLifeBarMod)、[RTF2 Debug Tools](https://github.com/BLACKujira/RTF2DebugToolsMod) 、[FPS Player](https://github.com/BLACKujira/FPSPlayerMod) 四个Mod，其它Mod依旧需要手动安装。

## 备份存档

如果你希望在体验完Mod内容后将存档恢复到原来的状态，或是因为担心某种原因导致的存档损坏，可以选择先备份游戏存档，在有需要的时候将存档替换回去。

在程序下方 `快捷功能` 这一栏中点击 `打开存档文件夹`，通常情况下能自动定位到存档文件夹并打开。

**复制**其中的文件（尤其是 `SLOT00.sav` ，这是游戏的主存档文件）到另一个文件夹即可。