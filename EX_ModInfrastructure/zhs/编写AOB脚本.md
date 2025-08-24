# 编写AOB脚本

在2025年8月的 `2.0.4` 更新后，*UE4SS* 出现了找不到重要函数AOB特征签名的问题，需要手动编写AOB脚本来解决。

合适的 AOB 脚本可以在不同环境下稳定定位目标函数，并且可以共享给其他用户，确保 *UE4SS* 正常运行。

## AOB的原理和作用

AOB（Array of Bytes） 是通过在进程内存中搜索连续字节序列来定位特定函数或数据地址的方法。在 UE4SS 启动时，它会用 AOB 自动绑定一些关键函数，包括：

- GUObjectArray
- GMalloc
- FName_ToString
- FName_Constructor
- FText_Constructor
- **StaticConstructObject**

如果内置的查找方法失败或匹配到多个地址，UE4SS 就无法正常工作。例如：

- 找不到地址的报错示例 
    ```
    [PS] Failed to find GNatives: expected at least one value`
    ```
- 找到多个地址的报错示例 （旧版本不会显示地址）
    ```
    [PS] Failed to find StaticConstructObject_Internal: found 2 unique values [7FF6CF1A8AF0, 7FF6D10A4DC0]
    ```

错误信息下方通常会提示：
```
`[PS] You can supply your own AOB in 'UE4SS_Signatures/StaticConstructObject.lua'`
```

注意：AOB 不一定必须是函数起始地址。通过间接寻址或偏移计算，也可以定位到正确地址。但只要选用足够长的序列，理论上可以定位函数起始地址，不过游戏每次更新后可能会失效，需要重新编写。

关于AOB脚本的格式和更多信息请参考 [UE4SS官方文档](https://docs.ue4ss.com/guides/fixing-compatibility-problems.html) 。

本教程以 `StaticConstructObject` 为例，介绍一种 *直接寻址* 到 *有多个匹配地址* 的函数的方式。

## 准备工作

确保你的 *UE4SS* 版本在 `v3.0.1` 的实验版及以上 （`v3.0.1` 正式版及以下不会显示地址）。

如果想编写通用的AOB脚本，请准备 *X64dbg* 或者 *IDA Pro* 这类反汇编调试工具。

## 通过硬编码找出正确的地址

将以下内容保存为 StaticConstructObject.lua（或对应函数名）到 `\RTypeFinal2\Binaries\Win64\UE4SS_Signatures` ：

``` LUA
function Register()
    return "00" -- 这里的"00"不需要修改...如果没有出现问题的话
end

function OnMatchFound(matchAddress)
    return 0x7FF6D10A4DC0 -- 换成你要尝试的地址
end
```

将注释处的地址改为需要尝试的匹配地址。如果启动游戏时 *UE4SS* 输出了

```
AOB scans could not be completed because of the following reasons:
Was unable to find AOB for 'StaticConstructObject' via Lua script
```

则代表没能匹配到序列，可以尝试将 `Register()` 中返回的序列改成内存中任意一段固定且唯一的序列。如果 `Register()` 中返回的都是通配符也会出现这个问题。

如果输出类似：

```
StaticConstructObject_Internal address: 0x7ff6d10a4dc0 <- Lua Script
```

这样的代表找到了序列，并成功将硬编码的地址标记为函数的入口。如果游戏报错崩溃则代表地址不对，请继续尝试其他地址；反之则代表找到了地址，记下这个地址和它在数组中的位置。

注意：由于程序启动内存分配可能会变化，这种方法可能不稳定，仅适合快速验证。

## 提取AOB序列

使用 *X64dbg* 或者 *IDA Pro* 调试 `RTypeFinal2.exe` ，跳转到之前找到的正确地址。注意看一下这里的汇编是否具有函数起始特征。若非起始位置，可能是内存分配发生变化。此时可移除硬编码的临时脚本，跳转至多重匹配报错中相同位置的地址。

将这个地址向下约32字节的内存复制为十六进制，将其中可能发生变化的地址替换为通配符 `??` ，将刚刚的脚本做如下修改。

``` LUA
function Register()
    return "48 89 5C 24 10 48 89 6C 24 18 48 89 74 24 20 57 41 56 41 57 48 81 EC ?? ?? ?? ?? 48 8B 05 ?? ?? ?? ?? 48 33 C4" -- 这里换成你提取的十六进制序列
end

function OnMatchFound(matchAddress)
    return matchAddress -- 将之前硬编码的地址改为matchAddress
end
```

如果你和我一样对汇编不熟悉，可以将十六进制和反汇编内容发给AI，让AI帮你判断哪些地址可能会发生变化。

启动游戏，如果游戏和UE4SS没有崩溃报错，并且输出了类似 `StaticConstructObject_Internal address: 0x7ff6d10a4dc0 <- Lua Script` 的信息，则代表成功。

- 如果提示找不到地址 → 则检查是否所有可能发生变化的地址都替换成了通配符 `??` 。

- 如果提示找到了多个地址 → 则说明AOB序列不够长或不够独特，需要提取更多字节，或者换一个地址使用间接寻找定位。

建议跨设备或重启后复测，验证AOB序列在不同内存分配下的稳定性。之后可以在社区中发布这个AOB脚本，帮助其他用户解决问题。