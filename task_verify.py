from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(12)

browser.get(" http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
button=browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_css_selector("[id='input_value']")
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector("[id='answer']")
input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))

button = browser.find_element_by_css_selector("[id='solve']")
button.click()


