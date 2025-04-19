# 使用FModel查看和解包游戏资源

*FModel* 是一个强大的 *UE4/5* 资源解包器，个人认为其在Mod开发中的重要性仅次于 *UE4SS*，对于 *R-Type Final 2* 需要提供 *AES密钥* 和 *.usmap映射文件* 才能正常解包。

## 选择目录

打开 *FModel* ，点击菜单中的 `Settings`，将 `Archive Directory` 设置为游戏目录下的 `RTypeFinal2` 文件夹（例：`D:\Program Files (x86)\Steam\steamapps\common\R-Type Final 2\RTypeFinal2`），`UE_Versions` 设置为 `GAME_UE4_26`。

点击确定，如果设置正确，你会发现左侧显示了游戏的 `.pak` 文件，但这些文件是灰色的，还无法解包。

目前 *FModel* 的菜单中的 `Directory` -> `Selector` 似乎还提供了自动检测游戏并设置的功能，或许可以试一试。

## 载入AES密钥

点击 *FModel* 的菜单中的 `Directory` -> `AES` ，依次尝试使用 *AESKeyFinder* 导出的密钥，当密钥正确时，左侧的 `.pak` 文件名会变成白色。此时就可以点击解包按钮了。

将 `Loading Mode` 调整成 `ALL` ，点击 `Load`，切换到 `Folders` 标签，就可以看到游戏的资源和目录了，但如果尝试预览或导出依旧会报错。

## 载入.usmap映射文件

点击 *FModel* 菜单中的 `Settings`，勾选 `ADVANCED` 中的 `Local Mapping File`，将 `Mapping File` 设置为之前导出的 `.usmap映射文件` 。此时就可以正常预览或导出资源了。