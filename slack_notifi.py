#슬랙 메시지 전송 모듈

import requests
import json

def send_to_slack(webhook_url, message):
    payload = {
        "text": message
    }
    try:
        response = requests.post(
            webhook_url, data=json.dumps(payload),
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code != 200:
            raise ValueError(
                f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}"
            )
    except Exception as e:
        print(f"Error sending message to Slack: {e}")