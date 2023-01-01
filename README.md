# Gmod-TSCP ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ <img style=right src=https://i.ibb.co/LkBP1Rn/Garry-s-Mod-logo.png alt="drawing" width="45"/>



> A convenient way to work with Garry's mod servers
######Telegram server control panel. This is a special utility for working with servers based on the [Source engine](https://developer.valvesoftware.com/wiki/Source "Source engine") using the [telegram messenger](https://telegram.org "telegram messenger"). It's open source, I will be very glad to receive your feedback to my email *<islavdo.nvrsk@gmail.com>*


######Now it's pre-alpha and this version will not be able to use, but I am in the process of developing and I think that a beta build will be born very soon.


###For correct work, you will need
- Python 3 (the newer the better)
- Some python packages (They are installed automatically, but if errors suddenly occur, you will find a full list of them below)
- Classic Garry's mod server in ***GarrysModDS*** folder with ***srcds.exe*** inside
- Windows 7 and newer
- Internet connection
- Telegram bot with token, which you can get from [@BotFather](https://t.me/BotFather "@BotFather")


###List of existing commands 
| Meaning       | Command |
| ---------     | -----:|
| PC Reboot     | /sysreboot |
| PC Shutdown   | /sysshutdown |
| Check online  | /test     |
| Internet connection  | /inetcond|
| Enable server  | /enableserv|
| Disable server  | /disableserv|
| Reboot server  | /rebootserv|
| CPU, RAM Indicators  | /sysindicators|


###Required python packages

`pip install pyTelegramBotAPI`\n
`pip install keyboard`\n
`pip install speedtest-cli`\n
`pip install Pillow`
`pip install psutil`
`pip install pyscreenshot`


