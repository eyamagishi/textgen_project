# main.py

import yaml
from llama_cpp import Llama
from rich.console import Console
from rich.table import Table
from rich.progress import track
from pathlib import Path
import time
import sys

# === 初期化 ===
console = Console()
CONFIG_PATH = Path("config.yaml")
PROMPT_PATH = Path("prompts/story.txt")
OUTPUT_PATH = Path("output.txt")

def load_config(path: Path) -> dict:
    """
    指定されたYAMLファイルから設定を読み込みます。

    引数:
        path (Path): 設定ファイルのパス

    戻り値:
        dict: 読み込まれた設定の辞書

    例外:
        SystemExit: ファイルが存在しない場合や読み込みに失敗した場合
    """
    if not path.exists():
        console.print(f"[red]❌ 設定ファイルが見つかりません: {path}[/red]")
        sys.exit(1)

    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def display_config(config: dict) -> None:
    """
    設定内容をテーブル形式でコンソールに表示します。

    引数:
        config (dict): 表示する設定の辞書
    """
    table = Table(title="🛠️ モデル設定")
    table.add_column("パラメータ", style="cyan", no_wrap=True)
    table.add_column("値", style="magenta")
    for key, value in config.items():
        table.add_row(str(key), str(value))
    console.print(table)

def load_prompt(path: Path) -> str:
    """
    指定されたファイルからプロンプトを読み込みます。

    引数:
        path (Path): プロンプトファイルのパス

    戻り値:
        str: 読み込まれたプロンプト文字列

    例外:
        SystemExit: ファイルが存在しない場合
    """
    if not path.exists():
        console.print(f"[red]❌ プロンプトファイルが見つかりません: {path}[/red]")
        sys.exit(1)

    return path.read_text(encoding="utf-8").strip()

def initialize_model(config: dict) -> Llama:
    """
    設定に基づいて Llama モデルを初期化します。

    引数:
        config (dict): モデル初期化に使用する設定辞書

    戻り値:
        Llama: 初期化された Llama モデルインスタンス

    例外:
        SystemExit: モデルの読み込みに失敗した場合
    """
    console.print("📦 モデルを準備中...", style="yellow")
    for _ in track(range(10), description="🔧 モデル初期化中..."):
        time.sleep(0.02)

    try:
        return Llama(
            model_path=config["model_path"],
            n_ctx=config.get("context_length", 512),
            n_threads=config.get("threads", 2),
            verbose=False
        )
    except Exception as e:
        console.print(f"[red]❌ モデルの読み込みに失敗しました: {e}[/red]")
        sys.exit(1)

def generate_response(llm: Llama, prompt: str, config: dict) -> str:
    """
    モデルにプロンプトを与えて応答を生成します。

    引数:
        llm (Llama): 初期化済みの Llama モデル
        prompt (str): 入力プロンプト
        config (dict): 生成パラメータを含む設定辞書

    戻り値:
        str: 生成された応答テキスト

    例外:
        SystemExit: 応答生成に失敗した場合
    """
    console.print("🧠 応答を生成中...", style="cyan")
    try:
        output = llm(
            prompt,
            max_tokens=config.get("max_tokens", 32),
            temperature=config.get("temperature", 0.7),
            top_k=config.get("top_k", 40),
            stop=["</s>"]
        )
        return output["choices"][0]["text"].strip()
    except Exception as e:
        console.print(f"[red]❌ 応答生成中にエラーが発生しました: {e}[/red]")
        sys.exit(1)

def save_output(text: str, path: Path) -> None:
    """
    生成されたテキストをファイルに保存します。

    引数:
        text (str): 保存するテキスト
        path (Path): 保存先のファイルパス
    """
    try:
        path.write_text(text, encoding="utf-8")
        console.print(f"💾 出力を保存しました: [green]{path}[/green]")
    except Exception as e:
        console.print(f"[yellow]⚠️ 出力の保存に失敗しました: {e}[/yellow]")

def main():
    """
    テキスト生成パイプラインのメイン処理を実行します。
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
