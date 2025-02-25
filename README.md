# Unlock-NetEaseMusic

Use the Chrome extension NetEaseMusicWorld+ to unlock overseas NetEase Music access.

It's run by Github Actions, so no self-hosted server is needed(This feature is **maintaining**, not available). Alternatively, you can run by local browser cache.  

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
3. Enter your chrome profile path in `local_login.py`, this path is usually `C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data`.    
4. Set the timer for repeating the task.  
5. Run `local_login.py`   

## How it works

When you login to https://music.163.com in Chrome the extension NetEaseMusicWorld+ will automatically run a script to make NetEase believe that your IP is in China. Once this is done, NetEase will allow you to access music in all platforms (e.g. on phone apps) for a short time (unclear) even if you access from a foreign IP.

The Github Action will run daily to do the above actions and unlock you from the foreign IP restriction.  

When you use local browser cache to execute, the script would use the cookie in your local browser to play songs, but you have to manully login the account in advance to obtain the cookie.
