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
    driver.get("https://www.instagram.com/")
    time.sleep(2)

    ac=ActionChains(driver)
    elem=driver.find_element(By.CLASS_NAME,"_aa4b")
    
    ac.click(elem)
    # ac.context_click()
    # ac.move_to_element_with_offset(elem,20,-10)
    ac.pause(1)
    ac.send_keys("Hello")
    ac.send_keys(Keys.TAB)
    ac.pause(1)
    ac.send_keys("Hello")
    #여기까지 action 등록
    ac.perform()
    # 여기서 action 실행
except Exception as e:
    print(e)
finally:
    driver.quit()