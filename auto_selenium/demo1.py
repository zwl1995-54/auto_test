from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.get("https://www.jd.com")
driver.find_element_by_css_selector("#kw").send_keys("您好")
sleep(10)
driver.find_element_by_css_selector("#su").click()
# driver.find_element_by_link_text("女装").click()
sleep(5)
driver.quit()