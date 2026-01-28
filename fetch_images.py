# -*- coding: utf-8 -*-
"""下载 SegFormer 模型页面相关图片到 template 目录"""
import os
import requests
from pathlib import Path

PROXIES = {"http": "http://127.0.0.1:18081", "https": "http://127.0.0.1:18081"}
TIMEOUT = 60

BASE = Path(__file__).resolve().parent
os.makedirs(BASE / "images", exist_ok=True)

URLS = [
    ("https://cdn-thumbnails.hf-mirror.com/social-thumbnails/models/Xenova/segformer-b0-finetuned-ade-512-512.png", "images/segformer-b0-finetuned-ade-512-512_model_page.png"),
    ("https://cdn-thumbnails.hf-mirror.com/social-thumbnails/models/Xenova/segformer-b0-finetuned-ade-512-512.png", "images/segformer-b0-finetuned-ade-512-512_thumbnail.png"),
]

def main():
    for url, rel_path in URLS:
        path = BASE / rel_path
        try:
            r = requests.get(url, proxies=PROXIES, timeout=TIMEOUT)
            r.raise_for_status()
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "wb") as f:
                f.write(r.content)
            print(f"OK: {rel_path}")
        except Exception as e:
            print(f"FAIL {url}: {e}")

if __name__ == "__main__":
    main()
