# core/config_loader.py

from pathlib import Path
import yaml
from rich.console import Console

console = Console()

def load_config(path: Path) -> dict:
    """
    YAML形式の設定ファイルを読み込みます。
    """
    if not path.exists():
        console.print(f"[red]❌ 設定ファイルが見つかりません: {path}[/red]")
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)
