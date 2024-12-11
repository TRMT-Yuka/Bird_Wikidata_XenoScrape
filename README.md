# Bird_Wikidata_XenoScrape

## プロジェクト概要

[Bird Ontology Project](https://github.com/TRMT-Yuka/Bird_ontology_Project)に連なる一連の鳥類マルチモーダル知識BDプロジェクトにおいて，Xeno-cantから収集された追加データを新たに利用した拡張版のマルチモーダル鳥類専用検索知識ベースを提供します．本プロジェクトで取り扱う鳥類のデータは，Wikidataエンティティ（例: [Wikidata: Q5113](https://www.wikidata.org/wiki/Q5113)）より下位に位置するすべてのエンティティに対し，それに対応するXeno-cantoの固有IDを抽出し，Xeno-cantoデータベースから取得した大規模な鳥類音声データを統合しています．本リポジトリでは，該当する音声データの取得のためのスクレイピングコード，フォーマット変換を含むデータ処理のためのコードを提供します．

## ファイル構成

### ディレクトリ構造

```
.
├── protected_data/        # 生成後の中間ファイル保護用のディレクトリ
├── wav_model_data/        # WAVモデル関連のデータ
├── 01_download_mp3.ipynb  # 音声データのダウンロードスクリプト
├── 02_make_wav_data.ipynb # 音声データの変換スクリプト
├── code_recipe_240929.ipynb # その他のコードサンプル
├── mymodule.py            # カスタムPythonモジュール
├── README.md              # プロジェクト概要（このファイル）
└── XenoScraping.py      # Xeno-cantoデータスクレイピング用スクリプト
```

### 主なファイルとディレクトリの説明

#### `01_download_mp3.ipynb`

- **概要**: WikidataのSPARQLエンドポイントを利用して特定のエンティティに対応するデータを取得．
- **主な機能**:
  - SPARQLクエリの実行によるエンティティの検索
  - Xeno-canto固有IDの抽出とリスト化
  - Xeno-canto APIを活用し，音声ファイル（MP3形式）を最大最新100件ダウンロード

#### `02_make_wav_data.ipynb`

- **概要**: 収集した音声ファイルの整合性を確認し，研究用途で扱いやすいWAV形式へ変換．
- **主な機能**:
  - ダウンロード済みファイルの重複・破損といった状態確認
  - 音声データから空白部分（無音区間）を除去，60秒の長さにクリップ
  - MP3からWAVへの高精度変換（音質を保ちながらのリサンプリングを含む）

#### `XenoScraping.py`

- **概要**: 本プロジェクトで汎用的に使用する関数をまとめた自作モジュール．主にXeno-cantoデータベースから効率的に音声データを取得する機能を提供．
- **主な機能**:
  - APIリクエストの最適化（リトライ機能やリクエスト間隔調整を含む）
  - スクレイピングしたデータの構造化およびローカル保存

#### `mymodule.py`

- **概要**: TRMT-Yukaが頻繁に利用する自作モジュール
- **主な機能**:
  - データ変換・保存やファイル処理の補助機能

## 使用方法

1. このリポジトリをクローン

   ```bash
   git clone https://github.com/your-repository.git
   cd your-repository
   ```

2. 必要なPythonライブラリをインストール

   ```bash
   pip install -r requirements.txt
   ```

3. 各Notebookを順番に実行します。

   - `01_download_mp3.ipynb`: 必要な音声データをダウンロード
   - `02_make_wav_data.ipynb`: ダウンロードしたファイルを確認し形式を変換
  
なおデータは別で公開予定

## 環境

- Python 3.12.4により動作確認
- 必須ライブラリ：`requirements.txt`

## 注意事項

- WikiData，Xeno-cantoの利用規約を要確認

