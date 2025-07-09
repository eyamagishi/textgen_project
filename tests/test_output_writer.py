# tests/test_output_writer.py

from core.output_writer import save_output
from pathlib import Path

def test_save_output_creates_file(tmp_path):
    """
    正常系:
    save_output() を使って指定されたパスにファイルを保存し、
    ファイルが存在し、内容が一致することを検証する。
    """
    output_path = tmp_path / "output.txt"
    content = "これはテスト出力です。"

    save_output(content, output_path)

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == content
