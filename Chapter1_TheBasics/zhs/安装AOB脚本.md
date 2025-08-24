# 安装AOB脚本
在 *R-Type Final 2* 的 `v2.0.4` 版本更新后，出现了 *UE4SS* 找不到 `StaticConstructObject` AOB签名的问题。本教程介绍如何在 [安装 *UE4SS*](安装UE4SS.md) 后为其加上AOB脚本。

## 判断是否需要安装AOB脚本

如果在启动安装了 *UE4SS* 的游戏时，控制台输出中出现了多条

```
[PS] Failed to find GNatives: expected at least one value
[PS] You can supply your own AOB in 'UE4SS_Signatures/GNatives.lua'
```

或者

```
[PS] Failed to find StaticConstructObject_Internal: found 2 unique values
[PS] You can supply your own AOB in 'UE4SS_Signatures/StaticConstructObject.lua'
```

之类的错误信息，并且Mod无法加载，则说明需要安装AOB脚本。`

![AOBErrorLog](../image/AOBErrorLog.png)

## 下载AOB脚本

进入 [RTF2-UE4SS-AOB](https://github.com/BLACKujira/RTF2-UE4SS-AOB) 仓库，在右侧的 [Releases](https://github.com/BLACKujira/RTF2-UE4SS-AOB/releases) 页面中，下载对应版本的所有 `.lua` 文件。

理论上来说，这个脚本应该可以用于不同的 *UE4SS* 版本，已经在 *UE4SS* `v3.0.1` 的正式版和实验版上进行过测试。

## 安装AOB脚本

和安装UE4SS时一样，首先打开游戏的安装目录。之后打开 `RTypeFinal2` 文件夹，依次打开其中的 `Binaries` 、 `Win64` 和 `UE4SS_Signatures` 文件夹。你可以看到这里有 `FName_ToString.lua.example` 和 `GUObjectArray.lua.example` 这两个文件。

将下载的 `.lua` 放置于这个文件夹即可，请不要重命名 `.lua` 文件。

![UE4SS_Signatures](../image/UE4SS_Signatures.png)

## 检验安装

### 1. 安装成功 或 脚本bug

如果输出类似于以下内容，并且游戏没有崩溃，则说明安装成功。

```
StaticConstructObject_Internal address: 0x7ff6d10a4dc0 <- Lua Script
```

如果游戏崩溃，则代表 AOB 脚本定位到了错误的位置，请移除脚本并联系脚本开发者。

### 2. 版本不匹配 或 脚本bug

如果输出类似于以下内容，则说明版本不匹配，请检查脚本和游戏版本是否对应。

也有可能是脚本本身选取的 AOB 有问题，这种情况请联系脚本开发者。

```
AOB scans could not be completed because of the following reasons:
Was unable to find AOB for 'StaticConstructObject' via Lua script
```

### 3. 安装失败

如果依旧输出类似于下面的内容

```
[PS] Failed to find GNatives: expected at least one value
```

或者

```
[PS] Failed to find StaticConstructObject_Internal: found 2 unique values [7FF6CF1A8AF0, 7FF6D10A4DC0]`
```

则表示脚本未加载，请检查是否将脚本放置于正确的位置，以及脚本的文件名是否正确。

在 *UE4SS* `v3.0.1` 实验版中，还有两个可选的函数 `GNatives` 和 `ConsoleManagerSingleton` 也同样无法通过内置方法定位，并输出这些信息。但UE4SS可以正常启动，暂时也不影响Mod的使用。


# DIY脚本

如果你想自己编写 AOB 脚本，可以参考这里的教程： [编写AOB脚本](../../EX_ModInfrastructure/zhs/编写AOB脚本.md) 