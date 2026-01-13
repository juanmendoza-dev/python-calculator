import time
from colorama import Fore

#console launcher
def console_launcher():
    print(Fore.LIGHTYELLOW_EX + "loading console...") #2 sec load time for console
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "Console Loaded!")
    console_logic()

    #restart console function
def console_restart():
            print(Fore.LIGHTYELLOW_EX + "Restarting...") #restarts console
            print(Fore.LIGHTYELLOW_EX + "-------------------")
            time.sleep(2)
            print(Fore.LIGHTGREEN_EX +"calcualtor sucessfulley loaded!")
            
  
def console_logic():
        while True:
            console = input(Fore.LIGHTYELLOW_EX + "Console: ")
            if console == ("restart"):
                console_restart()
                break
            elif (console == "back"):
                print(Fore.LIGHTYELLOW_EX +"returing to calcualtor...")
                time.sleep(1)
                print(Fore.LIGHTGREEN_EX + "success!!!!")
                break
                

            else:
                print(Fore.LIGHTRED_EX + "invalid input!")   
    
def go_back():
    return

go_back()





            


#planned updates
#TODO: add the restart function