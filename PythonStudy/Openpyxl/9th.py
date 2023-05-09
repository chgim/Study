import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
try:
    driver.get("https://cafe.naver.com/joonggonara")

    elem = driver.find_element(By.ID, "topLayerQueryInput")
    elem.send_keys("자전거")
    elem.send_keys(Keys.RETURN)

    time.sleep(1)

    iframe = driver.find_element(By.ID, "cafe_main")
    driver.switch_to.frame(iframe)

    elem = driver.find_elements(By.CLASS_NAME, "article-board")
    elem = elem[1]

    # trs = elem.find_elements(By.TAG_NAME, "tr")
    trs = elem.find_elements(By.XPATH, "./table/tbody/tr")
    for tr in trs:
        title = tr.find_element(By.CLASS_NAME, "article")
        link = title.get_attribute("href")
        print(title.text, link)

except Exception as e:
    print(e)
finally:
    driver.quit()