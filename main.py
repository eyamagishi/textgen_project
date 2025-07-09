# main.py

# === 標準ライブラリ ===
from pathlib import Path

# === サードパーティライブラリ ===
from rich.console import Console
from rich.table import Table

# === ローカルモジュール ===
from core.config_loader import load_config
from core.prompt_loader import load_prompt
from core.model_runner import initialize_model, generate_response
from core.output_writer import save_output

console = Console()

CONFIG_PATH = Path("config.yaml")
PROMPT_PATH = Path("prompts/story.txt")
OUTPUT_PATH = Path("outputs/output.txt")

def display_config(config: dict) -> None:
    """
    設定内容をテーブル形式で表示します。
    """
    table = Table(title="🛠️ モデル設定")
    table.add_column("パラメータ", style="cyan", no_wrap=True)
    table.add_column("値", style="magenta")
    for key, value in config.items():
        table.add_row(str(key), str(value))
    console.print(table)

def main():
    """
    テキスト生成パイプラインのメイン処理。
    """
    config = load_config(CONFIG_PATH)
    display_config(config)

    prompt = load_prompt(PROMPT_PATH)
    console.rule("[bold cyan]📝 プロンプト")
    console.print(prompt, style="white on black")

    llm = initialize_model(config)
    response = generate_response(llm, prompt, config)

    console.rule("[bold green]📤 生成結果")
    console.print(response, style="bold white")

    save_output(response, OUTPUT_PATH)

if __name__ == "__main__":
    main()
