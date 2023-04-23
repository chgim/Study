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
    elem.send_keys('파이썬')
    elem.send_keys(Keys.RETURN)

    uls = driver.find_elements(By.CLASS_NAME, 'keyword_challenge_list')
    ul = uls[0]

    lis = ul.find_elements(By.XPATH, './li')
    for li in lis:
        title = li.find_element(By.CLASS_NAME, 'title')
        content = li.find_element(By.CLASS_NAME, 'desc')
        print(title.text, content.text)


    # for title in titles:
    #     print(title.text)

    # contents = ul.find_elements(By.CLASS_NAME, 'txt')
    # for content in contents:
    #     print(content.text)


except Exception as e:
    print(e)
finally:
    driver.quit()