import time, logging
from selenium import webdriver

timer = 30 # time for manual login, unit of seconds, 

def extract_cookie():
    chrome_options = webdriver.ChromeOptions()

    logging.info("Load Chrome driver")
    browser = webdriver.Chrome(executable_path="/chromedriver/win64/chromedriver.exe", options=chrome_options)

    browser.implicitly_wait(20)

    logging.info("Getting the webpage")
    browser.get('https://music.163.com')

    logging.info("You have 30 second to complete login")
    time.sleep(timer)
    browser.refresh() # 刷新页面
    print(browser.get_cookie("MUSIC_U"))

if __name__ == "__main__":
    try:
        extract_cookie()
    except Exception as e:
        logging.error("Error: %s", e)