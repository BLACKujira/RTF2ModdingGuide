# Modマネージャーの使用方法

UE4SSとModのインストール手順が複雑すぎる問題を解決するために、私は [R-Type Final 2 Mod マネージャー](https://github.com/BLACKujira/RTF2ModManager) を制作しました。  
これは *R-Type Final 2* のMod導入を簡略化するためのグラフィカル管理ツールで、多言語切り替え、自動ゲームディレクトリ検出、UE4SSのインストール、および一般的なModのワンクリック管理に対応しています。

## Modマネージャーのダウンロード

まず、[RTF2ModManager の Releases](https://github.com/BLACKujira/RTF2ModManager/releases) ページから `RTF2ModManager.zip` をダウンロードしてください。

![RTF2MM_Releases](../image/RTF2MM_Releases.png)

ダウンロードしたZIPファイルを任意のフォルダに**解凍**します。

解凍後、フォルダ内の `RTF2ModManager.exe` を実行します。

![RTF2MM_Folder](../image/RTF2MM_Folder.png)

> **注意：ZIPファイル内から直接 `RTF2ModManager.exe` を実行しないでください。**  
> Modファイルが見つからずエラーが発生する可能性があります。

## ゲームディレクトリの設定

Steam版でデフォルトのインストール先（`\Program Files (x86)\Steam\steamapps\common\R-Type Final 2`）を変更していない場合、プログラムは起動時に自動でゲームフォルダを検出します。  
この場合、「ゲームディレクトリ設定」欄には検出されたパスが表示されます。

![RTF2MM_AutoSearch](../image/RTF2MM_AutoSearch.png)

もし「ゲームディレクトリ設定」欄に `ゲームディレクトリを選択してください` と表示されている場合は、右側の「手動選択」ボタンをクリックします。

![RTF2MM_ManualSelect](../image/RTF2MM_ManualSelect.png)

表示されたウィンドウで、`RTypeFinal2.exe` があるフォルダを選択してください。  
このフォルダ内には `Engine` や `RTypeFinal2` フォルダなどが含まれています。OSTを購入している場合は、OSTフォルダもここに存在します。

![GameDir](../image/GameDir.png)

## UE4SSのインストール

「UE4SS管理」欄には現在の *UE4SS* のインストール状態が表示されます。  
ほとんどのModは *UE4SS* が必要です。  
「インストール」ボタンをクリックすると、`v2.0.4` 用の *AOBスクリプト* を含むUE4SSを自動で導入します。

![alt text](../image/RTF2MM_UE4SSInstall.png)

初回インストール後は、**一度ゲームを起動**して必要なファイルやフォルダを生成してください。  
インストールが成功している場合、ゲーム起動時に *UE4SSコンソール* とコマンドラインウィンドウが同時に表示されます。  
また、Modマネージャーに戻ると「UE4SS管理」欄の `LogicMods フォルダが見つかりません。UE4SS のインストール後に一度ゲームを起動してください。改善しない場合は手動での注入をお試しください` という警告が消えます。  
これでModをインストールできるようになります。

### 静的注入の使用

UE4SSをインストールした後にゲームを起動しても *UE4SSコンソール* やコマンドラインウィンドウが表示されない場合、あなたの環境では `UE4SS.dll` が自動でゲームプロセスに注入されていない可能性があります。  
この場合、「静的注入」機能を使って強制的に解決できます。

![RTF2MM_UE4SSInject](../image/RTF2MM_UE4SSInject.png)

「静的注入」をクリックし、しばらく待機してください。完了後にもう一度ゲームを起動して、必要なファイル・フォルダを生成させます。

## Modのインストール

「Mod管理」欄の左側リストには、対応しているModとインストール状況が表示されます。  
リストの項目を選択すると、右側に詳細情報が表示されます。  
下部の「インストール」ボタンをクリックすると、選択したModが自動的に導入されます。  
依存関係のあるモジュールも自動的に処理されます。

![RTF2MM_ModInstall](../image/RTF2MM_ModInstall.png)

右側の詳細欄に  
`UE4SS がインストールされていないため、PAK 以外のモジュールを含む Mod をインストールできません。`  
または  
`LogicMods フォルダーが検出されませんでした。ブループリントモジュールを含む Mod をインストールできません。`  
と表示されている場合は、UE4SSが正しくインストールされ、少なくとも一度ゲームを起動しているか確認してください。

> このプログラムがサポートしているModは以下の4つのみです：  
> [G-Type Origin](https://github.com/BLACKujira/GTypeOrigin)、  
> [Simple Boss LifeBar](https://github.com/BLACKujira/SimpleBossLifeBarMod)、  
> [RTF2 Debug Tools](https://github.com/BLACKujira/RTF2DebugToolsMod)、  
> [FPS Player](https://github.com/BLACKujira/FPSPlayerMod)  
> それ以外のModは手動でインストールする必要があります。

## セーブデータのバックアップ

Modをプレイした後に元の状態へ戻したい場合や、セーブデータの破損が心配な場合は、事前にバックアップを取っておくことをおすすめします。

プログラム下部の「ショートカット機能」欄にある「セーブデータフォルダを開く」ボタンをクリックすると、通常は自動でセーブフォルダが開きます。

その中のファイル（特に `SLOT00.sav` ― メインセーブデータ）を**コピー**して、別の場所に保存してください。
