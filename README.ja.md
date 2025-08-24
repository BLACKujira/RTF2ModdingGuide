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
- [セーブデータのバックアップ](Chapter1_TheBasics/ja/セーブデータのバックアップ.md)

## Chapter 2.0: R-Type Final 2 のアンパック

通常、ゲームのアンパックはMod開発の第一歩です。ほとんどの *UE4/5* ゲームにおいて、 [FModel](https://github.com/iAmAsval/FModel/) はリソースの閲覧・抽出ツールとして最適で、*R-Type Final 2* も例外ではありません。ただし、開発時の設定により、アンパックには *AESキー* と *.usmap マッピングファイル* が必要です。

- [AESキーと.usmapマッピングファイルの取得](Chapter2_0_Unpack/ja/AESキーとusmapの取得.md)
- [FModelを使ってゲームリソースを閲覧・抽出](Chapter2_0_Unpack/ja/FModelによるリソース抽出.md)

## Chapter 2.1: R-Type Final 2 のプロジェクト構成

これはMod開発の基本の一つであり、ゲーム内部の構成を簡単に紹介しています。

- [リソースファイルのディレクトリ](Chapter2_1_ProjectStructure/ja/リソースファイルディレクトリ.md)
- [リソースファイルのプレフィックス](Chapter2_1_ProjectStructure/ja/リソースファイルのプレフィックス.md)
- [重要な列挙型](Chapter2_1_ProjectStructure/ja/重要な列挙型.md)
- [重要なデータテーブル](Chapter2_1_ProjectStructure/ja/重要なデータテーブル.md)
- [重要なランタイムオブジェクト](Chapter2_1_ProjectStructure/ja/重要なランタイムオブジェクト.md)

## Chapter 2.2: クイックリファレンス

この章では、いくつかのデータテーブルや列挙型、関連情報をリストアップしており、開発者が必要なIDをすぐに見つけられるようにしています。

敵の数が非常に多いため、すべてを詳細に列挙することはしていませんが、敵のIDを特定する方法については解説します。

- [BydoLabの敵画像から敵IDを特定](Chapter2_2_QuickReference/ja/BydoLabの画像で敵IDを特定.md)
- [ステージリスト](Chapter2_2_QuickReference/ja/ステージリスト.md)
- [R戦闘機リスト](Chapter2_2_QuickReference/ja/R戦闘機リスト.md)
- Forceリスト


## Chapter 3.0: Mod開発の一般的な知識

この章からは、第一章のように各ステップを詳細に解説することはせず、すでに他のチュートリアルで解説されている内容を繰り返すこともありません。一部のチュートリアルでは [ツールリスト] への参照がありますので、必要なツールのダウンロードやスキルの習得にはそちらをご確認ください。

- [ツールリスト](Chapter3_0_DeveBasics/ja/ツールリスト.md)
- [記事・コミュニティ](Chapter3_0_DeveBasics/ja/記事とコミュニティ.md)
- [ゲーム内コンソールコマンド](Chapter3_0_DeveBasics/ja/ゲーム内コンソールコマンド.md)

## Chapter 4.0: ブループリントMod

これは、Unreal Engine の機能を活かした人気のある Mod の形式で、Modローダーを使用することで、各ステージのロード時にカスタムロジックを持つ Actor を自動的に生成できます。

初心者の方は、まず [この定番チュートリアル](https://docs.ue4ss.com/dev/feature-overview/blueprint-modloader.html) を参考に、「Modが読み込まれました」と表示するシンプルな *ブループリントMod* を作成してみましょう。その後、より複雑なロジックを追加することができます。

- ブループリントMod開発の基本フロー
- [バージョン選択: 4.26.2 または 4.26 Chaos](Chapter4_0_BPMod/ja/UE4バージョンの選択.md)
- [アニメーションブループリント更新イベントによるクラッシュの回避](Chapter4_0_BPMod/ja/アニメーションBPクラッシュ回避.md)
- [カスタムマテリアルが表示されない・クラッシュする問題の解決](Chapter4_0_BPMod/ja/カスタムマテリアル問題の解決.md)
- メモリ不足によるコンパイルエラーの解決
- [kismet-analyzer でブループリントを解析](Chapter4_0_BPMod/ja/KismetAnalyzer.md)
- [デリゲートを関数の引数として使用](Chapter4_0_BPMod/ja/デリゲートを関数のパラメータとして使用する.md)

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

- [E000_PowArmor](Chapter5_1_EnemyData/ja/E000_PowArmor.md)

## 特別章：R-Type Tactics II のアンパック

リマスター版 *R-Type Tactics I & II Cosmos* がまもなく発売されるため、より高精細なデータを簡単に抽出できる方法が登場する可能性があります。したがって、この章の内容は将来的にあまり重要ではなくなるかもしれません。

- [メインリソースファイルのアンパック](EX_UnpackRTT2/ja/メインリソースファイルのアンパック.md)
- [リソースパック方式の分析](EX_UnpackRTT2/ja/リソースパック方式の分析.md)
- [Photoshopを使ってノーマルマップを生成する](EX_UnpackRTT2/ja/Photoshopでノーマルマップを生成.md)
- [PPSSPPを使ってテクスチャを抽出する](EX_UnpackRTT2/ja/PPSSPPでテクスチャを抽出.md)

## 特殊章: 調査中の問題
この章の内容はまだ調査が完了していないため、これらのガイドに従って操作を行っても、期待通りの結果が得られない可能性があります。これらの問題に対する研究ルートが正しいか、問題が解決可能かは不明です。

この章は、同じ問題を調査している他の人々と情報を共有し、協力して解決策を見つけるために存在します。

- [ゲームプロジェクトのミラー作成](EX_UnderInvestigation/ja/ミラーゲームプロジェクトの作成.md)

## 特殊章：Mod基盤整備
この章では、一度誰かが作成すればコミュニティ全体で利用できるリソースの作成方法を紹介します。例としては、*UE4SS* の AOB シグネチャスキャンスクリプトや Mod テンプレートなどがあります。

- [Writing AOB Scripts](EX_ModInfrastructure/ja/AOBスクリプトの作成.md)
