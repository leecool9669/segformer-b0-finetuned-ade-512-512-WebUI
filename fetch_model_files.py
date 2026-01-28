# -*- coding: utf-8 -*-
"""从 HuggingFace 模型仓库下载代码文件（不包括大权重文件）到 template"""
import os
import requests
import json
from pathlib import Path

PROXIES = {"http": "http://127.0.0.1:18081", "https": "http://127.0.0.1:18081"}
TIMEOUT = 60
MODEL_ID = "Xenova/segformer-b0-finetuned-ade-512-512"
BASE_URL = "https://hf-mirror.com"
BASE = Path(__file__).resolve().parent

# 需要下载的小文件（不包括 .onnx, .bin, .safetensors 等大文件）
SMALL_FILES = [
    "config.json",
    "preprocessor_config.json",
    "README.md",  # 如果需要原始 README 作为参考
]

def download_file(repo_id, filepath, dest_path):
    """从 HuggingFace 下载单个文件"""
    url = f"{BASE_URL}/{repo_id}/resolve/main/{filepath}"
    try:
        r = requests.get(url, proxies=PROXIES, timeout=TIMEOUT, stream=True)
        r.raise_for_status()
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dest_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"OK: {filepath}")
        return True
    except Exception as e:
        print(f"FAIL {filepath}: {e}")
        return False

def main():
    print(f"从 {MODEL_ID} 下载配置文件...")
    for filename in SMALL_FILES:
        dest = BASE / filename
        if filename == "README.md":
            # 跳过原始 README，我们有自己的版本
            continue
        download_file(MODEL_ID, filename, dest)
    print("完成。")

if __name__ == "__main__":
    main()
