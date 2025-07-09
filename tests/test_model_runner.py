# tests/test_model_runner.py
import pytest
from core import model_runner

class MockLlama:
    def __call__(self, prompt, max_tokens, temperature, top_k, stop):
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
