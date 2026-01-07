import time
from colorama import Fore


def cal_console():
    print(Fore.LIGHTYELLOW_EX + "loading console...")
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Console Loaded!")
    while True:
        console = input(Fore.LIGHTYELLOW_EX + "Console: ")
        if console == ("restart"):
            print(Fore.LIGHTYELLOW_EX + "Restarting...")
            mainLauncher()
            break


