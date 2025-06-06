# Usage
# ollama run gemma3:1b でモデルを起動しておくこと
# sentence-transformers × FAISS or nomic-embed-textで埋め込み＋類似検索 を行うためにfassとtransformersをインストール
# pip install faiss-cpu sentence-transformers
# Ollamaを動かしたのと違うターミナルウインドウでpython3 chat_gemma.py


import os
import json
import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "gemma3:1b"
HISTORY_FILE = "history.json"
SYSTEM_PROMPT = """
あなたは心理テスト分析の専門家であり、タロットカードの引き結果を客観的かつ構造的に分析する役割です。
依頼者の質問に対して3枚のカードを引き、各カードの名前・向き（正位置 or 逆位置）・意味を簡潔に説明し、全体としての分析結果を明確に述べてください。
あなたは、質問を受けたら即座に3枚のタロットカードを引きます。
依頼者の状況や詳細な説明は不要です。常に以下の形式で答えてください。

1. カード名（向き）：意味（簡潔に1行程度）
2. カード名（向き）：意味
3. カード名（向き）：意味

→ 全体の解釈（2〜3文で明快にまとめる）

質問の内容に関わらず、毎回3枚引いてこの構造で返答してください。
感情的な語りや「状況を教えてください」などの返答は行わないでください。
出力は番号付きで構造化し、冗長な表現や沈黙を避けてください。
"""


# 履歴読み込み or 初期化
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("🧠 Gemmaチャット開始（CTRL+Cで終了）")

try:
    while True:
        user_input = input("👤 あなた> ")
        history.append({"role": "user", "content": user_input})

        res = requests.post(
            "http://localhost:11434/api/chat",
            json={
                "model": MODEL,
                "messages": history,
                "stream": False,
            },
        )

        reply = res.json()["message"]["content"]
        print(f"🤖 Gemma> {reply}\n")

        history.append({"role": "assistant", "content": reply})

        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            json.dump(history, f, ensure_ascii=False, indent=2)

except KeyboardInterrupt:
    print("\n💾 終了：履歴を保存しました。")
