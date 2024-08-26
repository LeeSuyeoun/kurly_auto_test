from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def tc1(driver):
    result = ""  # result 변수를 초기화합니다.

    try:
        # 요소가 로드될 때까지 대기
        username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "eo7pjfk1"))
        )
        username.click()
        
        # 배너 텍스트 확인
        banner = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "e5rtjnl0"))
        )

        # 배너 텍스트가 기대한 것과 일치하는지 확인 후 결과 전달
        if banner.text == "월 0원으로 매일 무료 배송 받기":
            result += "tc1번 성공 : '" + banner.text + "' 확인 했습니다. (PASS)\n"
        else:
            result += "tc1번 실패 : '" + banner.text + "' 확인 했습니다. (FAIL)\n"

    except Exception as e:
        # 예외 발생 시 실패 메시지를 기록
        result += f"tc1번 실패: 오류 발생 - {str(e)}\n"

    return result if result else "tc1번 실패: 결과를 가져오지 못했습니다.\n"  # 항상 문자열 반환
