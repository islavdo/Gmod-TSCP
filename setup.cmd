
@echo off


if not exist "D:\Users\%USERNAME%\AppData\Local\Programs\Python" (
start "" data\havenopython.vbs
timeout 5
explorer https://www.python.org/
exit 
)


start cmd.exe /c "py -m pip install --upgrade pip"


start cmd.exe /c "pip install pyTelegramBotAPI"


start cmd.exe /c "pip install keyboard"

start cmd.exe /c "pip install speedtest-cli"

start "" data\setup.py
