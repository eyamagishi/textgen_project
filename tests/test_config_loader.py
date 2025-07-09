# tests/test_config_loader.py

# === 標準ライブラリ ===
from pathlib import Path

# === サードパーティライブラリ ===
import pytest

# === ローカルモジュール ===
from core.config_loader import load_config

def test_load_config_returns_dict(tmp_path):
    """
    正常系:
    一時的に作成したYAML形式の設定ファイルを読み込み、
    load_config() が正しく辞書を返すことを検証する。
    """
    config_file = tmp_path / "test_config.yaml"
    config_file.write_text("model_path: models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf\nrepeat_penalty: 1.2")

    config = load_config(config_file)
    assert isinstance(config, dict)
    assert config["model_path"] == "models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf"
    assert config["repeat_penalty"] == 1.2

def test_load_config_file_not_found():
    """
    異常系:
    存在しない設定ファイルを指定した場合に、
    load_config() が FileNotFoundError を発生させることを確認する。
    """
    with pytest.raises(FileNotFoundError):
        load_config(Path("nonexistent_config.yaml"))
