# R-Type Final 2 Modインストールおよび開発ガイド

## Chapter 1.0: R-Type Final 2 Modding の基礎
この章では、*R-Type Final 2* のための *UE4SS* やさまざまな種類のModをインストールする方法を学びます。Mod開発者でもプレイヤーでも、この章の内容は必須です。

本章の内容は、一般的な *Unreal Engine 4* および *Unreal Engine 5* のModdingチュートリアルと共通していますが、*R-Type Final 2* に特化した詳細が含まれています。

- [UE4SSをインストール](Chapter1_TheBasics/ja/UE4SSのインストール.md)
- [UE4SSを手動で注入](Chapter1_TheBasics/ja/手動でUE4SSを注入する.md)
- [ブループリントModのインストール](Chapter1_TheBasics/ja/ブループリントModのインストール.md)
- [PAK Modのインストール](Chapter1_TheBasics/ja/PAKModのインストール.md)
- [LUA Modのインストール](Chapter1_TheBasics/ja/LUAModのインストール.md)
- [Modステージに入る方法](Chapter1_TheBasics/ja/Modステージに入る方法.md)

## Chapter 2.0: R-Type Final 2 のプロジェクト構成
Mod開発の基礎の一部ですが、技術的な内容には深く踏み込んでいません。非開発者でも興味を持って読むことができます。

- [リソースファイルのディレクトリ](Chapter2_0_ProjectStructure/ja/リソースファイルディレクトリ.md)
- [リソースファイルのプレフィックス](Chapter2_0_ProjectStructure/ja/リソースファイルのプレフィックス.md)
- 重要な列挙型
- 重要なデータテーブル
- 重要なランタイムオブジェクト
- UE4SSを使ってランタイムオブジェクトを操作

## Chapter 2.1: クイックリファレンス
この章では、いくつかのデータテーブル、列挙型、関連する内容を挙げており、開発者が必要なIDを素早く検索できるようにしています。

敵の数が多すぎるため、詳細なリストは省略されていますが、この章では敵のIDを特定する方法を紹介します。

- BydoLabの敵画像から敵IDを特定
- ステージリスト
- R戦闘機リスト
- Forceリスト

## Chapter 3.0: Mod開発の一般的な知識
この章からは、第一章のように詳細なステップを説明することはありません。また、他のチュートリアルで既に説明されている内容を繰り返すことはありません。一部のチュートリアルの冒頭には、[ツールリスト] と [スキルリスト] へのリンクがありますので、それに従って必要なツールのダウンロードやスキルの習得を行ってください。

- ツールリスト
- スキルリスト
- [ゲーム内コンソールコマンド](Chapter3_0_DeveBasics/ja/ゲーム内コンソールコマンド.md)

## Chapter 4.0: ブループリントMod
これは、Unreal Engineを十分に活用したModで、Modローダーを使用することで、各ステージの読み込み時にカスタムロジックを持つアクターを生成することができます。

*ブループリントMod* の基礎については、[こちらの古典的なチュートリアル](https://docs.ue4ss.com/dev/feature-overview/blueprint-modloader.html)を参考にしてください。

- [バージョン選択: 4.26.2 か 4.26 Chaosか](Chapter4_0_BPMod/ja/UE4バージョンの選択.md)
- アニメーションブループリントの更新イベントによるクラッシュの解決
- カスタムマテリアルが表示されないかクラッシュする問題の解決
- メモリ不足によるコンパイル問題の解決
- [kismet-analyzerでブループリントを解析](Chapter4_0_BPMod/ja/KismetAnalyzer.md)
- [デリゲートを関数のパラメータとして使用](Chapter4_0_BPMod/ja/デリゲートを関数のパラメータとして使用する.md)

## Chapter 4.1: PAK Mod
*PAK Mod* は、ブループリントModの上位に位置するもので、通常ゲームシステムを拡張する機能はありません。PAK Modには2つのタイプがあります。*UAssetGUI* と *UnrealPak* を使って、ベイクを必要としない *PAK Mod* を作成する方法（通常はデータの修正に使用）と、*Unreal Engine* を使用してベイクが必要な *PAK Mod* を作成する方法（通常は音楽やテクスチャの置き換えに使用）です。

- 例: バックグラウンドミュージックを変更（ベイクが必要）
- 例: 武器データを変更（ベイクが不要）

## Chapter 5.0: ステージMod
この章では、*ステージMod* の一般的な知識について説明します。各*ステージModテンプレート* の詳細については、それぞれのドキュメントを参照してください。

- ステージの読み込みロジック
- ステージの構成
- ステージ初期化ロジック
- CountAsset（スクロールイベント）

## Chapter 5.1: 敵の情報
この章では、ゲームの元々の敵の技術情報を主に紹介し、ステージMod開発者がそれらをステージ内に生成するために役立てられるようにしています。

- [E000_E1940_PowArmor](Chapter5_1_EnemyData/ja/E000_E1940_PowArmor.md)

## 特殊章: 調査中の問題
この章の内容はまだ調査が完了していないため、これらのガイドに従って操作を行っても、期待通りの結果が得られない可能性があります。これらの問題に対する研究ルートが正しいか、問題が解決可能かは不明です。

この章は、同じ問題を調査している他の人々と情報を共有し、協力して解決策を見つけるために存在します。

- [ゲームプロジェクトのミラー作成](/UnderInvestigation/ja/ミラーゲームプロジェクトの作成.md)
