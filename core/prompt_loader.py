# core/prompt_loader.py

from pathlib import Path
from rich.console import Console

console = Console()

def load_prompt(path: Path) -> str:
    """
    プロンプトファイルを読み込みます。
    """
    if not path.exists():
        console.print(f"[red]❌ プロンプトファイルが見つかりません: {path}[/red]")
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8").strip()
