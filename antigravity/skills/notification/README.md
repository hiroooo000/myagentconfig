# Discord通知スキル - セットアップガイド

Antigravityのユーザー通知をDiscordへ送信するスキルです。このドキュメントでは、環境セットアップから使用方法まで、詳細な手順を説明します。

## 📋 目次

1. [概要](#概要)
2. [環境セットアップ](#環境セットアップ)
3. [使用方法](#使用方法)
4. [トラブルシューティング](#トラブルシューティング)
5. [技術仕様](#技術仕様)

---

## 概要

### 機能
- Discord WebhookへのメッセージPOST
- コマンドライン引数によるメッセージ送信
- Pythonプログラムからの呼び出し対応
- エラー時の全員メンション機能(`@everyone`)

### 前提条件
- Python 3.7以上
- インターネット接続
- DiscordチャンネルへのWebhook作成権限

---

## 環境セットアップ

### ステップ1: Python環境の確認

(変更なし)

### ステップ2: pipのインストール(必要な場合)

(変更なし)

### ステップ3: 依存ライブラリのインストール

(変更なし)

### ステップ4: Discord Webhook URLの取得

DiscordチャンネルにWebhookを設定し、URLを取得します。

#### 4-1. チャンネル設定を開く
1. Discordで通知を送信したいチャンネルの「チャンネルの編集」(歯車アイコン)をクリック
2. 左メニューから **連携サービス (Integrations)** を選択

#### 4-2. Webhookを作成
1. **ウェブフック (Webhooks)** を選択
2. **新しいウェブフック (New Webhook)** をクリック
3. 名前を変更(例: `Antigravity通知`)
4. **ウェブフックURLをコピー (Copy Webhook URL)** をクリック

**Webhook URLの形式**:
```
https://discord.com/api/webhooks/123456789.../abcdefg...
```

> [!IMPORTANT]
> このURLは機密情報です。他人と共有したり、公開リポジトリにコミットしないでください。

### ステップ5: 環境変数の設定

#### 5-1. `.env`ファイルの作成

スキルディレクトリに移動し、`.env.example`をコピーして`.env`を作成します。

```bash
cd /home/node/myagentflow/antigravity/skills/notification
cp .env.example .env
```

#### 5-2. Webhook URLの設定

`.env`ファイルをエディタで開き、Webhook URLを設定します。

```bash
# エディタで開く(例: nano)
nano .env
```

以下のように記述します:

```env
NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
```

> [!WARNING]
> - URLは必ず**ダブルクォート(`"`)で囲んでください**
> - `=`の前後にスペースを入れないでください
> - ステップ4で取得したURL全体をコピーしてください

保存して閉じます(nanoの場合: `Ctrl+O` → `Enter` → `Ctrl+X`)

#### 5-3. 設定の確認

`.env`ファイルが正しく作成されたか確認します。

```bash
cat .env
```

以下のような出力が表示されればOKです:

```
NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."
```

---

## 使用方法

### 基本的な使い方

#### 1. デフォルトメッセージの送信

```bash
cd /home/node/myagentflow/antigravity/skills/notification
python3 scripts/notify_skill.py
```

**Discordに送信されるメッセージ**:
```
Pythonからのテスト通知です(引数なし)
```

#### 2. カスタムメッセージの送信

```bash
python3 scripts/notify_skill.py "ビルドが完了しました"
```

**Discordに送信されるメッセージ**:
```
ビルドが完了しました
```

#### 3. 複数単語のメッセージ

```bash
python3 scripts/notify_skill.py "デプロイが" "成功しました" "🎉"
```

**Discordに送信されるメッセージ**:
```
デプロイが 成功しました 🎉
```

### 応用的な使い方

#### パターンA: 絶対パスで実行(どこからでも実行可能)

```bash
# 現在のディレクトリに関係なく実行できる
python3 /home/node/myagentflow/antigravity/skills/notification/scripts/notify_skill.py "メッセージ"
```

#### パターンB: シェルスクリプトから呼び出し

```bash
#!/bin/bash

# ビルドスクリプト例
npm run build

if [ $? -eq 0 ]; then
    python3 /home/node/myagentflow/antigravity/skills/notification/scripts/notify_skill.py "ビルド成功 ✅"
else
    python3 /home/node/myagentflow/antigravity/skills/notification/scripts/notify_skill.py "ビルド失敗 ❌"
fi
```

#### パターンC: Pythonプログラムから呼び出し

```python
import sys
import os

# スキルのパスを追加
sys.path.append('/home/node/myagentflow/antigravity/skills/notification')

# インポート
from scripts import notify_skill

# 通常の通知
result = notify_skill.send_notification("処理が完了しました")
print(result)

# エラー通知(全員メンション付き)
result = notify_skill.send_notification("エラーが発生しました", is_error=True)
print(result)
```

**エラー通知の場合、Discordでは以下のように表示されます**:
```
@everyone 🚨 **Attention**: 
エラーが発生しました
```

---

## トラブルシューティング

### ❌ エラー: 環境変数が見つかりません

**エラーメッセージ**:
```
[Error] 環境変数 NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL が見つかりません。
/home/node/myagentflow/antigravity/skills/notification/.env を確認してください。
```

**原因と解決方法**:

| 原因 | 解決方法 |
|------|----------|
| `.env`ファイルが存在しない | `cp .env.example .env` で作成 |
| 環境変数名が間違っている | `.env`内の変数名を確認(`NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL`) |
| Webhook URLが設定されていない | `.env`にURLを追加 |
| ダブルクォートで囲んでいない | `NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL="URL"` の形式にする |

### ❌ エラー: モジュールが見つかりません

**エラーメッセージ**:
```
ModuleNotFoundError: No module named 'requests'
```

**解決方法**:
```bash
sudo apt-get install python3-requests python3-dotenv
```

### ❌ エラー: 通知失敗

**エラーメッセージ**:
```
通知失敗: HTTPError: 400 Client Error
```

**原因と解決方法**:

| 原因 | 解決方法 |
|------|----------|
| Webhook URLが無効 | Discordで新しいWebhookを作成し、URLを更新 |
| URLが途中で切れている | `.env`のURL全体がコピーされているか確認 |
| ネットワーク接続エラー | インターネット接続を確認 |
| チャンネルへのアクセス権限がない | Discordチャンネルの権限を確認 |

### ❌ エラー: Permission denied

**エラーメッセージ**:
```
PermissionError: [Errno 13] Permission denied: '.env'
```

**解決方法**:
```bash
# ファイルの権限を確認
ls -la .env

# 読み取り権限を追加
chmod 644 .env
```

---

## 技術仕様

### スクリプト仕様

**ファイル**: `scripts/notify_skill.py`

**主要機能**:

| 関数 | 説明 | 引数 | 戻り値 |
|------|------|------|--------|
| `send_notification(message, is_error)` | Discordに通知を送信 | `message` (str): メッセージ本文<br>`is_error` (bool): エラー通知フラグ | `str`: 実行結果メッセージ |

**環境変数**:

| 変数名 | 必須 | 説明 |
|--------|------|------|
| `NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL` | ✅ | Discord Webhook URL |

**依存ライブラリ**:

| ライブラリ | バージョン | 用途 |
|-----------|-----------|------|
| `requests` | 最新 | HTTP POST リクエスト送信 |
| `python-dotenv` | 最新 | `.env` ファイルの読み込み |

### エラーハンドリング

- 環境変数未設定時: エラーメッセージを表示し、処理を中断
- HTTP通信エラー時: 例外をキャッチし、エラーメッセージを返す
- タイムアウト: 10秒でタイムアウト

### セキュリティ

- `.env`ファイルは`.gitignore`で除外され、Gitにコミットされません
- Webhook URLは環境変数として管理され、コードに直接記述されません

---

## ディレクトリ構造

```
/home/node/myagentflow/antigravity/skills/notification/
├── SKILL.md                    # スキル定義(Antigravity用)
├── README.md                   # このファイル
├── .env                        # 環境変数(Git管理外)
├── .env.example                # 環境変数テンプレート
├── .gitignore                  # Git除外設定
└── scripts/
    └── notify_skill.py         # 通知スクリプト本体
```

---

## よくある質問

### Q1: 複数のチャンネルに通知を送りたい

A: 複数のWebhook URLを設定する場合は、環境変数を追加するか、スクリプトを複数回呼び出してください。

```bash
# チャンネル1に通知
NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL="URL1" python3 scripts/notify_skill.py "メッセージ"

# チャンネル2に通知
NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL="URL2" python3 scripts/notify_skill.py "メッセージ"
```

### Q2: メッセージに改行を入れたい

A: `\n`を使用してください(シェルの場合は`$'...'`構文を使用)。

```bash
python3 scripts/notify_skill.py $'1行目\n2行目\n3行目'
```

### Q3: メンション機能の詳細は?

A: `is_error=True`を指定すると、メッセージの先頭に`@everyone 🚨 **Attention**: `が追加され、検索チャンネルの全メンバーにメンションが送られます。

---

## サポート

問題が解決しない場合は、以下を確認してください:

1. Python環境: `python3 --version`
2. 依存ライブラリ: `python3 -c "import requests, dotenv; print('OK')"`
3. 環境変数: `cat .env`(URLは伏せて確認)
4. ネットワーク: `curl -I https://discord.com`

---

## ライセンス

このスキルは、Antigravityプロジェクトの一部として提供されています。
