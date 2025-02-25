# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,os,logging
from retrying import retry

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import schedule

@retry(wait_random_min=5000, wait_random_max=10000, stop_max_attempt_number=3)
def enter_iframe(browser):
    try:
        logging.info("Enter login iframe")
        target = browser.find_element_by_xpath("//*[starts-with(@id,'x-URS-iframe')]")
        # browser.execute_script('arguments[0].scrollIntoView(true);', target)
        browser.switch_to.frame(target)

        return browser
    except Exception as e:
        logging.error("Error entering iframe: %s", e)
        raise

# 失败后随机 1-3s 后重试，最多 3 次
@retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=5)
def extension_login(email, password,userDataDir):
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("user-data-dir="+userDataDir)
        # chrome_options.add_argument("profile-directory"+profile_name)
        logging.info("Load Chrome extension NetEaseMusicWorldPlus")
        chrome_options.add_extension('NetEaseMusicWorldPlus.crx')

        logging.info("Load Chrome driver")
        browser = webdriver.Chrome(executable_path="chromedriver.exe", options=chrome_options)

        # 设置全局的隐式等待(直到找到元素),20秒后找不到抛出找不到元素
        browser.implicitly_wait(20)

        logging.info("Getting the webpage")
        browser.get('https://music.163.com')
        

        browser.refresh() # 刷新页面
        time.sleep(5)

        # 进入音乐清单
        logging.info("Click my playlist")
        browser.find_element_by_xpath('//a[.//em[text()="我的音乐"]]').click()

        time.sleep(5)

        try:
            browser.switch_to.frame("g_iframe")
            logging.info("Successfully entered the playing frame")
        
        except Exception as e:
            logging.error("Error entering iframe: %s", e)
            raise

        # 播放音乐
        logging.info("Play the music")
        browser.find_element(By.ID, 'flag_play').click()

        time.sleep(10)
        browser.refresh() # 刷新页面
        logging.info("Unlock finished")

        time.sleep(10)
        browser.quit()
    except Exception as e:
        logging.error("Error during login process: %s", e)
        raise

def login_task():
    try:
        # email = os.environ['EMAIL']
        # password = os.environ['PASSWORD']
        email="test"
        password="test123"
        userDataDir = "C:\\Users\\yaaly\\AppData\\Local\\Google\\Chrome\\User Data"  # path of Chrome profile
        profile_name = "Profile 1"

    except:
        logging.error('Fail to read email and password.')
        exit(1)
    else:
        try:
            extension_login(email,password,userDataDir)
        except Exception as e:
            logging.error("Failure in auto login: %s", e)
            exit(1)
        else:
            logging.info("Script executed successfully")
            exit(0)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,format='[%(levelname)s] %(asctime)s %(message)s')
    schedule.every().day.at("01:48").do(login_task)# timer to repeat the task
    login_task()

    while True:
        schedule.run_pending()  
        time.sleep(1)
