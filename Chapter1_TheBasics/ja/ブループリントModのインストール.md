# ブループリントModのインストール

## どのようなModがブループリントModか
`ブループリントMod` は特別な `PAK Mod` の一種で、特徴としてPAK Modと同様、`.pak` で終わるファイルです。しかし、UE4SSのようなModローダーが必要で、正しく動作するためにはこれが必要です。インストール方法はPAK Modとは少し異なり、Mod作者が提供する情報を元にどちらのタイプのModかを判断する必要があります。

通常、`PAK Mod` のファイル名は `_P` で終わりますが、`ブループリントMod` はそのような名前の規則はありません。

## ブループリントModのインストール場所を特定する
UE4SSをインストールする際と同じように、まずゲームのインストールディレクトリを開きます。次に、`RTypeFinal2` フォルダを開き、その中の `Content` フォルダ、さらに `Paks` フォルダを開きます。ここで、いくつかの `.pak` ファイルと `.sig` ファイルのペアを見ることができます。

![PaksFolder](../image/PaksFolder.png)

UE4SSが正常にインストールされていて、ゲームを少なくとも1回実行している場合、`Paks` フォルダの中に `LogicMods` フォルダが出現します。このフォルダがブループリントModのインストール場所です。

- ゲームを正常にインストールした後でもこのフォルダが見つからない場合は、手動で `LogicMods` フォルダを作成してください。

## ブループリントModのインストール
ブループリントModの **`.pak` ファイル** を `LogicMods` フォルダにコピーします。もし `.sig` ファイルがあれば、それも一緒にコピーします。

もし `.sig` ファイルがない場合は、`Paks` フォルダから適当な `.sig` ファイルを**コピー**し、`LogicMods` フォルダに貼り付けて、`ブループリントMod` の `.pak` ファイルと同じ名前にリネームします。

- PAK Modとは異なり、**ブループリントModの.pakファイルをリネームしないでください**、Mod作者が特に要求した場合を除き、そうしないとブループリントModが正常に機能しません。

![LogicModsFolder](../image/LogicModsFolder.png)

### SimpleBossLifeBarModの例
1. [SimpleBossLifeBarMod](https://github.com/BLACKujira/SimpleBossLifeBarMod) の [Releases](https://github.com/BLACKujira/SimpleBossLifeBarMod/releases) ページから `SimpleBossLifeBar.pak` ファイルをダウンロードします。
2. `SimpleBossLifeBar.pak` を `LogicMods` フォルダにコピーします。
3. `Paks` フォルダから `pakchunk0-WindowsNoEditor.sig` をコピーし、`LogicMods` フォルダに貼り付けて、`SimpleBossLifeBar.sig` にリネームします。
4. ゲームを実行し、インストールが成功したか確認します。ゲームを起動した際、UE4SSのコンソールに以下のような出力が表示されます：
```
[xx:xx:xx] [Lua] [SimpleBossLifeBar] ModActorPath: /Game/Level/title/title.title:PersistentLevel.ModActor_C_2147482405
[xx:xx:xx] [Lua] [SimpleBossLifeBar] WE ARE NOW RUSHING INTO STAGE 0 BE ON YOUR GUARD!
```

## 拡張読書：.pakファイルとは何か
`.pakファイル` はUnreal Engineのリソースファイルで、ゲームのテクスチャ、マテリアル、音楽、マップなどのデータが保存されています。

Unreal Engineはこれらのファイルにパッチを適用することを考慮して設計されており、1つの `.pak` ファイルの内容が他の `.pak` ファイルの内容を上書きすることができます。`PAK Mod` はこの特性を利用してゲーム内のコンテンツを変更します。しかし、`PAK Mod` は通常静的で、ゲームの画面、音、データを変更することはできますが、新しいゲームコンテンツを追加することはできません。

一方、`ブループリントMod` の `.pak` ファイルには特別なエントリーポイントが含まれています。UE4SSのようなModローダーを使うことで、このエントリーポイントをゲームのレベルに生成し、ゲームコンテンツを拡張することができます。

UE4SSのブループリントModシステムは、.pakファイルのファイル名を使用して、.pakファイル内の同名のパスにあるエントリーポイントを探します。これが、ブループリントModの.pakファイルをリネームしてはいけない理由です。

## 拡張読書：.sigファイルとは何か
`.sigファイル` は `.pakファイル` の署名ファイルで、ゲームは `.pak` ファイルをロードする際に対応する `.sig` ファイルの存在を確認します。もし `.sig` ファイルが存在しない場合、`.pak` ファイルは読み込まれません。そのため、`Paks` フォルダ内の `.sig` ファイルと `.pak` ファイルはペアで存在する必要があります。

同様に、Mod作者が追加した `.pak` ファイルにも対応する `.sig` ファイルが必要です。幸い、ゲームは `.sig` ファイルの詳細な検証を行わないため、Mod開発者は `.sig` ファイルがどのように生成されるかを理解する必要はありません。ゲーム本体の `.sig` ファイルをコピーして、 `.pak` ファイルと同じ名前にリネームすれば、ゲームを欺くことができます。
