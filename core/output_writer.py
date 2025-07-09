# core/output_writer.py

# === 標準ライブラリ ===
import json
from pathlib import Path
from datetime import datetime

# === サードパーティライブラリ ===
from rich.console import Console

# === ローカルモジュール ===

console = Console()

def save_output(text: str, path: Path) -> None:
    """
    出力テキストをファイルに保存します。
    """
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        console.print(f"💾 出力を保存しました: [green]{path}[/green]")
    except Exception as e:
        console.print(f"[yellow]⚠️ 出力の保存に失敗しました: {e}[/yellow]")

def save_log(prompt: str, config: dict, output: str, log_dir: Path) -> None:
    """
    実行時のプロンプト・設定・出力をJSON形式でログとして保存します。
    """
    try:
        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_path = log_dir / f"log_{timestamp}.json"

        log_data = {
            "timestamp": timestamp,
            "prompt": prompt,
            "config": config,
            "output": output
        }

        log_path.write_text(json.dumps(log_data, ensure_ascii=False, indent=2), encoding="utf-8")
        console.print(f"📝 ログを保存しました: [green]{log_path}[/green]")
    except Exception as e:
        console.print(f"[yellow]⚠️ ログの保存に失敗しました: {e}[/yellow]")
