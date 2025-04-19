# 获取AES密钥和usmap映射文件

和许多UE4/5游戏一样， *R-Type Final 2* 的资源文件经过了加密，并且使用了特殊的映射方式。解包/修改游戏内资源时通常要用到 *AES密钥* 和 *`.usmap`映射文件*

## 获取AES密钥

下载 [AESKeyFinder](https://github.com/GHFear/AESKeyFinder-By-GHFear) ，并参考 [这个教程](https://github.com/Dmgvol/UE_Modding/blob/main/TheBasics/AesKey.md) 的第一种方式，将 `RTypeFinal2-Win64-Shipping.exe` 复制到 *AESKeyFinder* 的文件夹中，执行脚本，导出密钥。

当前版本中一共会导出四个密钥，只有一个是有效的。

## 导出 .usmap 映射文件

有两种方式，比较简便的是使用 *UE4SS* 导出 `.usmap` 映射文件。参考 [这个教程](https://github.com/Dmgvol/UE_Modding/blob/main/TheBasics/Extractingusmap.md) 即可。

另一种方式是使用 [Dumper-7](https://github.com/Encryqed/Dumper-7) 。下载或克隆代码后编译这个项目，使用 *任意DLL注入器* 将其注入到游戏进程中。导出的内容中包括 `.usmap` 映射文件。

## 各种工具对这两种文件的需求

| 工具       | 是否需要 AES 密钥 | 是否需要 `.usmap` 映射文件 |
|------------|------------------|------------------------------|
| FModel     | ✅                | ✅                            |
| UModel     | ✅                | ❌                            |
| UAssetGUI  | ❌                | ✅                            |