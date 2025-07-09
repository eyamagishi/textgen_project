# tests/test_model_runner.py

# === 標準ライブラリ ===
# （このファイルでは標準ライブラリは使用していません）

# === サードパーティライブラリ ===
import pytest
from unittest.mock import patch

# === ローカルモジュール ===
from core import model_runner

class MockLlama:
    def __call__(self, prompt, max_tokens, temperature, top_k, stop):
        """
        モデルの代替として使用されるモッククラス。
        呼び出し時に引数の型を検証し、固定の応答を返す。
        """
        assert isinstance(prompt, str)
        assert isinstance(max_tokens, int)
        assert isinstance(temperature, float)
        assert isinstance(top_k, int)
        assert isinstance(stop, list)
        return {
            "choices": [
                {"text": f"Mocked response to: {prompt}"}
            ]
        }

def test_generate_response_with_mock_llama_returns_expected_text():
    """
    正常系:
    モックLlamaを使って generate_response() を呼び出し、
    期待される文字列が返されることを検証する。
    """
    mock_llm = MockLlama()
    prompt = "こんにちは、AIさん。"
    config = {
        "max_tokens": 32,
        "temperature": 0.7,
        "top_k": 40
    }

    result = model_runner.generate_response(mock_llm, prompt, config)
    expected = "Mocked response to: こんにちは、AIさん。"
    assert result == expected

def test_initialize_model_calls_llama_with_expected_args():
    """
    正常系:
    initialize_model() が Llama を正しい引数で初期化することを検証する。
    """
    config = {
        "model_path": "models/mock.gguf",
        "context_length": 256,
        "threads": 4
    }

    with patch("core.model_runner.Llama") as MockLlama:
        model_runner.initialize_model(config)
        MockLlama.assert_called_once_with(
            model_path="models/mock.gguf",
            n_ctx=256,
            n_threads=4,
            verbose=False
        )

def test_generate_response_raises_keyerror_if_choices_missing():
    """
    異常系:
    モデル出力に 'choices' キーが存在しない場合に KeyError が発生することを確認する。
    """
    class BrokenLlama:
        def __call__(self, *args, **kwargs):
            return {"unexpected": "structure"}

    with pytest.raises(KeyError):
        model_runner.generate_response(BrokenLlama(), "テスト", {})
