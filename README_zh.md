# Unlock-NetEaseMusic

使用 Chrome 扩展程序 NetEaseMusicWorld++ 解锁海外网易云音乐的访问权限。

本项目通过 Github Actions 运行，无需自建服务器。你也可以通过本地浏览器缓存运行。

## 系统要求  
:white_check_mark:Windows 8.1/10/11 (x64)  
:white_check_mark:Linux（仅支持 X64 CPU）  
:x:MacOS（暂不支持，开发中）  

## 如何在 Github 上运行（首次需要手动登录以获取 Cookie）

1. Fork 本仓库（喜欢的话可以点个 star）  
2. 在你自己的仓库中，将你的配置 json（应为 [`config.json`](./config.json "`config.json`")）作为 Github Action 仓库密钥 `CONFIG` 的值输入。  
3. 运行 Github Action `Unlock-NetEaseMusic`（它会每天自动运行一次。）

## 如何在本地运行

### 通过邮箱和密码运行（海外用户可能会被验证码拦截）
~~1. 安装 Python 依赖包：`pip install -r requirements.txt`~~  
~~2. 在 `auto_login.py` 中输入你的邮箱和密码~~  
~~3. 运行 `auto_login.py`~~   

### 通过本地浏览器缓存运行（推荐）
1. 在本地电脑上打开 Chrome 并登录网易云音乐，然后使用 Chrome 的调试工具查找名为 `MUSIC_U` 的 Cookie，并复制其值备用。  
如果你觉得用调试工具获取 Cookie 有难度，可以通过执行 `python cookie_extract.py` 使用我们的帮助程序自动获取。在这种方式下，你有 30 秒时间用于登录，获取到的 Cookie 会在终端打印出来。
1. 安装 Python 依赖包：`pip install -r requirements.txt`   
2. 通过本地浏览器缓存运行时，[`config.json`](./config.json "`config.json`") 中的 email、password、userDataDir 和 profileName 不再需要，可以随意填写。  
将第 1 步获取到的 login_cookie 填入即可。  
~~在 `config.json` 中填写你的 Chrome 用户配置路径，Windows 下通常为 `C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data`，也可以在 `chrome://version/` 页面找到。~~     

1. 设置定时任务以重复执行。  
2. 运行 `python local_login.py`   

### 通过 Docker 运行
1. 使用 `docker build -t netease .` 构建 Docker 镜像。
2. 按照 [通过本地浏览器缓存运行](#通过本地浏览器缓存运行推荐) 的第 1 步获取登录 Cookie。
3. 在 [`config.json`](./config.json "`config.json`") 中填写配置后，使用 `docker run -v $PWD/config.json:/app/config.json netease` 将json文件挂载到Docker容器中并启动。  

## config.json 模板
支持单用户模式和多用户模式。  
**单用户模式**：  
```json
{
    "userDataDir": "C:\\Users\\YourUser\\AppData\\Local\\Google\\Chrome\\User Data",
    "email": "test",
    "password": "test123",
    "login_cookie": "xxx"
}
```
**多用户模式**：  
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
### PS：多账号模式  
多账号模式下，你需要为每个网易云账号登录并填写对应的 login_cookie。
~~多账号模式下，你需要创建多个 Chrome 配置文件，并在每个配置文件中登录对应账号。然后在 config.json 中填写不同的 profileName。~~

### Cookie 有效期
每次登录获取的 Cookie 有效期大约为 1 个月，并非永久有效。因此，大约每个月需要重新登录获取新的 Cookie。

## 工作原理

当你在 Chrome 浏览器登录 https://music.163.com 时，NetEaseMusicWorld++ 扩展会自动运行脚本，让网易云认为你的 IP 位于中国。这样一来，即使你在海外 IP，网易云也会在所有平台（如手机 App）短时间内允许你访问音乐（具体时长不确定）。

Github Action 会每天自动运行上述操作，帮你解除海外 IP 限制。

当你用本地浏览器缓存运行时，脚本会使用你本地浏览器中的 Cookie 播放歌曲，但你需要提前手动登录账号以获取 Cookie。

## 致谢
本项目 fork 自 [Lennox-Elaphurus/Unlock-NetEaseMusic](https://github.com/Lennox-Elaphurus/Unlock-NetEaseMusic "Lennox-Elaphurus/Unlock-NetEaseMusic")。由于原仓库已归档，我们决定解除 fork 关系以便后续维护，同时也让本仓库能被更多人检索到（因为 fork 仓库默认不会被 GitHub 索引）。