# kismet-analyzer を使用してブループリントを分析する
[kismet-analyzer](https://github.com/trumank/kismet-analyzer) は、`.uasset` ブループリントファイルおよび `.umap` マップファイルを分析し、その内部のロジックをフローチャートのような形で表示するツールです。

## 必要なスキルとリソース

### スキル
- `C#` 開発 (自分で *kismet-analyzer* を生成したい場合)

### リソース
- `.NET 8.0` の生成および実行環境
- 解凍された `raw data (.uasset)` ゲームリソース 
- ゲームの `.usmap` マップファイル

## kismet-analyzer の準備

以下の手順を行うことで、kismet-analyzer を準備できます。もし事前に生成された *kismet-analyzer* を使用したい場合は、[Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) からダウンロードできますが、.NET 8.0 ランタイムも必要です。

### 手順1：kismet-analyzer リポジトリをクローンする

- まず、[kismet-analyzer](https://github.com/trumank/kismet-analyzer) のコードをダウンロード、または任意の `Git` クライアントを使用してクローンします。

多くの `Git` クライアントはこのプロジェクト内の *UAssetAPI* プロジェクトを同期的に取得しないため、*UAssetAPI* プロジェクトも手動でダウンロードまたはクローンし、適切なフォルダに配置する必要があります。

### 手順2：生成環境の設定

- *Visual Studio* や他のIDEを使用して `kismet-analyzer.csproj` を開き、生成を試みます。多くの場合、この時点で生成が失敗します。

もし `NET SDK は .NET 8.0 をターゲットとして設定することをサポートしていません。 .NET 6.0 またはそれ以下のバージョンをターゲットとして設定するか、.NET 8.0 をサポートする .NET SDK バージョンを使用してください` というエラーが表示される場合、[.NET 8.0 SDK](https://dotnet.microsoft.com/ja-jp/download/visual-studio-sdks) と `.NET 8.0 ランタイム` をインストールする必要があります。

### 手順3：UAssetAPI と kismet-analyzer の生成

この時点で *kismet-analyzer* を生成しようとすると `D:\Extract\kismet-analyzer\UAssetAPI\UAssetAPI\bin\Debug\net8.0\UAssetAPI.dll` ファイルが見つからないというエラーが発生します。そのため、まずは *UAssetAPI* を生成する必要があります。

- IDEを使用して `UAssetAPI\UAssetAPI\UAssetAPI.csproj` を開き、プロジェクトを生成します。
- 次に `kismet-analyzer` を生成します。

### 手順4：Graphviz のインストール

- *kismet-analyzer* は [Graphviz](https://graphviz.org/) を使用してフローチャートを生成するため、*Graphviz* をインストールする必要があります。
- インストール時に `PATH` システム変数に追加するオプションを選択してください。そうでなければ手動で `PATH` に追加するか、*kismet-analyzer* のコードを変更する必要があります。

## kismet-analyzer を使用してゲームリソースを分析する

- *コマンドプロンプト* を開き、以下の形式でコマンドを入力します。

```
"(生成された kismet-analyzer のディレクトリ)\kismet-analyzer.exe" cfg "(分析する .uasset または .umap ファイル)" -m "(.usmap マップファイルの場所)" --ue-version VER_UE4_26
```

`(生成された kismet-analyzer のディレクトリ)` 、 `(分析する .uasset または .umap ファイル)` 、および `(.usmap マップファイルの場所)` を実際のパスに置き換えてください。

例：

```
"D:\Extract\kismet-analyzer\bin\Debug\net8.0\kismet-analyzer.exe" cfg "E:\Extract\RTypeFinal2\Content\character\Enemy\E000\ABP_E000_POW_01.uasset" -m "D:\Extract\Dumper-7\Unicode-Names-4.26.0-0+++UE4+Release-4.26-RTypeFinal2\Mappings\4.26.0-0+++UE4+Release-4.26-RTypeFinal2.usmap" --ue-version VER_UE4_26
```


成功すれば、ブラウザが開き、フローチャートがウェブ形式で表示されます。

---

もし次のエラーが発生した場合：

```
System.ComponentModel.Win32Exception (2): An error occurred trying to start process 'dot' with working directory 'D:\Extract\kismet-analyzer\bin\Debug\net8.0'. The system cannot find the file specified.
   at System.Diagnostics.Process.StartWithCreateProcess(ProcessStartInfo startInfo)
   at System.Diagnostics.Process.Start(ProcessStartInfo startInfo)
   at KismetAnalyzer.Program.WriteDotViewer(String dot, String outputPath, String dotPath) in D:\Extract\kismet-analyzer\Program.cs:line 235
   at KismetAnalyzer.Program.Cfg(EngineVersion ueVersion, String mappings, String assetPath, String dotPath) in D:\Extract\kismet-analyzer\Program.cs:line 262
   at System.CommandLine.Handler.<>c__DisplayClass5_04.<SetHandler>b__0(InvocationContext context)
   at System.CommandLine.Invocation.AnonymousCommandHandler.Invoke(InvocationContext context)
   at System.CommandLine.Invocation.InvocationPipeline.<>c__DisplayClass4_0.<<BuildInvocationChain>b__0>d.MoveNext()
```

`graphviz` が正しく `PATH` システム変数に追加されているかを確認してください。もし追加されていなければ、`dot.exe` の場所を指定するか、エラーメッセージ内の `Program.cs:line 235` 付近のコードを変更して、`dot.exe` のパスをハードコードする必要があります。

## 最後に

ゲームのロジックの大部分は `C++` コードで実装されているため、残念ながらこの方法では限られたゲームロジックしか分析できません。

しかし、非常に重要な *ゲームマップ* のロジックはブループリント内にあり、*kismet-analyzer* を使用して分析できます。そう、あの見た目が頭痛を引き起こすブループリントのロジックを再現しないと、自分でカスタムレベルを実行できません。幸い、これらのロジックの大部分は不要な if 分岐であり、残りのロジックを再現するのは一人だけで十分です。その再現作業はすでに私が行いました。

また、ユーザーインターフェース、アニメーションブループリント、ブループリント関数ライブラリもこの方法で分析でき、非常に有用な情報を得ることができます。

*kismet-analyzer* は主にブループリントのロジックを表示しますが、リソース自体の属性、パラメータ、変数の詳細情報を取得するには、*FModel* を使用して JSON に変換するか、*UAssetGUI* を使用する必要があります。
