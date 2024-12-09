# 手动注入UE4SS
如果安装正确的情况下，UE4SS并没有伴随游戏启动，请检查UE4SS安装目录中是否有UE4SS.log文件。如果没有，则UE4SS没能自动注入游戏进程中。  
这种情况似乎会发生在Windows10以下的系统中。此时需要手动注入DLL。

## 准备DLL注入器
这里我推荐使用 `Detours` 的 `setdll.exe` 注入DLL，由于`Detours`是微软官方维护的项目，所以不会被识别为病毒。同时`setdll.exe`会将DLL注入到游戏的可执行文件中，在启动时随游戏自动运行，不需要每次都手动注入。
如果你信得过我，就在 Releases 中下载我编译好的 `setdll.exe` ，也可以克隆 [detours](https://github.com/microsoft/detours) 的代码自行编译。

## 使用指令注入DLL
Windows10及以上，按 `徽标 + X` ，在弹出的菜单中打开命令提示符或者Power Shell。  
Windows7及以下，打开开始菜单，选择 `运行` ，输入 `CMD` 打开命令提示符。  
在命令提示符中输入以下指令：  
```
"\(setdll.exe 文件的位置\)/setdll.exe" d:"\(游戏目录\)/RTypeFinal2/Binaries/Win64/UE4SS.dll" "\(游戏目录\)/RTypeFinal2/Binaries/Win64/RTypeFinal2-Win64-Shipping.exe"
```
- 请将上方的 `\(setdll.exe 文件的位置\)` 和 `\(游戏目录\)` 换成你电脑上对应的目录。
如果成功， `RTypeFinal2-Win64-Shipping.exe` 将被更新，同时生成一个叫 `RTypeFinal2-Win64-Shipping.exe~` 的备份文件。