#한번에 주석처리 단축키 ctrl + /

from selenium import webdriver
from selenium.webdriver.common.by import By   #find_element(By.CLASS_NAME,"gLFyf")사용 가능
import time
from selenium.webdriver.common.keys import Keys #enter키 불러오기
import openpyxl

sort= input("원하는 채용 종류를 입력하시오:")

driver = webdriver.Chrome()
url = 'https://www.saramin.co.kr/zf_user/public-recruit/schedule'
driver.get(url)

def load():
    name=[]
    type=[]
    date=[]

    recruit = driver.find_element(By.CLASS_NAME,"recruit_content_list")
    time.sleep(1)

    tbody = recruit.find_element(By.TAG_NAME,"tbody")
    rows = tbody.find_elements(By.TAG_NAME,"tr")

    for value in rows:
        body1=value.find_elements(By.TAG_NAME,"td")[1]
        body2=value.find_elements(By.TAG_NAME,"td")[2]
        body3=value.find_elements(By.TAG_NAME,"td")[3]

        if body2.text==sort:#text==>selenium element텍스트 읽기, 가져오기
            name.append(body1.text)
            type.append(body2.text)
            date.append(body3.text)

            print(body1.text,body2.text,body3.text)
    return name,type,date #조건에 맞는 리스트 반환

load()
list1,list2,list3=load() #list1=name list2=type list3=date
cor=list1
kind=list2
day=list3

xpath="//a[@class='page']" #xpath 값 설정 class는 고유한 값
i=0

try:
    while(1):
        nextpage=driver.find_elements(By.XPATH,xpath)[i].click()
        load()
        list1,list2,list3=load()
        cor=cor+list1
        kind=kind+list2
        day=day+list3 
        i=i+1
       
except IndexError:
    print("페이지가 더 없습니다")

wb=openpyxl.Workbook()#임시 엑셀생성
wb.create_sheet("saramin")#시트 추가

sheet= wb["saramin"] #시트 선택
sheet.append(cor)#리스트를 append할때는 []가 필요 없다
sheet.append(kind)
sheet.append(day)

wb.save("C:/coding/saraminexcel.xlsx")


while(1):
    pass
