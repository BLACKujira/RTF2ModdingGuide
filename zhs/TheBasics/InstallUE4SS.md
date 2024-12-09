# 安装UE4SS
在开始为 R-Type Final 2 开发或使用 MOD 之前，安装 UE4SS 是必不可少的第一步。
`UE4SS (Unreal Engine 4 Scripting System)` 是一个强大的工具，其不仅提供了对两大主流Mod—— `LUA Mod` 和 `蓝图Mod` 的支持，还包括关卡内对象查看和编辑、映射文件和接头文件导出等重要功能，本教程的大部分内容都需要其作为基础。
在这个教程中，我们将学会如何安装开发者版本的 `UE4SS v3.0.0` ，并升级到 `v3.0.1`，最后验证安装是否成功并排除可能的问题。

# 下载UE4SS
首先进入 [UE4SS-RE/RE-UE4SS](https://github.com/UE4SS-RE/RE-UE4SS) ，点击页面右侧的Releases，下载 `zDEV-UE4SS_v3.0.1.zip` 。下滑页面，同样下载 `zDEV-UE4SS_v3.0.0.zip` 。注意，这两个版本都需要下载，因为必须要先安装v3.0.0才能升级到v3.0.1。

# 寻找安装目录
以Steam版为例，右击游戏图标，在弹出的菜单中选择 `管理` -> `浏览本地文件` ，即可打开游戏的安装目录。这里应该有一个名叫 `RTypeFinal2.exe` 的可执行文件和两个文件夹。
打开 `RTypeFinal2` **文件夹**，再打开其中的 `Binaries` 文件夹，最后打开其中的 `Win64` 文件夹。在这里，你应该能看到 `RTypeFinal2-Win64-Shipping.exe` 这个文件，与游戏有着一样的图标、孤零零的放在这里。这里就是UE4SS的安装目录。

# 安装 UE4SS v3.0.0
将 `zDEV-UE4SS_v3.0.0.zip` 中的内容全部解压至此，如果操作正确，文件夹的样子将如图所示。
此时启动游戏，如果安装成功，你将可以看到UE4SS的控制台伴随游戏一起启动了。如果没有，请检查之前的操作是否正确，如果操作正确，嗯...那就麻烦了，请参照最下面的教程解决这个问题。如果控制台为一片空白，也不需要担心，在升级为 `v3.0.1` 之后再解决这个问题。

# 安装 UE4SS v3.0.1
将 `zDEV-UE4SS_v3.0.1.zip` 的内容解压到同样的文件夹，覆盖所有相同名称的文件。这样就升级到 `UE4SS v3.0.1` 了。

# 解决控制台的显示问题
如果UE4SS的控制台为全黑或全白，请找到UE4SS安装目录中的 `UE4SS-settings.ini` 这个文件，右键编辑这个文件。在打开的文本编辑器中定位到 `GraphicsAPI = opengl` 这一行，并修改为 `GraphicsAPI = dx11`。

# 为什么要选择 v3.0.1 和开发者版本的 UE4SS
由于游戏的武器、机体、关卡资料都记录在数据表中，添加新的内容可能需要修改数据表。UE4SS预计将在未来的版本中加入在运行时修改数据表的功能，为了预备版本的升级，建议使用最新的v3.0.1进行Mod的开发。
此外，开发者版本默认情况下控制台是开启的，新手不需要修改配置文件即可直观的判断出UE4SS是否已经正常运行。同时控制台中输入的信息也可以用来判断Mod是否被正确安装。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。。

# 错误排查和手动注入
如果安装正确的情况下，UE4SS并没有伴随游戏启动，请检查UE4SS安装目录中是否有UE4SS.log文件。如果没有，则UE4SS没能自动注入游戏进程中。这种情况似乎会发生在Windows10以下的系统中。此时需要手动注入DLL。
这里我使用 `Detours` 的 `setdll.exe` 注入DLL，由于`Detours`是微软官方维护的项目，所以不会报毒。而`setdll.exe`会将DLL注入到游戏的可执行文件中，在启动时随游戏自动运行，不需要每次都手动注入。
如果你信得过我，就在 Releases 中下载我编译好的 `setdll.exe` ，也可以克隆 [detours](https://github.com/microsoft/detours) 的代码自行编译。
Windows10以上，按 `徽标 + X` 打开命令提示符，Windows10以下，通过 `运行` 输入 `CMD` 打开命令提示符。在命令提示符中输入以下指令
```
".../setdll.exe" d:".../RTypeFinal2/Binaries/Win64/UE4SS.dll" ".../RTypeFinal2/Binaries/Win64/RTypeFinal2-Win64-Shipping.exe"
```
如果成功， `RTypeFinal2-Win64-Shipping.exe` 所在的目录下会生成一个叫 `RTypeFinal2-Win64-Shipping.exe~` 的备份文件。
