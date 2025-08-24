# AOBスクリプトの作成

2025年8月の `2.0.4` アップデート以降、*UE4SS* で重要な関数の AOB シグネチャが見つからない問題が発生しており、手動で AOB スクリプトを作成して解決する必要があります。

適切な AOB スクリプトを用意すれば、異なる環境でも安定して対象の関数を特定でき、他のユーザーと共有することで *UE4SS* を正常に動作させることができます。

## AOBの原理と役割

AOB（Array of Bytes）は、プロセスのメモリ内で連続するバイト列を検索することで、特定の関数やデータアドレスを特定する手法です。UE4SS の起動時には、AOB によって以下のような重要な関数が自動的にバインドされます。

- GUObjectArray
- GMalloc
- FName_ToString
- FName_Constructor
- FText_Constructor
- **StaticConstructObject**

もし内蔵の検索方法が失敗したり、複数のアドレスが一致した場合、UE4SS は正常に動作しなくなります。例えば：

- アドレスが見つからなかった場合のエラーメッセージ
    ```
    [PS] Failed to find GNatives: expected at least one value`
    ```
- 複数のアドレスが一致した場合のエラーメッセージ（旧バージョンではアドレスは表示されません）
    ```
    [PS] Failed to find StaticConstructObject_Internal: found 2 unique values [7FF6CF1A8AF0, 7FF6D10A4DC0]
    ```


エラーの下には通常、次のようなメッセージが表示されます：
```
`[PS] You can supply your own AOB in 'UE4SS_Signatures/StaticConstructObject.lua'`
```


注意：AOB は必ずしも関数の先頭アドレスである必要はありません。間接参照やオフセット計算によっても正しいアドレスを特定できます。ただし十分に長いシーケンスを選べば関数の先頭を理論的に特定できますが、ゲームのアップデートごとに無効になる可能性があるため、そのたびに再作成が必要です。

AOB スクリプトのフォーマットや詳細については [UE4SS公式ドキュメント](https://docs.ue4ss.com/guides/fixing-compatibility-problems.html) を参照してください。

本チュートリアルでは `StaticConstructObject` を例に、**複数の一致アドレスを持つ関数を直接指定して解決する方法**を紹介します。

## 準備

*UE4SS* のバージョンが `v3.0.1` の実験版以上であることを確認してください（`v3.0.1` 正式版以前ではアドレスが表示されません）。

汎用的な AOB スクリプトを作成する場合は、*X64dbg* や *IDA Pro* といった逆アセンブラ・デバッガーツールを用意してください。

## ハードコードによるアドレス特定

以下の内容を `StaticConstructObject.lua` （または対象の関数名）として `\RTypeFinal2\Binaries\Win64\UE4SS_Signatures` に保存してください：

``` LUA
function Register()
    return "00" -- ここは問題がなければ "00" のままでOK
end

function OnMatchFound(matchAddress)
    return 0x7FF6D10A4DC0 -- 試したいアドレスに変更する
end
```

コメント部分のアドレスを、試したい一致アドレスに書き換えます。もしゲーム起動時に UE4SS が次のように出力した場合：

```
AOB scans could not be completed because of the following reasons:
Was unable to find AOB for 'StaticConstructObject' via Lua script
```

これはシーケンスが一致しなかったことを意味します。その場合は `Register()` で返すシーケンスを、メモリ内の固定的かつ一意のバイト列に変更してください。`Register()` がすべてワイルドカードの場合もこのエラーになります。

もし次のように出力された場合：

```
StaticConstructObject_Internal address: 0x7ff6d10a4dc0 <- Lua Script
```

これはシーケンスが見つかり、ハードコードしたアドレスが関数のエントリーポイントとして認識されたことを示します。ゲームがクラッシュする場合はアドレスが誤りなので、別のアドレスを試してください。クラッシュしなければ正しいアドレスが特定できたことになり、そのアドレスと配列内の位置を記録しましょう。

注意：プログラム起動時のメモリ割り当ては変動するため、この方法は安定性に欠け、あくまで迅速な検証用です。

AOBシーケンスの抽出

X64dbg または IDA Pro を使って `RTypeFinal2.exe を解析し`、正しいアドレスにジャンプします。ここが関数の先頭かどうか、アセンブリを確認してください。もし先頭でなければ、メモリ割り当てが変化している可能性があります。その場合はハードコードの一時スクリプトを削除し、エラーメッセージに出ていた複数アドレスの同じ位置を再確認します。

そのアドレスから下方向に約32バイトのメモリを16進数としてコピーし、変動する可能性のあるアドレス部分をワイルドカード `??` に置き換えます。そして、先ほどのスクリプトを次のように修正します：

``` LUA
function Register()
    return "48 89 5C 24 10 48 89 6C 24 18 48 89 74 24 20 57 41 56 41 57 48 81 EC ?? ?? ?? ?? 48 8B 05 ?? ?? ?? ?? 48 33 C4" -- 抽出した16進数シーケンスに置き換える
end

function OnMatchFound(matchAddress)
    return matchAddress -- ハードコードのアドレスを matchAddress に置き換える
end
```

アドレスが見つからない場合 → 変動する可能性のある部分がすべて `??` に置換されているか確認してください。

複数のアドレスが見つかる場合 → シーケンスが短すぎるか、一意でない可能性があります。より長いバイト列を使うか、別のアドレスを基準に間接的に探してください。

安定性を確認するために、再起動や異なる環境でテストしてください。安定した AOB シーケンスを確認できたら、AOB スクリプトとしてコミュニティに公開し、他のユーザーの問題解決に役立てましょう。