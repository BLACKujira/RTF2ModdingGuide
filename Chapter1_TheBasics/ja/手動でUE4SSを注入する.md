# 手動でUE4SSを注入する

インストールが正しく行われているにもかかわらず、UE4SSがゲームの起動時に一緒に立ち上がらない場合は、UE4SSインストールディレクトリに `UE4SS.log` ファイルが存在するかを確認してください。もしない場合、UE4SSがゲームプロセスに自動で注入されていないことになります。この場合、DLLを手動で注入する必要があります。

この問題は、Windows7以下のシステムで発生することが多いようですが、システムによるものとは限らないという証拠はありません。

## DLL注入ツールの準備

ここでは、`Detours` の `setdll.exe` を使用してDLLを注入する方法を推奨します。`Detours` はMicrosoftが公式にメンテナンスしているプロジェクトなので、ウイルスとして誤認識されることはありません。

また、`setdll.exe` はゲームの実行可能ファイルにDLLを注入し、ゲームと共に自動的に起動します。毎回手動で注入する必要はありません。

私を信頼している場合は、[Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) ページから私がビルドした `setdll.exe` をダウンロードできます。または、[detours](https://github.com/microsoft/detours) のコードをクローンして自分でビルドすることもできます。ビルドした `setdll.exe` は `bin.X64` フォルダ内に保存されます。

## 注入スクリプトの使用

DLL、注入ツール、ゲームファイルが固定されているため、注入操作を簡略化するためにバッチファイルを作成しました。

1. まず、[Releases](https://github.com/BLACKujira/RTF2ModdingGuide/releases) から `setdll.exe` と `ManuallyInjectUE4SS.bat` をダウンロードします。
2. `setdll.exe` と `ManuallyInjectUE4SS.bat` を `RTypeFinal2\Binaries\Win64` フォルダに移動します。このフォルダには `RTypeFinal2-Win64-Shipping.exe` と `UE4SS.dll` が存在します。
3. `ManuallyInjectUE4SS.bat` をダブルクリックして実行します。**コマンドプロンプト** が開き、手動で `UE4SS.dll` を注入する指示が実行されます。

- 注入に成功すると、**コマンドプロンプト** にDLL名が並んだ後、`Injection successful! Launching the game...` と表示され、ゲームが起動します。その他のメッセージは注入失敗を意味します。
- `Injection skipped to avoid overwriting the backup file.` と表示された場合は、スクリプトが以前の注入時に残したバックアップファイルを検出したことを意味します。再度注入しないでください。

## 代替方法：コマンドでDLLを注入する方法

注入スクリプトが機能しない場合、次の方法でDLLを注入できます。

**Windows10以上** の場合、`Win + X` を押して、表示されたメニューから **コマンドプロンプト** または **Power Shell** を開きます。

**Windows7以下** の場合、スタートメニューを開き、**実行** を選択し、`CMD` と入力して **コマンドプロンプト** を開きます。

**コマンドプロンプト** または **Power Shell** に以下のコマンドを入力します：
```
"(setdll.exe の場所)/setdll.exe" d:"(ゲームディレクトリ)/RTypeFinal2/Binaries/Win64/UE4SS.dll" "(ゲームディレクトリ)/RTypeFinal2/Binaries/Win64/RTypeFinal2-Win64-Shipping.exe"
```
- 上記の `(setdll.exe の場所)` と `(ゲームディレクトリ)` を、実際のパスに置き換えてください。
- コマンド内の二重引用符を削除しないでください。この部分が何のために使われるか分からない場合でも、そのままにしてください。

エンターキーを押すと、注入が成功すれば `RTypeFinal2-Win64-Shipping.exe` が更新され、同時に `RTypeFinal2-Win64-Shipping.exe~` というバックアップファイルが生成されます。

もし権限が不足しているというメッセージが表示された場合は、**コマンドプロンプト** または **Power Shell** を管理者として実行してください。

**注意：重複して注入しないでください**。そうしないと、バックアップファイル `RTypeFinal2-Win64-Shipping.exe~` が既に注入されたファイルで上書きされてしまいます。

## インストールの確認

ゲームを起動し、UE4SSのコントロールコンソールウィンドウがゲームと一緒に立ち上がれば、手動注入は成功です。

もしUE4SSの注入を解除したい場合は、バックアップファイル `RTypeFinal2-Win64-Shipping.exe~` で `RTypeFinal2-Win64-Shipping.exe` を上書きすれば元に戻せます。
