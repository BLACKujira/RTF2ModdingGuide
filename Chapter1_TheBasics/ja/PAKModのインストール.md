# PAK Modのインストール

## PAK Modとは？
`PAK Mod`は、`Blueprint Mod`のスーパーセットであり、ファイル名が`.pak`で終わることが特徴です。このModは主に数値の変更、テクスチャや音楽の置き換えに使用され、Modローダーを必要としません。

通常、`PAK Mod`のファイル名は`_P`で終わりますが、`Blueprint Mod`はこのような命名ルールではありません。

## PAK Modのインストール場所を特定する
`Blueprint Mod`と同様に、まずゲームのインストールディレクトリを開きます。その後、`RTypeFinal2`フォルダを開き、続いて`Content`フォルダ、最後に`Paks`フォルダを開きます。ここには、複数の`.pak`および`.sig`ファイルのペアが表示されます。

![PaksFolder](../image/PaksFolder.png)

このフォルダが`PAK Mod`ファイルを配置する場所です。

## PAK Modのインストール方法
`PAK Mod`の`.pak`ファイルを`Paks`フォルダにコピーします。対応する`.sig`ファイルがあれば、それも一緒にコピーします。

もし`.sig`ファイルがない場合は、`Paks`フォルダから任意の`.sig`ファイルをコピーし、`.pak`ファイルと同じ名前にリネームしてください。

![PaksFolderWithMod](../image/PaksFolderWithMod.png)

- `Blueprint Mod`と異なり、`.pak`ファイルのリネームは動作に影響しない場合もありますが、基本的にはリネームしない方が良いです。特に**`_P`を削除しないでください**。

## タイトル画面の音楽を置き換えるModの例
1. [RTypeFinal2MusicMod](https://github.com/BLACKujira/RTypeFinal2MusicMod) の[Releases](https://github.com/BLACKujira/RTypeFinal2MusicMod/releases)ページから`TitleBGM_Final_P.pak`ファイルをダウンロードします。
2. `TitleBGM_Final_P.pak`を`Paks`フォルダにコピーします。
3. `Paks`フォルダ内の`pakchunk0-WindowsNoEditor.sig`をコピーして、`TitleBGM_Final_P.sig`にリネームします。
4. ゲームを起動します。インストールが成功していれば、タイトル画面のBGMが変更されます。

## 拡張情報：PAKファイルのリソース上書きルール
異なる`.pak`ファイルが同じ場所・名前のリソースを含む場合、ゲームは`.pak`ファイル名に基づいてどのリソースを使用するかを決定します（具体的なルールは不明です）。特に、`_P`で終わるファイルは最も高い優先順位を持つため、ほとんどの`PAK Mod`はこのサフィックスが付いています。`_P`を削除すると、Modが動作しなくなる可能性があります。

この特性はゲームパッチのために設計されたようですが、Mod開発者にとって簡単にゲームリソースを置き換える方法を提供しています。

もし2つのMod（`PAK Mod`または`Blueprint Mod`）が同じリソースを含む場合、リソースの競合が発生し、どちらかまたは両方のModが正常に動作しなくなることがあります。特に似たタイプのModではその可能性が高くなります。

## 拡張情報：PAK Modが正常にインストールされたかの確認方法
`PAK Mod`はカスタムロジックを実行できないため、`Blueprint Mod`や`LUA Mod`のようにインストール成功のメッセージを出力することはできません。ゲーム内で変更された内容が確認できる場合にのみ、インストール成功を判断できます。

もし`.pak`ファイルの内容を知っている場合、*UE4SS*のデバッグウィンドウを使って対応するリソースを確認し、インストール成功を検証できます。

Mod作者がインストール状態を検出して情報を出力するための診断用`Blueprint Mod`や`LUA Mod`を公開することもあります。また、スコアチャレンジのステージ画像のようなわかりやすい内容を置き換えてインストール成功を示す場合もあります。
