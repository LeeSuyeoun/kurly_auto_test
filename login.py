from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback

def login(driver, id, password):
    result = ""
    driver.get("https://www.kurly.com/member/login")
    username_field = driver.find_element(By.NAME, "id")
    password_field = driver.find_element(By.NAME, "password")
    username_field.send_keys(id)
    password_field.send_keys(password)
    login_button = driver.find_element(By.CLASS_NAME,"e4nu7ef3")
    login_button.click()

    try:
        username = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "eo7pjfk1"))
        )

        if username.text == "이수연 님":
            result = "로그인 성공 :" + username.text + "과 일치합니다"
            return True, result
        else:
            result = "로그인 실패 :" + username.text + "과 일치 하지 않습니다"
            return False, result

    except Exception as e:
        tb = traceback.format_exc()
        result = f"작업 실패: {str(e)} (at line {tb.splitlines()[-3]})\n"
        return False, result
