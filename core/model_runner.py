# core/model_runner.py

import time
from rich.console import Console
from rich.progress import track
from llama_cpp import Llama

console = Console()

def initialize_model(config: dict) -> Llama:
    """
    Llamaモデルを初期化します。
    """
    console.print("📦 モデルを準備中...", style="yellow")
    for _ in track(range(10), description="🔧 モデル初期化中..."):
        time.sleep(0.02)

    return Llama(
        model_path=config["model_path"],
        n_ctx=config.get("context_length", 512),
        n_threads=config.get("threads", 2),
        verbose=False
    )

def generate_response(llm: Llama, prompt: str, config: dict) -> str:
    """
    モデルにプロンプトを与えて応答を生成します。
    """
    console.print("🧠 応答を生成中...", style="cyan")
    output = llm(
        prompt,
        max_tokens=config.get("max_tokens", 32),
        temperature=config.get("temperature", 0.7),
        top_k=config.get("top_k", 40),
        stop=["</s>"]
    )
    return output["choices"][0]["text"].strip()
