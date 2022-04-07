from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input = browser.find_element_by_css_selector("[id='answer']")
    input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    
    option1 = browser.find_element_by_css_selector("[id='robotCheckbox']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[id='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    time.sleep(20)
    browser.quit()

