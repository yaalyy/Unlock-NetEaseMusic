# coding: utf-8

from selenium import webdriver
import time,os,logging
from retrying import retry
from selenium.webdriver.common.by import By
import schedule
import json
from Users import User
from logging.handlers import TimedRotatingFileHandler

"""Abandoned code"""
# @retry(wait_random_min=5000, wait_random_max=10000, stop_max_attempt_number=3)
# def enter_iframe(browser):
#     try:
#         logging.info("Enter login iframe")
#         target = browser.find_element_by_xpath("//*[starts-with(@id,'x-URS-iframe')]")
#         # browser.execute_script('arguments[0].scrollIntoView(true);', target)
#         browser.switch_to.frame(target)

#         return browser
#     except Exception as e:
#         logging.error("Error entering iframe: %s", e)
#         raise



# 失败后随机 1-3s 后重试，最多 3 次
@retry(wait_random_min=1000, wait_random_max=3000, stop_max_attempt_number=3)
def extension_login(email=None, password=None, userDataDir=None, profile_name=None, cookie=None):
    try:
        chrome_options = webdriver.EdgeOptions()
        chrome_options.add_argument("headless")  # Headless mode(Browser running in backend)
        if os.environ.get("CHROME_NO_SANDBOX") == "1":
            chrome_options.add_argument("--no-sandbox")  # This is required for docker environments
            chrome_options.add_argument("--disable-dev-shm-usage")  # Avoid shared memory limits in container environments

        #chrome_options.add_argument("user-data-dir="+userDataDir)
        #if profile_name:
        #    chrome_options.add_argument("profile-directory="+profile_name)

        
        logging.info("Load Chrome extension NetEaseMusicWorldPlus")
        chrome_options.add_extension('NetEaseMusicWorldPlus.crx')

        logging.info("Load Chrome driver")
        browser = webdriver.Edge(options=chrome_options)

        if(not cookie):
            raise Exception("Not found login cookie")
        

        # 设置全局的隐式等待(直到找到元素),20秒后找不到抛出找不到元素
        browser.implicitly_wait(20)

        logging.info("Getting the webpage")
        browser.get('https://music.163.com')
        
        browser.add_cookie({"name": "MUSIC_U", "value": cookie, "httpOnly": True})
        logging.info("Inserted cookie")

        browser.refresh() # 刷新页面
        time.sleep(5)


        # 进入音乐清单
        logging.info("Click my playlist")
        browser.find_element(By.XPATH, '//a[.//em[text()="我的音乐"]]').click()

        time.sleep(10)

        try:
            browser.switch_to.frame("g_iframe")
            logging.info("Successfully entered the playing frame")
        
        except Exception as e:
            logging.error("Error entering iframe: %s", e)
            raise

        # 播放音乐
        #logging.info("Play the music")
        #browser.find_element(By.ID, 'flag_play').click()

        time.sleep(20)
        browser.refresh() # 刷新页面
        logging.info("Unlock finished")

        time.sleep(10)
        browser.quit()
    except Exception as e:
        logging.error("Error during login process: %s", e)
        browser.quit()
        raise

def login_task():
    global error_flag
    try:
        # email = os.environ['EMAIL']
        # password = os.environ['PASSWORD']
        multi_user_mode = False
        try:
            with open("config.json",mode="r", encoding="utf-8") as read_file:
                config_data = json.load(read_file)
        except FileNotFoundError:
            logging.info("Config File Not Found")
            config_data = None
            error_flag = True
            return
        except json.JSONDecodeError:
            logging.info("ERROR: config.json error format！")
            config_data = None
            error_flag = True
            return

        #if(config_data):
        #    print("Got config")
        if "users" in config_data:
            multi_user_mode = True
            users = []
            for user in config_data["users"]:
                name = user["name"]
                email= user["email"]
                password = user["password"]
                userDataDir = user["userDataDir"]  # path of Chrome profile
                profile_name = user["profileName"]
                login_cookie = user["login_cookie"]
                users.append(User(name = name, email = email, password = password, userDataDir = userDataDir, profileName=profile_name, cookie=login_cookie))
        else:
            email=config_data["email"]
            password=config_data["password"]
            userDataDir = config_data["userDataDir"]  # path of Chrome profile
            login_cookie = config_data["login_cookie"]
            

    except Exception as e:
        logging.error('Failed to read user credential: ',e)
        error_flag = True
        # exit(1)
        return
    else:
        if multi_user_mode == True:  # multi user mode
            for user in users:
                email = user.getEmail()
                password = user.getPassword()
                userDataDir = user.getUserDataDir()
                name = user.getName()
                profile_name = user.getProfileName()
                login_cookie = user.getCookie()
                try:
                    logging.info("Start auto login of user (%s)", name)
                    extension_login(email=email,password=password,userDataDir=userDataDir,profile_name=profile_name, cookie=login_cookie)
                except Exception as e:
                    logging.error("Failure in auto login of user (%s) :%s",name, e)
                    # exit(1)
                else:
                    logging.info("User (%s) script executed successfully", name)
                    # exit(0)
        
        else:  # single user
            try:
                extension_login(email=email,password=password,userDataDir=userDataDir,cookie=login_cookie)
            except Exception as e:
                logging.error("Failure in auto login: %s", e)
                # exit(1)
            else:
                logging.info("Script executed successfully")
                # exit(0)
    
if __name__ == '__main__':
    # created logs directory
    if not os.path.exists('logs'):
        os.makedirs('logs')

    # Setting up logging
    log_formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(message)s')
    log_file_path = os.path.join('logs', 'netease_music.log')
    
    file_handler = TimedRotatingFileHandler(log_file_path, when='midnight', interval=1, backupCount=30, encoding='utf-8')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.INFO)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(log_formatter)

    logging.basicConfig(level=logging.INFO, handlers=[file_handler, console])

    # Setting up scheduler
    schedule_logger = logging.getLogger("schedule")
    schedule_logger.setLevel(level=logging.DEBUG)
    
    schedule.every().day.at("01:48").do(login_task)# timer to repeat the task
    
    error_flag = False
    login_task()

    while not error_flag:
        schedule.run_pending()  
        time.sleep(1)
