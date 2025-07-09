# tests/test_output_writer.py

from core.output_writer import save_output, save_log
from pathlib import Path
from unittest.mock import patch
import json

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

def test_save_output_handles_exception(tmp_path):
    """
    異常系:
    write_text() が例外を投げた場合に、save_output() が例外を握りつぶすことを確認する。
    """
    dummy_path = tmp_path / "output.txt"
    with patch.object(Path, "write_text", side_effect=IOError("書き込み失敗")):
        save_output("テスト", dummy_path)
    # rich.console の出力はモック対象外（視覚確認または別途検証）

def test_save_log_creates_json(tmp_path):
    """
    正常系:
    save_log() が JSON ファイルを正しく作成し、内容が一致することを検証する。
    """
    prompt = "テストプロンプト"
    config = {"model": "test-model", "temperature": 0.7}
    output = "これは出力です"

    save_log(prompt, config, output, tmp_path)

    log_files = list(tmp_path.glob("log_*.json"))
    assert len(log_files) == 1

    log_data = json.loads(log_files[0].read_text(encoding="utf-8"))
    assert log_data["prompt"] == prompt
    assert log_data["config"] == config
    assert log_data["output"] == output

def test_save_log_handles_exception(tmp_path):
    """
    異常系:
    write_text() が例外を投げた場合に、save_log() が例外を握りつぶすことを確認する。
    """
    with patch("core.output_writer.Path.write_text", side_effect=OSError("保存失敗")):
        save_log("prompt", {"key": "value"}, "output", tmp_path)
