import time, os, getpass
USERNAME = getpass.getuser()
def lotprints():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

lotprints()

a = input('Select a language (en) / Выберите язык (ru):')
my_file = open("lang.txt", "w+")
my_file.write(a)
my_file.close()

if a ==  'ru':
    print()
    print('Русский язык установлен')
    print()
    time.sleep(1)
    print('Для использования TSP вам нужет токен телеграм-бота')
    print()
    time.sleep(1)
    ans = input('Вставьте ваш токен:')
    print()
    time.sleep(1)
    print('Ваш токен ', ans, ' был записан.')
    print("")
    my_file = open('cfgtoken.txt', "w+")
    my_file.write(ans)
    my_file.close()
    time.sleep(1)
    print()
    print("Укажите путь до папки с сервером Gmod")
    print("По типу: C:\Gmod_server\steamapps\common\GarrysModDS")
    print()
    serveradress = input('Путь до сервера: ')
    print()
    print(serveradress + " - Путь до вашего сервера" )
    time.sleep(1)
    autorun = input('Вы хотите добавить TSP в авто загрузку? y/n:')
    if autorun == 'y':
        def add_to_startup():
            bath_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start menu\Programs\Startup' % USERNAME
            with open(bath_path + '\\' + 'open.bat', 'w+') as bat_file:
                bat_file.write(r'start "update.py" %s' % serveradress)
                print(bat_file)

        add_to_startup()
    else:
        print('')
        print('Gmod TCP не будет добавлен в автозагрузку')

    os.replace("lang.txt", serveradress+"\lang.txt")
    os.replace("cfgtoken.txt", serveradress + "\cfgtoken.txt")
    os.replace("update.py", serveradress+"update.py")
    print('')
    print('Распаковка файлов сервера прошла успешно')
    time.sleep(10)




else:
    print()
    print('English was selected')
    print()
    time.sleep(1)
    print('You need telegram-bot token to use TSP')
    print()
    time.sleep(1)
    ans = input('Insert your token:')
    time.sleep(1)
    print()
    print('Your token', ans, ' was saved.')
    print("")
    time.sleep(1)
    my_file = open("token.txt", "w+")
    my_file.write(ans)
    my_file.close()
    autorun = input('Do you want to add TSP to autorun? y/n: ')
    if autorun == 'y':
        time.sleep(1)
        print('123')

    else:
        time.sleep(1)
        print('Gmod TCP will not be added to the auto-upload')





time.sleep(3)



