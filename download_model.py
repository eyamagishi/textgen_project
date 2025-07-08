# download_model.py

from huggingface_hub import hf_hub_download
import os

# 保存先ディレクトリ
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# ダウンロード対象
REPO_ID = "TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF"
FILENAME = "tinyllama-1.1b-chat-v1.0.Q4_0.gguf"

# ダウンロード実行
print(f"📥 Downloading {FILENAME} from {REPO_ID}...")
model_path = hf_hub_download(
    repo_id=REPO_ID,
    filename=FILENAME,
    local_dir=MODEL_DIR,
    local_dir_use_symlinks=False
)

print(f"✅ Download complete: {model_path}")
