from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открываем браузер
    browser = webdriver.Chrome()
    browser.get(link)

    # Ждем появления нужного текста
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    # Нажимаем на кнопку
    button1 = browser.find_element(By.ID, "book")
    button1.click()

    # Находим x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve")
    button.click()

    # Успеть скопировать код за 30 секунд
    time.sleep(10)

finally:
    # Закрывать браузер после всех манипуляций
    browser.quit()