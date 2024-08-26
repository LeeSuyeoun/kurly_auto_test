from login import login
from slack_notifi import send_to_slack
from selenium import webdriver
from TestCase1 import tc1
from TestCase2 import tc2

import time
import traceback


if __name__ == "__main__":
    webhook_url = "https://hooks.slack.com/services/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"
    success_id = "ssss8784"
    password = "testtest00"

    driver = webdriver.Chrome()
    driver.maximize_window()

    combined_result = ""

    try:
        # 로그인 수행
        success, message = login(driver, success_id, password)
        combined_result = f"로그인 결과: {message}\n\n"

        if success:
            # TC1 실행
            tc1_result = tc1(driver)
            combined_result += tc1_result + "\n\n"
            # TC2 실행
            tc2_result = tc2(driver)
            combined_result += tc2_result + "\n\n"

    except Exception as e:
        # 예외 발생 시 오류 메시지를 추가
        combined_result += f"오류 발생: {str(e)}\n\n"
        combined_result += "스택 트레이스:\n" + traceback.format_exc() + "\n\n"

    finally:
        # 슬랙으로 최종 결과 전송
        send_to_slack(webhook_url, combined_result)
        time.sleep(5)
        driver.quit()
