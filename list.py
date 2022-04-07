from selenium import webdriver
import time


def sum (x,y):
    return str(x+y)


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_css_selector("[id='num1']").text
    y = browser.find_element_by_css_selector("[id='num2']").text
    z = (int(x)+int(y))
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(z))
    
 
    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    time.sleep(20)
    browser.quit()
