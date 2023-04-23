"""
1. 네이버에 접속한다.
2. 안양대를 검색한다.
3. VIEW탭을 클릭한다. ( click() 함수가 있음. )
4. 처음 나오는 검색 결과 제목, 내용 수집해서 출력한다.
"""
# 20분
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://naver.com")
    time.sleep(3)

    elem = driver.find_element(By.ID, 'query')
    elem.send_keys('안양대')
    elem.send_keys(Keys.RETURN)

    # tab = driver.find_elements(By.CLASS_NAME, "tab")[3]
    tab = driver.find_element(By.LINK_TEXT, "VIEW")
    tab.click()

    lis = driver.find_elements(By.CLASS_NAME, '_svp_item')
    for li in lis:
        title = li.find_element(By.CLASS_NAME, 'total_tit')
        content = li.find_element(By.CLASS_NAME, 'total_dsc')
        print(title.text, content.text)

except Exception as e:
    print(e)
finally:
    driver.quit()