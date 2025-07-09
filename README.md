# 🧠 Local Text Generation with GGUF Models

![Coverage](https://codecov.io/gh/eyamagishi/textgen_project/branch/main/graph/badge.svg)
![CI](https://github.com/eyamagishi/textgen_project/actions/workflows/test.yml/badge.svg)
![Lint](https://github.com/eyamagishi/textgen_project/actions/workflows/lint.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![LLM](https://img.shields.io/badge/LLM-GGUF%20%2F%20llama.cpp-orange)

このプロジェクトは、`llama.cpp` ベースのローカルLLM（例：TinyLlama, Mistral）を使用して、プロンプトに対する自然なテキスト生成を行うPythonアプリケーションです。

## 🚀 特徴

- ✅ ローカルで高速に動作（インターネット不要）
- ✅ `config.yaml` による柔軟なモデル設定
- ✅ `rich` による視認性の高い出力
- ✅ モジュール分割された構造で保守性・拡張性が高い
- ✅ 出力は `outputs/` に自動保存（ディレクトリも自動作成）

## 📁 ディレクトリ構成

```
textgen_project/
├── main.py                  # 実行エントリーポイント
├── config.yaml              # モデル設定ファイル
├── prompts/                 # プロンプトファイル格納
│   └── story.txt
├── outputs/                 # 生成結果の保存先
│   └── output.txt
├── models/                  # GGUFモデル格納
│   └── *.gguf
├── core/                    # モジュール群（設定・生成・保存）
│   ├── config_loader.py
│   ├── prompt_loader.py
│   ├── model_runner.py
│   └── output_writer.py
├── requirements.txt         # 必要なパッケージ
└── README.md                # このファイル
```

## ⚙️ セットアップ

### 1. 仮想環境の作成（任意）

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 依存ライブラリのインストール

```bash
pip install -r requirements.txt
```

### 3. モデルのダウンロード（例）

```bash
python download_model.py
```

## 🧪 実行方法

```bash
python main.py
```

出力は `outputs/output.txt` に保存されます。

## 🛠️ 設定ファイル（config.yaml）

```yaml
model_path: models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf
context_length: 512
threads: 2
max_tokens: 32
temperature: 0.7
top_k: 40
```

## 📌 今後の拡張予定（例）

- [ ] CLI引数対応（`--prompt`, `--output`, `--config`）
- [ ] stream=True によるリアルタイム出力
- [ ] チャット形式への拡張
- [ ] テストスイートの導入（pytest）

## 📄 ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。  
詳細は [LICENSE](./LICENSE) ファイルをご確認ください。

## 🤝 貢献

このプロジェクトへの貢献を歓迎します！

### 🔍 Issue を確認する

- バグ報告や機能提案を行う前に、[Issues](https://github.com/eyamagishi/textgen-project/issues) を確認してください。
- 既に同様のIssueが存在する場合は、そのスレッドにコメントを追加してください。
- 該当するIssueがない場合は、新しいIssueを作成してから作業を始めてください。

### 🛠️ 貢献の流れ

1. リポジトリをフォーク
2. 新しいブランチを作成（例：`feature/add-cli-support`）
3. コードを変更・テスト
4. Pull Request を作成（テンプレートに従って記述）

詳しくは [CONTRIBUTING.md](./CONTRIBUTING.md) をご覧ください。

## 🙏 謝辞

このプロジェクトは、Microsoft Copilot の支援を受けて設計・実装されています。  
設計のアドバイス、コードの生成、ドキュメントの整備などにおいて、Copilot の提案を積極的に活用しています。
