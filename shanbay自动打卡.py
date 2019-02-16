import selenium
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

def login(username,password):
    drive = webdriver.Chrome()
    url = "https://web.shanbay.com/web/account/login"
    drive.get(url)
    user = drive.find_element_by_id("input-account")
    user.send_keys(username)
    drive.find_element_by_id("input-password").send_keys(password)
    drive.find_element_by_id("button-login").click()
    time.sleep(2)
    drive.find_element_by_xpath("//*[text()='单词']").click()
    time.sleep(2)
    drive.find_element_by_xpath("//*[text()='开始学习']").click()
    time.sleep(2)
    for i in range(0,305):
        try :
            drive.find_element_by_xpath("//*[text()='认识']").click()
        except:
            pass
        time.sleep(3)
        try :
            for n in range(0,10):
                try:
                    if drive.find_element_by_css_selector("#learning-box > div.test-box.span12.learning-detail-container > div:nth-child("+str(n)+") > div > a"):
                        drive.find_element_by_css_selector("#learning-box > div.test-box.span12.learning-detail-container > div:nth-child("+str(n)+") > div > a").click()
                        break
                except:
                    continue
            if drive.find_element_by_css_selector("#summary-box > div.span9 > div:nth-child(3) > div > a"):
                drive.find_element_by_css_selector("#summary-box > div.span9 > div:nth-child(3) > div > a").click()
        except:
            pass
        time.sleep(3)
    print("300单词已经学完了")
    drive.close()






