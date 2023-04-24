"""
1. 네이버에 접속한다.
2. 안양대를 검색한다.
3. VIEW탭을 클릭한다. ( click() 함수가 있음. )
4. 처음 나오는 검색 결과 제목, 내용 수집해서 출력한다.
"""
# 20분
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
    driver.get("https://naver.com") # get을 통해 네이버 페이지 가져옴
    time.sleep(3)

    elem = driver.find_element(By.ID, 'query') # find_element_by_id를 사용하여 해당 요소를 가져옴(검색버튼)
    elem.send_keys('안양대') # 해당 요소로 키 입력
    elem.send_keys(Keys.RETURN) # send_keys(Keys.RETURN)으로 엔터를 전송

    # tab = driver.find_elements(By.CLASS_NAME, "tab")[3]
    tab = driver.find_elements(By.LINK_TEXT, "VIEW") 
    # link_text는 <a> tag의 링크를 대상으로 찾는다. 비슷하게 partial_link_text는 요소의 링크가 전달한 링크를 일부분으로 포함되어 있으면 해당 요소가 선택된다.
    tab.click() # 해당 요소를 클릭

    lis = driver.find_elements(By.CLASS_NAME, '_svp_item') # 클래스 이름으로 검색 _svp_item으로 되어있는 요소 모두 가져옴. elements.
    for li in lis:
        title = li.find_element(By.CLASS_NAME, 'total_tit') # title과 content로 나눠서 클래스 이름으로 가져옴
        content = li.find_element(By.CLASS_NAME, 'total_dsc')
        print(title.text, content.text) # 각 요소마다 제목, 내용 가져와서 출력

except Exception as e:
    print(e)
finally:
    driver.quit() # driver.quit(): chromedriver를 닫음


    # selenium: 동적 페이지 크롤링
    # pip install selenium  webdriver-manager
    # get 함수: 입력값으로 준 주소로 이동
    # find_element: 원하는 요소 찾기 (By.ID를 사용하여 id속성값 활용)
    # find_elements: 원하는 모든 요소 찾기 (By.TAG_NAME:태그명 활용)

    # pip install selenium  webdriver-manager