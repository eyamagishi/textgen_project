# 🤝 貢献ガイド（Contributing Guide）

このプロジェクトへのご関心ありがとうございます！  
以下のガイドラインに従っていただくことで、円滑なコラボレーションが可能になります。

---

## 🛠️ 貢献の方法

### 1. Issue を確認する
- バグ報告や機能要望は、まず [Issues]([../../issues](https://github.com/eyamagishi/textgen_project/issues)) を確認してください。
- 新しい提案がある場合は、重複していないか確認のうえ新規 Issue を作成してください。

### 2. フォークしてブランチを作成
```bash
git checkout -b feature/your-feature-name
```

### 3. コードを変更・追加
- `core/` 以下に機能を追加する場合は、単一責任の原則を意識してください。
- `config.yaml` を変更する場合は、共有用と個人用（`config.local.yaml`）を分けてください。

### 4. テストと確認
- 変更が他の機能に影響しないか確認してください。
- 出力ファイルやログが `.gitignore` に含まれていることを確認してください。

### 5. Pull Request を作成
- `main` ブランチへの直接 push はできません。必ず Pull Request を作成してください。
- PR テンプレートに従って、目的・変更点・確認方法を明記してください。
- コミットメッセージは明確かつ簡潔に記述してください（例：`fix: 出力ファイル名の重複を修正`）

---

## 🧪 開発環境のセットアップ

```bash
git https://github.com/eyamagishi/textgen_project.git
cd textgen_project
python -m venv venv
source venv/bin/activate  # Windows の場合は venv\Scripts\activate
pip install -r requirements.txt
```

---

## 📄 ライセンス

このプロジェクトは [MIT License](./LICENSE) のもとで公開されています。  
貢献いただいた内容も同ライセンスのもとで公開されます。

---

ご協力ありがとうございます！🚀
