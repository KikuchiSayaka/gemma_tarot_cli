# gemma_tarot_cli（Local + Stateful CLI chat bot）

gemma3:1b を Ollama 上で動作させる、完全ローカル・ステートフルな CLI チャットボットです。
このスクリプトは会話履歴を保持し、システムプロンプトによる人格（ペルソナ）制御を行います。
また、オプションで FAISS + sentence-transformers を使った RAG（検索拡張生成）にも対応可能です。

前提条件
Python 3.8 以上

Ollama がインストールされており、gemma3:1b モデルが使用可能であること

（任意）faiss-cpu および sentence-transformers を使った RAG による履歴参照を行いたい場合は追加でインストール

## Installation

```bash
pip install faiss-cpu sentence-transformers
```

RAG（検索拡張生成）機能を有効にしたい場合は、以下のライブラリをインストールしてください。
この機能を利用しない場合はインストール不要です。

```bash
pip install faiss-cpu sentence-transformers
```

※ RAG を使うと、過去の会話履歴や任意のドキュメントから類似情報を検索し、会話の文脈として Gemma に渡すことができます。

## Usage

1. ターミナルで Ollama の Gemma モデルを起動します：

```bash
ollama run gemma3:1b
```

2. 別のターミナルウィンドウでチャットスクリプトを実行します：

```bash
python3 chat_gemma.py
```

3. スクリプトの動作内容：

- history.json に会話履歴を読み込み／初期化
- 会話のたびに履歴を自動保存
- システムプロンプトによって人格（タロット占い師など）を固定
- ステートフルな会話を CLI で実現

4. 会話をリセットしたい場合は、history.json を削除してください。

## Customization

このチャットボットは現在、日本語入力前提であり、タロット占い師として動作するようにシステムプロンプトが設定されています。

他言語で使いたい場合、あるいは別の用途（たとえばコーディング支援、コンサルティング、学習用 AI など）で使いたい場合は、`chat_gemma.py` 内の `SYSTEM_PROMPT` を目的に応じて編集してください。

## Notes

本スクリプトは、http://localhost:11434/api/chat で提供される Ollama のローカル HTTP API にリクエストを送信しています。
この API は OpenAI Chat API に類似した形式（messages 配列と role 指定）を受け付けます。
"stream": false に設定しているため、ストリーム処理の煩雑さがなく簡単に扱えます。
完全にオフラインで動作し、インターネット接続や外部 API アクセスは一切不要です。

## License

This project is licensed under the MIT License.
