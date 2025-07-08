# main.py

import yaml
from llama_cpp import Llama
from utils.tokenizer import load_prompt

# 設定読み込み
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# モデル初期化
llm = Llama(
    model_path=config["model_path"],
    n_ctx=config["context_length"],
    n_threads=config["threads"]
)

# プロンプト読み込み
prompt = load_prompt("prompts/story.txt")

# テキスト生成
print("🧠 モデル読み込み完了。プロンプトを送信中...")
output = llm(
    prompt,
    max_tokens=config["max_tokens"],
    temperature=config["temperature"],
    top_k=config["top_k"]
)
print("✅ 応答生成完了")
print(output["choices"][0]["text"])

print("📝 生成結果:\n", output["choices"][0]["text"])
