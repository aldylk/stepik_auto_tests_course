from selenium import webdriver
import time
import os

try: 
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    elements = browser.find_elements_by_css_selector("input.form-control[required]")
    for element in elements:
        element.send_keys("Мой ответ")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test1.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element_by_css_selector ("[type='file']")
    element.send_keys(file_path)

  

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

