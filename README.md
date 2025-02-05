# Unlock-NetEaseMusic
### Issue encountered: Login May be intercepted by CAPTCHA, so the script may not working
Use the Chrome extension NetEaseMusicWorld+ to unlock overseas NetEase Music access.

It's run by Github Actions, so no self-hosted server is needed.

## How to run on Github

1. Fork this repository (and star if you like it)
2. In your own repository, enter your email and password as the value of two Github Action repository secrets `EMAIL` and `PASSWORD` .
3. Run Github Action `Unlock-NetEaseMusic` (It will run automatically every day.)

## How to run locally

1. Install python packages: `pip install selenium webdriver_manager `
2. Enter your email address and password in `auto_login.py`
3. Run `auto_login.py`

## How it works

When you login to https://music.163.com in Chrome the extension NetEaseMusicWorld+ will automatically run a script to make NetEase believe that your IP is in China. Once this is done, NetEase will allow you to access music in all platforms (e.g. on phone apps) for a short time (unclear) even if you access from a foreign IP.

The Github Action will run daily to do the above actions and unlock you from the foreign IP restriction.
