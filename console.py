import time
from colorama import Fore


def cal_console():
    print(Fore.LIGHTYELLOW_EX + "loading console...") #2 sec load time for console
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Console Loaded!")
    while True:
        console = input(Fore.LIGHTYELLOW_EX + "Console: ")
        if console == ("restart"):
            print(Fore.LIGHTYELLOW_EX + "Restarting...") #restarts console
            mainLauncher()
            break


#planned updates for console
#TODO: Add settings bar 
#TODO: Performance mode 
#TODO: quick maths 