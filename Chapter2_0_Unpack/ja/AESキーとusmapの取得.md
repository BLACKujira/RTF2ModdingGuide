# AESキーと`.usmap`マッピングファイルの取得

多くのUE4/5ゲームと同様に、*R-Type Final 2* のリソースファイルは暗号化されており、特殊なマッピング方式が使用されています。ゲーム内リソースをアンパックまたは改造するには、通常 *AESキー* と *.usmap マッピングファイル* の両方が必要です。

## AESキーの取得

[AESKeyFinder](https://github.com/GHFear/AESKeyFinder-By-GHFear) をダウンロードし、[このガイド](https://github.com/Dmgvol/UE_Modding/blob/main/TheBasics/AesKey.md) の「方法1」に従ってください。`RTypeFinal2-Win64-Shipping.exe` を *AESKeyFinder* のフォルダにコピーし、スクリプトを実行してキーを抽出します。

現在のバージョンでは、4つのキーが抽出されますが、そのうち有効なのは1つだけです。

## `.usmap` マッピングファイルの抽出

方法は2つあります。簡単なのは *UE4SS* を使用して `.usmap` ファイルを抽出する方法です。[このチュートリアル](https://github.com/Dmgvol/UE_Modding/blob/main/TheBasics/Extractingusmap.md) を参考にしてください。

もう一つの方法は [Dumper-7](https://github.com/Encryqed/Dumper-7) を使う方法です。プロジェクトをダウンロードまたはクローンしてコンパイルし、*任意のDLLインジェクター* を使ってゲームプロセスに注入します。抽出された内容に `.usmap` ファイルが含まれています。

## 各ツールにおけるファイルの必要性

| ツール       | AESキーが必要か | `.usmap` マッピングファイルが必要か |
|--------------|----------------|--------------------------------------|
| FModel       | ✅              | ✅                                    |
| UModel       | ✅              | ❌                                    |
| UAssetGUI    | ❌              | ✅                                    |
