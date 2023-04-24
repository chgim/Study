import time
from selenium import webdriver # 크롬 브라우저를 띄우기 위한 웹드라이버를 가져옴
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys # Keys: 웹 문서에 문자가 아닌 키(ex: 엔터)를 전달하기 위해 필요
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 업데이트

#크롬 드라이버 자동 설치
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)# driver을 통해 제어
try:
    driver.get("https://naver.com")# get을 통해 네이버 페이지 가져옴
    time.sleep(3)
    #추가사항
    elem = driver.find_element(By.ID, 'query') # find_element_by_id를 사용하여 해당 요소를 가져옴(검색버튼)
    elem.send_keys('파이썬') #  send_keys로 계정 정보 입력
    elem.send_keys(Keys.RETURN) # send_keys(Keys.RETURN)으로 엔터를 전송
    time.sleep(5)

except Exception as e:
    print(e)
finally:
    driver.quit() # driver.quit(): chromedriver를 닫음

    # selenium: 동적 페이지 크롤링
    # pip install selenium  webdriver-manager
    # get 함수: 입력값으로 준 주소로 이동
    # find_element: 원하는 요소 찾기 (By.ID를 사용하여 id속성값 활용)
    # find_elements: 원하는 모든 요소 찾기 (By.TAG_NAME:태그명 활용)