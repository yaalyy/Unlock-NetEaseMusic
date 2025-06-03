# Unlock-NetEaseMusic

Use the Chrome extension NetEaseMusicWorld++ to unlock overseas NetEase Music access.

It's run by Github Actions, so no self-hosted server is needed. Alternatively, you can run by local browser cache.  

## System Requirements  
:white_check_mark:Windows 8.1/10/11 (x64)  
:white_check_mark:Linux (Only for X64 CPU)  
:x:MacOS (Not Supported, developing)  

## How to run on Github (Need manual login at the first time to obtain cookie)

1. Fork this repository (and star if you like it)  
2. In your own repository, enter your config json that should be in [`config.json`](./config.json "`config.json`") as the value of Github Action repository secrets `CONFIG`.  
3. Run Github Action `Unlock-NetEaseMusic` (It will run automatically every day.)

## How to run locally

### Run by email address and password  (May be intercepted by CAPTCHA in oversea)
~~1. Install python packages: `pip install -r requirements.txt `~~  
~~2. Enter your email address and password in `auto_login.py`~~  
~~3. Run `auto_login.py`~~   

### Run by local browser cache (Recommended)
1. Open the Chrome on your local computer to login Netease Music, then use Inspect tool of the Chrome to find the cookie named `MUSIC_U` and copy its value for the later use.  
If you find it difficult to use Inspect tool to obtain cookie, you can use our help procedure to automatically obtain, by executing `python cookie_extract.py`. In this case, you are given 30 seconds to login, and the obtained cookie will be printed on the terminal. 
2. Install python packages: `pip install -r requirements.txt `   
3. When run by local browser cache, the email, password, userDataDir and profileName in [`config.json`](./config.json "`config.json`") are not needed, so you can fill in them casually.  
Enter the value of login_cookie that we obtained in step 1.  
~~Enter your chrome profile path in `config.json`, this path is usually `C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data` for Windows. This path can also be found in `chrome://version/`.~~     

4. Set the timer for repeating the task.  
5. Run `python local_login.py`  

### Run by Docker
1. Run `docker build -t netease .` to build the Docker image.  
2. Follow the step 1 in [Run by local browser cache](#run-by-local-browser-cache-recommended) to obtain the login cookie.  
3. After filling config json into [`config.json`](./config.json "`config.json`"), run `docker run -v $PWD/config.json:/app/config.json netease` to launch the Docker container and mount the json file.  
     
## config.json Template
We support single user mode and multi-user mode.  
**Single User**:  
```json
{
    "userDataDir": "C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data",
    "email": "test",
    "password": "test123",
    "login_cookie": "xxx"
}
```
**Multi-User**:  
```json
{
    "users": [
        {
            "userDataDir": "C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data",
            "email": "test",
            "password": "test123",
            "name": "tt",
            "profileName": "profile 1",
            "login_cookie": "xxx"
        },
        {
            "userDataDir": "C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data",
            "email": "test",
            "password": "test123",
            "name": "user2",
            "profileName": "profile 2",
            "login_cookie": "xxx"
        }
    ]

}
```
### PS: Multi-Account Mode:   
To run in multi-account mode, you need to login and fill in the login_cookie for every Netease Music account.
~~To run in multi-account mode, you need to create multiple Chrome profiles, and login your respective account in each profile. Then in the config.json, you need to fill in different profile names for each profile.~~

### Cookie Expire Duration:
Each cookie obtained by login has about 1-month expire duration, which is not valid forever. Therefore, after about one month, you need to login again to obtain a new cookie.

## How it works

When you login to https://music.163.com in Chrome the extension NetEaseMusicWorld++ will automatically run a script to make NetEase believe that your IP is in China. Once this is done, NetEase will allow you to access music in all platforms (e.g. on phone apps) for a short time (unclear) even if you access from a foreign IP.

The Github Action will run daily to do the above actions and unlock you from the foreign IP restriction.  

When you use local browser cache to execute, the script would use the cookie in your local browser to play songs, but you have to manully login the account in advance to obtain the cookie.  

## Credit
This repo was forked from [Lennox-Elaphurus/Unlock-NetEaseMusic](https://github.com/Lennox-Elaphurus/Unlock-NetEaseMusic "Lennox-Elaphurus/Unlock-NetEaseMusic"). Due to the original repo has been archived, we decided to detach the fork connection for the future maintenance, and this also makes this repo enabled to be indexed by people, as forked repo is not indexed on GitHub by default. 
