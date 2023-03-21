from selenium import webdriver
from selenium.webdriver.common.by import By   #find_element(By.CLASS_NAME,"gLFyf")사용
import time
from selenium.webdriver.common.keys import Keys #enter키 불러오기

driver = webdriver.Chrome()
url = 'https://www.daum.net'
driver.get(url)

time.sleep(3)

driver.find_element(By.CLASS_NAME,"inner_login").click()
driver.find_element(By.ID,"loginKey--1").send_keys("")
driver.find_element(By.ID,"password--2").send_keys("")
driver.find_element(By.CLASS_NAME,"recaptcha-checkbox-checkmark").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"btn_g highlight submit").click()



while(1):
    pass