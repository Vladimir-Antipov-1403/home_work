from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

def check_elements() -> None:
    # Запуск браузера
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new") 

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get("https://www.saucedemo.com/")
        
        wait = WebDriverWait(driver, 10)

        username = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        password = wait.until(EC.presence_of_element_located((By.ID, "password")))
        submit   = wait.until(EC.presence_of_element_located((By.ID, "login-button")))

        # Проверка наличия всех элементов
        if username and password and submit:
            print("Элементы найдены")
    except TimeoutException:
        print("Один или несколько элементов не найдены")
    finally:
        driver.quit()

# Запуск функции
if __name__ == "__main__":
    check_elements()
