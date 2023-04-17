import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # 관리하는 경로 설치, 연결

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service) # driver을 통해 제어
try:
    driver.get("http://naver.com") # get을 통해 네이버 페이지 가져옴
    time.sleep(3)
    #추가사항
    elem=driver.find_element(By.ID, 'query')
    elem.send_keys('파이썬')
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()

#selenium: 동적 페이지 크롤링