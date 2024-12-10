# 手动注入UE4SS
如果安装正确的情况下，UE4SS并没有伴随游戏启动，请检查UE4SS安装目录中是否有 `UE4SS.log` 文件。如果没有，则UE4SS没能自动注入游戏进程中，此时需要手动注入DLL。

已知的这种情况发生在Windows7及以下的系统中，但没有证据表明其一定与系统有关。

## 准备DLL注入器
这里我推荐使用 `Detours` 的 `setdll.exe` 注入DLL，由于`Detours`是微软官方维护的项目，所以不会被识别为病毒。

同时`setdll.exe`会将DLL注入到游戏的可执行文件中，在启动时随游戏自动运行，不需要每次都手动注入。

如果你信得过我，就在 [Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) 中下载我编译好的 `setdll.exe` ，也可以克隆 [detours](https://github.com/microsoft/detours) 的代码自行编译，编译好的 `setdll.exe` 将出现在 `bin.X64` 文件夹中。

## 使用注入脚本
由于注入工具、DLL和目标文件都是固定的，所以我编写了一个批处理文件用来简化注入的操作。

1. 首先在 [Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) 中下载 `setdll.exe` 和 `ManuallyInjectUE4SS.bat` 这两个文件
2. 将 `setdll.exe` 和 `ManuallyInjectUE4SS.bat` 移动到 `RTypeFinal2\Binaries\Win64` 文件夹中，也就是 `RTypeFinal2-Win64-Shipping.exe` 和 `UE4SS.dll` 所在的文件夹。
3. 双击运行 `ManuallyInjectUE4SS.bat`，**命令提示符** 会打开，执行手动注入 `UE4SS.dll` 的指令

- 如果注入成功，**命令提示符** 中会输出一长串各种DLL的名字，之后输出 `Injection successful! Launching the game...` 并启动游戏，其他的输出均为注入失败。
- 如果输出 `Injection skipped to avoid overwriting the backup file.`，代表脚本检测到了之前注入时留下的备份文件，请勿重复注入。

## 备用方案：使用指令注入DLL
当注入脚本失效时，可以尝试使用这个方案进行注入。

**Windows10** 及以上，按 `徽标 + X` ，在弹出的菜单中打开 **命令提示符** 或者 **Power Shell**。  

**Windows7** 及以下，打开开始菜单，选择 **运行** ，输入 `CMD` 打开 **命令提示符** 。  

在 **命令提示符** 或 **Power Shell** 中输入以下指令：  
```
"(setdll.exe 文件的位置)/setdll.exe" d:"(游戏目录)/RTypeFinal2/Binaries/Win64/UE4SS.dll" "(游戏目录)/RTypeFinal2/Binaries/Win64/RTypeFinal2-Win64-Shipping.exe"
```
- 请将上方的 `(setdll.exe 文件的位置)` 和 `(游戏目录)` 换成你电脑上对应的目录。
- 不要删除指令中的双引号，如果你不知道这是做什么用的。

按下回车，如果注入成功， `RTypeFinal2-Win64-Shipping.exe` 将被更新，同时生成一个叫 `RTypeFinal2-Win64-Shipping.exe~` 的备份文件。

如果出现缺少权限的提示，请以管理员身份运行 **命令提示符** 或者 **Power Shell**。

**注意：不要重复注入**，否则备份文件 `RTypeFinal2-Win64-Shipping.exe~` 会被已经注入的文件覆盖。

## 验证安装
启动游戏，如果UE4SS的控制台窗口随游戏一起运行，则手动注入成功。

如果想取消UE4SS的注入，使用备份文件 `RTypeFinal2-Win64-Shipping.exe~` 覆盖 `RTypeFinal2-Win64-Shipping.exe` 即可。