import time, logging
from selenium import webdriver
from utils.driver_path import get_driver_path

#timer = 30 # time for manual login, unit of seconds, 

def extract_cookie():
    chrome_options = webdriver.ChromeOptions()

    logging.info("Load Chrome driver")
    browser = webdriver.Chrome(options=chrome_options)

    browser.implicitly_wait(20)

    logging.info("Getting the webpage")
    browser.get('https://music.163.com')

    logging.info("Please complete the login in the browser, then press Enter to extract the cookid")
    input("Press Enter after completing the login...")
    browser.refresh() # 刷新页面
    print(browser.get_cookie("MUSIC_U"))

if __name__ == "__main__":
    try:
        extract_cookie()
    except Exception as e:
        logging.error("Error: %s", e)