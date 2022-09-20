import telebot, os, time, keyboard, speedtest
from telebot import types

keyboard.press("Win")
keyboard.press("Shift")
keyboard.press("Z")
keyboard.release("Win")
keyboard.release("Shift")
keyboard.release("Z")




bot = telebot.TeleBot('5253945013:AAF6yqBKUkKr2ENj0c8yBHfjujulEFglCnQ');
startfile = open('start.bat', encoding='utf-8')




mainkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton("/test")
btn2 = types.KeyboardButton("/start_server")
btn3 = types.KeyboardButton("/internet_speed")
btn4 = types.KeyboardButton("/reboot")
btn5 = types.KeyboardButton("/shutdown_server")
btn6 = types.KeyboardButton("/reboot_pc")
mainkeyboard.add(btn1, btn2, btn3, btn4,btn5,btn6)





@bot.message_handler(commands=['test'])
def welcome_start(message):
    tym = time.localtime()
    opt = time.strftime("%d/%m/%Y, %H:%M:%S",tym)
    bot.send_message(message.chat.id, 'Добро пожаловать! Телеграм бот запущен. \n\nДата и время опроса: ' + opt, reply_markup=mainkeyboard)



@bot.message_handler(commands=['reboot_pc'])
def welcome_start(message):
    tym = time.localtime()
    opt = time.strftime("%d/%m/%Y, %H:%M:%S",tym)
    bot.send_message(message.chat.id, 'Перезагрузка... \n\nДата и время перезагрузки: ' + opt, reply_markup=mainkeyboard)
    os.system("shutdown /r /t 00")



@bot.message_handler(commands=['start_server'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Сервер запускается, подождите...')
    os.system("start.bat")
    time.sleep(2)
    keyboard.press("Win")
    keyboard.press("Shift")
    keyboard.press("Z")
    keyboard.release("Win")
    keyboard.release("Shift")
    keyboard.release("Z")

@bot.message_handler(commands=['shutdown_server'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Сервер выключается, подождите...')
    os.system("TASKKILL /F /IM srcds.exe")
    bot.send_message(message.chat.id, 'Сервер выключен')




@bot.message_handler(commands=['reboot'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Сервер перезапускается')
    time.sleep(3)
    os.system("TASKKILL /F /IM srcds.exe")
    bot.send_message(message.chat.id, "Сервер выключен")
    time.sleep(10)
    os.system("start.bat")
    time.sleep(3)
    bot.send_message(message.chat.id, "Сервер в процессе запуска...")
    time.sleep(15)
    bot.send_message(message.chat.id, "Сервер запущен")


@bot.message_handler(commands=['internet_speed'])
def welcome_help(message):
    bot.send_message(message.chat.id, 'Подождите... \nПроводятся замеры скорости интернета')
    test = speedtest.Speedtest()


    speeddownload = test.download()
    speeddownloadnormal = (speeddownload / 1024) / 1024

    if round(speeddownloadnormal,2) > 90:
        bot.send_message(message.chat.id, 'Скорость загрузки идеальная' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')
    elif round(speeddownloadnormal,2) > 70:
        bot.send_message(message.chat.id, 'Скорость загрузки отличная' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')
    elif round(speeddownloadnormal, 2) > 50:
        bot.send_message(message.chat.id, 'Скорость загрузки хорошая' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')
    elif round(speeddownloadnormal, 2) > 30:
        bot.send_message(message.chat.id, 'Скорость загрузки нормальная' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')
    elif round(speeddownloadnormal, 2) > 20:
        bot.send_message(message.chat.id, 'Скорость загрузки удавлетворительная' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')
    elif round(speeddownloadnormal, 2) > 10:
        bot.send_message(message.chat.id, 'Скорость загрузки не удавлетворительная' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')
    elif round(speeddownloadnormal, 2) > 5:
        bot.send_message(message.chat.id, 'Возможность загрузки практически отсутствует' f'\nᅠ \n⬆️ Скорость загрузки {round(speeddownloadnormal,2)} Mb/s ⬇️\nᅠ ')




    speedupload = test.upload()
    speeduploadnormal = (speedupload / 1024) / 1024
    if round(speeduploadnormal, 2) > 90:
        bot.send_message(message.chat.id, 'Скорость выгрузки идеальная' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')
    elif round(speeduploadnormal, 2) > 70:
        bot.send_message(message.chat.id, 'Скорость выгрузки отличная' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')
    elif round(speeduploadnormal, 2) > 50:
        bot.send_message(message.chat.id, 'Скорость выгрузки хорошая' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')
    elif round(speeduploadnormal, 2) > 30:
        bot.send_message(message.chat.id, 'Скорость выгрузки нормальная' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')
    elif round(speeduploadnormal, 2) > 20:
        bot.send_message(message.chat.id, 'Скорость выгрузки удавлетворительная' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')
    elif round(speeduploadnormal, 2) > 10:
        bot.send_message(message.chat.id, 'Скорость выгрузки не удавлетворительна' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')
    elif round(speeduploadnormal, 2) > 5:
        bot.send_message(message.chat.id, 'Возможность выгрузки практически отсутствует' f'\nᅠ \n⬆️ Скорость выгрузки {round(speeduploadnormal,2)} Mb/s ⬆️\nᅠ ')






bot.polling()  # запускаем бота
