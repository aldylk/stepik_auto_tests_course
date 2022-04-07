from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_css_selector("button.btn-primary")
    button.click()


     
    confirm = browser.switch_to.alert
    confirm.accept()

    

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)


    input = browser.find_element_by_css_selector("[id='answer']")
    input.send_keys(str(math.log(abs(12 * math.sin(int(x))))))

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()
    
finally:
    print(browser.switch_to.alert.text)
    # закрываем браузер после всех манипуляций
    browser.quit()
