# tests/test_prompt_loader.py

import pytest
from pathlib import Path
from core.prompt_loader import load_prompt

def test_load_prompt_returns_str(tmp_path):
    """
    正常系:
    一時的に作成したプロンプトファイルを読み込み、
    load_prompt() が文字列を返し、内容が正しく整形されていることを検証する。
    """
    prompt_file = tmp_path / "prompt.txt"
    prompt_file.write_text("これはテスト用のプロンプトです。\n")

    result = load_prompt(prompt_file)
    assert isinstance(result, str)
    assert result == "これはテスト用のプロンプトです。"

def test_load_prompt_file_not_found():
    """
    異常系:
    存在しないプロンプトファイルを指定した場合に、
    load_prompt() が FileNotFoundError を発生させることを確認する。
    """
    with pytest.raises(FileNotFoundError):
        load_prompt(Path("nonexistent_prompt.txt"))
