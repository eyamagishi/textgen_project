# main.py

import yaml
from llama_cpp import Llama
from rich.console import Console
from rich.table import Table
from rich.progress import track
from pathlib import Path
import time

# === Rich Console 初期化 ===
console = Console()

# === 設定ファイルの読み込み ===
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# === 設定の表示 ===
table = Table(title="🛠️ Model Configuration")
table.add_column("Parameter", style="cyan", no_wrap=True)
table.add_column("Value", style="magenta")

for key, value in config.items():
    table.add_row(str(key), str(value))
console.print(table)

# === プロンプトの読み込み ===
prompt_path = Path("prompts/story.txt")
if not prompt_path.exists():
    console.print(f"[red]❌ プロンプトファイルが見つかりません: {prompt_path}[/red]")
    exit(1)

prompt = prompt_path.read_text(encoding="utf-8").strip()
console.rule("[bold cyan]📝 プロンプト")
console.print(prompt, style="white on black")

# === モデルの読み込み（進捗バー付き） ===
console.print("📦 モデルを準備中...", style="yellow")
for _ in track(range(10), description="🔧 モデル初期化中..."):
    time.sleep(0.05)  # 実際の初期化処理に置き換え可能

llm = Llama(
    model_path=config["model_path"],
    n_ctx=config.get("context_length", 512),
    n_threads=config.get("threads", 2),
    verbose=False
)
console.print("✅ モデル読み込み完了", style="green")

# === 応答生成 ===
console.print("🧠 応答を生成中...", style="cyan")
output = llm(
    prompt,
    max_tokens=config.get("max_tokens", 32),
    temperature=config.get("temperature", 0.7),
    top_k=config.get("top_k", 40),
    stop=["</s>"]
)

# === 出力の表示 ===
console.rule("[bold green]📤 生成結果")
generated_text = output["choices"][0]["text"].strip()
console.print(generated_text, style="bold white")

# === 出力をファイルに保存 ===
output_path = Path("output.txt")
output_path.write_text(generated_text, encoding="utf-8")
console.print(f"💾 出力を保存しました: [green]{output_path}[/green]")
