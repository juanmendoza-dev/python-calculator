import time
from colorama import Fore

#console launcher
def console_launcher():
    print(Fore.LIGHTYELLOW_EX + "loading console...") #2 sec load time for console
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Console Loaded!")

    #restart console function
def console_restart():
            print(Fore.LIGHTYELLOW_EX + "Restarting...") #restarts console
            print(Fore.LIGHTYELLOW_EX + "-------------------")
            time.sleep(2)
            print(Fore.LIGHTGREEN_EX +"calcualtor sucessfulley loaded!")
            return
    
while True:
    console = input(Fore.LIGHTYELLOW_EX + "Console: ")
    if console == ("restart"):
           console_restart()
    elif (console == "back"):
           print("still working on this!")
    else:
           print("invalid input!")
           
           
    
    





            


#planned updates
#TODO: add the restart function