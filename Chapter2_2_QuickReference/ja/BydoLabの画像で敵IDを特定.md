# BydoLabの画像から敵IDを特定する方法

- まず、FModelを開き、`Content/Design/texture/Bydolabo/img_bydo` に移動して、このフォルダー内のすべての画像を抽出します。

- 次に、画像を保存したフォルダーを開き、敵の見た目を確認し、該当する敵を探します。ファイル名の中央部分が敵のIDになります。

このIDを元に、以下の情報を見つけることができます：

- `/Content/Enemy/ID/IDParamAsset.uasset`：敵の定義ファイルで、敵のクラスやパラメータが記録されています。ステージ内でのオブジェクトプール作成に使用されます。
- `/Content/character/Enemy/ID/`：敵のモデル、アニメーション、テクスチャ、マテリアルが含まれています。（Yルート、Zルート、または後から追加されたステージは、それぞれのプラグイン内にあります。）
- `/Content/Data/BydoData.uasset` 内で画像を検索すると、そのローカライズキー名も確認できます。

## 例：Stage 3.0 と Stage X6.0 に登場する浮遊砲台
![E386](../image/E386.png)

- 画像からIDがE386であると判別できます。
- 対応する敵定義ファイルは `/Content/Enemy/E386/E386ParamAsset.uasset` です。
- 発射する弾の定義は `/Content/Enemy/E386/S386ParamAsset.uasset` にあります。
- モデルは `/Content/character/Enemy/E386/E386_01.uasset` に格納されています。
- `/Content/Data/BydoData.uasset` ではIDが `102`、ローカライズキーは `NAME_103_SourceString` です。

# 後書き

ゲームには確かに敵とIDの対応関係が存在しますが、全体を網羅した敵のリストはありません。*BydoLab* は公式に公開されたステージに登場した敵しか記録していません。そのため、この方法では未公開ステージの敵IDを特定することはできません。