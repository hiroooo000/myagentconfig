import os
import sys
import json
import requests
from dotenv import load_dotenv

# ---------------------------------------------------------
# 設定ファイルの読み込み (堅牢版)
# ---------------------------------------------------------
# このスクリプト自身があるフォルダの場所を取得
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 親ディレクトリ(notify_google_chat)の .env を読み込む
PARENT_DIR = os.path.dirname(BASE_DIR)
load_dotenv(os.path.join(PARENT_DIR, '.env'))

ENV_VAR_NAME = "NOTIFY_ANTIGRAVITY_TO_DISCORD_WEBHOOK_URL"

def send_notification(message: str, is_error: bool = False) -> str:
    """
    Discordへ通知を送信します。
    
    Args:
        message (str): 送信するメッセージ
        is_error (bool): エラー通知の場合True(全員メンション付き)
    
    Returns:
        str: 実行結果メッセージ
    """
    webhook_url = os.environ.get(ENV_VAR_NAME)

    if not webhook_url:
        error_msg = f"[Error] 環境変数 {ENV_VAR_NAME} が見つかりません。{PARENT_DIR}/.env を確認してください。"
        print(error_msg)
        return error_msg

    # Discordでは @everyone で全員メンション
    prefix = "@everyone " 
    
    payload = {
        "content": f"{prefix}{message}"
    }

    try:
        response = requests.post(
            webhook_url, 
            data=json.dumps(payload), 
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        response.raise_for_status()
        return f"通知成功: {message}"
    
    except Exception as e:
        return f"通知失敗: {e}"

# ---------------------------------------------------------
# コマンドライン実行ブロック
# ---------------------------------------------------------
if __name__ == "__main__":
    # 引数を取得 (例: python notify_skill.py "こんにちは")
    args = sys.argv[1:]
    
    if len(args) >= 2:
        project_name = args[0]
        message_body = " ".join(args[1:])
        msg = f"[{project_name}] {message_body}"
        print(f"送信中: '{msg}' ...")
        result = send_notification(msg)
    else:
        # 引数が足りない場合
        print("Usage: python notify_skill.py <project_name> <message>")
        result = "Error: Arguments required (Project Name, Message)"

    
    print(result)
