# tests/test_prompt_loader.py

import pytest
from pathlib import Path
from core.prompt_loader import load_prompt

def test_load_prompt_returns_str(tmp_path):
    # 一時的なプロンプトファイルを作成
    prompt_file = tmp_path / "prompt.txt"
    prompt_file.write_text("これはテスト用のプロンプトです。\n")

    result = load_prompt(prompt_file)
    assert isinstance(result, str)
    assert result == "これはテスト用のプロンプトです。"

def test_load_prompt_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_prompt(Path("nonexistent_prompt.txt"))
