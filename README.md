# Unlock-NetEaseMusic

Use the Chrome extension NetEaseMusicWorld+ to unlock overseas NetEase Music access.

It's run by Github Actions, so no self-hosted server is needed(This feature is **maintaining**, not available). Alternatively, you can run by local browser cache.  

## System Requirements  
:white_check_mark:Windows 8.1/10/11   
:x:Linux (Not Supported, developing)  
:x:MacOS (Not Supported, developing)  

## How to run on Github  (May be intercepted by CAPTCHA in oversea)

~~1. Fork this repository (and star if you like it)~~  
~~2. In your own repository, enter your email and password as the value of two Github Action repository   secrets `EMAIL` and `PASSWORD` .~~  
~~3. Run Github Action `Unlock-NetEaseMusic` (It will run automatically every day.)~~  

## How to run locally

### Run by email address and password  (May be intercepted by CAPTCHA in oversea)
~~1. Install python packages: `pip install -r requirements.txt `~~  
~~2. Enter your email address and password in `auto_login.py`~~  
~~3. Run `auto_login.py`~~   

### Run by local browser cache (Recommended)
1. Open the Chrome on your local computer to login Netease Music, then close the Chrome(Closing the Chrome is important).  
2. Install python packages: `pip install -r requirements.txt `   
3. Enter your chrome profile path in `config.json`, this path is usually `C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data` for Windows. This path can also be found in `chrome://version/`. When run by local browser cache, the email and password in `config.json` are not needed, so you can fill in them casually.      
4. Set the timer for repeating the task.  
5. Run `local_login.py`  
## config.json Template
We support single user mode and multi-user mode.  
**Single User**:  
```json
{
    "userDataDir": "C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data",
    "email": "test",
    "password": "test123"
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
            "profileName": "profile 1"
        },
        {
            "userDataDir": "C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data",
            "email": "test",
            "password": "test123",
            "name": "user2",
            "profileName": "profile 2"
        }
    ]

}
```
### PS: Multi-Account Mode:   
To run in multi-account mode, you need to create multiple Chrome profiles, and login your respective account in each profile. Then in the config.json, you need to fill in different profile names for each profile.

## How it works

When you login to https://music.163.com in Chrome the extension NetEaseMusicWorld+ will automatically run a script to make NetEase believe that your IP is in China. Once this is done, NetEase will allow you to access music in all platforms (e.g. on phone apps) for a short time (unclear) even if you access from a foreign IP.

The Github Action will run daily to do the above actions and unlock you from the foreign IP restriction.  

When you use local browser cache to execute, the script would use the cookie in your local browser to play songs, but you have to manully login the account in advance to obtain the cookie.  

## Credit
This repo was forked from [Lennox-Elaphurus/Unlock-NetEaseMusic](https://github.com/Lennox-Elaphurus/Unlock-NetEaseMusic "Lennox-Elaphurus/Unlock-NetEaseMusic"). Due to the original repo has been archived, we decided to detach the fork connection for the future maintenance, and this also makes this repo enabled to be indexed by people, as forked repo is not indexed on GitHub by default. 
