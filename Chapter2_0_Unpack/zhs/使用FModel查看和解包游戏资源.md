# 使用FModel查看和解包游戏资源

*FModel* 是一个强大的 *UE4/5* 资源解包器，个人认为其在Mod开发中的重要性仅次于 *UE4SS*，对于 *R-Type Final 2* 需要提供 *AES密钥* 和 *.usmap映射文件* 才能正常解包。

## 选择目录


1. 打开 *FModel*，点击顶部菜单栏的 `Settings`。
2. 将以下两项进行设置：
   - `Archive Directory`：设置为游戏目录下的 `RTypeFinal2` 文件夹。（例：`D:\Program Files (x86)\Steam\steamapps\common\R-Type Final 2\RTypeFinal2`）
   - `UE_Versions`：选择 `GAME_UE4_26`
3. 点击 `OK` 保存更改。

如果设置成功，左侧会显示出游戏的 `.pak` 文件，但此时它们仍然是灰色的，表示尚未解密，无法解包。

目前 *FModel* 的菜单中的 `Directory` -> `Selector` 似乎还提供了自动检测游戏并设置的功能，或许可以试一试。

## 载入AES密钥

1. 打开顶部菜单 `Directory -> AES`。
2. 使用 *AESKeyFinder* 导出的多个密钥，逐个尝试输入。
3. 当输入了正确的密钥后，左侧 `.pak` 文件名将从灰色变为白色，表示已解密成功。

此时已经可以解包基础的内容了。将 `Loading Mode` 调整成 `ALL` ，点击 `Load`，切换到 `Folders` 标签，就可以看到游戏的资源和目录了，但如果尝试预览或导出依旧会报错。

## 载入.usmap映射文件

1. 点击菜单中的 `Settings`。
2. 勾选 `ADVANCED` 设置中的 `Local Mapping File`。
3. 将 `Mapping File Path` 路径设置为之前导出的 `.usmap` 文件。

现在就可以正常预览和解包资源了。