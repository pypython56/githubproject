#python -m venv selenium 파이썬 가상환경 설정 TERMINAL


from selenium import webdriver
from selenium.webdriver.common.by import By   #find_element(By.CLASS_NAME,"gLFyf")
import time
from selenium.webdriver.common.keys import Keys #enter키 불러오기

driver = webdriver.Chrome()
url = 'https://www.google.com'
driver.get(url)

time.sleep(3)

driver.find_element(By.CLASS_NAME,"gLFyf").send_keys("사람인") #구글 검색창에 "사람인"입력
driver.find_element(By.CLASS_NAME,"gLFyf").send_keys(Keys.ENTER) #Keys로 ENTER
driver.find_elements(By.CLASS_NAME,"LC20lb")[0].click() #elements, [2]를 사용하여 검색내용의 리스트 3번째 내용 클릭
driver.find_elements(By.CLASS_NAME,"LC20lb")[0].click()


while(1):
    pass