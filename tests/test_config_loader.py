# tests/test_config_loader.py

import pytest
from pathlib import Path
from core.config_loader import load_config

def test_load_config_returns_dict(tmp_path):
    # テスト用のYAMLファイルを作成
    config_file = tmp_path / "test_config.yaml"
    config_file.write_text("model_path: models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf\nrepeat_penalty: 1.2")

    config = load_config(config_file)
    assert isinstance(config, dict)
    assert config["model_path"] == "models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf"
    assert config["repeat_penalty"] == 1.2

def test_load_config_file_not_found():
    with pytest.raises(FileNotFoundError):
        load_config(Path("nonexistent_config.yaml"))
