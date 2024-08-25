from login import login
from slack_notifi import send_to_slack
from selenium import webdriver
import time
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException, TimeoutException

if __name__ == "__main__":
    webhook_url = "https://hooks.slack.com/services/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"
    success_id = "ssss8784"
    password = "testtest00"

    driver = webdriver.Chrome()
    driver.maximize_window()

    combined_result = ""

    try:
        # login 함수에서 반환되는 두 개의 값을 각각 받아옵니다.
        success, login_message = login(driver, success_id, password)
        
        # login_message를 그대로 combined_result에 추가합니다.
        combined_result += login_message

    except Exception as e:
        combined_result += f"오류 발생: {str(e)}\n\n"
        combined_result += "스택 트레이스:\n" + traceback.format_exc() + "\n\n"

    finally:
        send_to_slack(webhook_url, combined_result)
        time.sleep(5)
        driver.quit()
