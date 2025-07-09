# core/output_writer.py

from pathlib import Path
from rich.console import Console

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
