import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains #추가

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://watcha.com/")

    
    lis = driver.find_elements(By.CLASS_NAME, "custom-1wp6uk4") # 클래스 이름으로 검색 _svp_item으로 되어있는 요소 모두 가져옴. elements.
    for li in lis:
        title = li.find_element(By.CLASS_NAME, 'custom-1histt2') # title과 content로 나눠서 클래스 이름으로 가져옴
        print(title.text) # 각 요소마다 제목, 내용 가져와서 출력


    ac=ActionChains(driver)
    elem=driver.find_element(By.CLASS_NAME,"custom-17amef")
    ac.click(elem)
    ac.perform()
    ac.pause(2)


    elem2=driver.find_element(By.CLASS_NAME,"custom-134bl1m")
    ac.click(elem2)
    ac.send_keys("kim")
    ac.send_keys(Keys.TAB)
    ac.pause(2)
    ac.send_keys("chanho")
    #여기까지 action 등록
    ac.perform()
    # 여기서 action 실행




except Exception as e:
    print(e)
finally:
    driver.quit()