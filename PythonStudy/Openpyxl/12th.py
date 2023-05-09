import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains #추가

service = Service(ChromeDriverManager().install())

filepath=os.path.abspath(__file__)
basepath=os.path.dirname(filepath)
chromepath=os.path.join(basepath, 'Chrome')

opts=webdriver.ChromeOptions()
opts.add_argument(f"user-data-dir={chromepath}")

driver = webdriver.Chrome(service=service, options=opts)
try:
    driver.get("https://www.naver.com/")
    input()
    time.sleep(2)
    
   

except Exception as e:
    print(e)
finally:
    driver.quit()