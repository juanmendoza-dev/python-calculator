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
            clear()
            time.sleep(2)
            print(Fore.LIGHTGREEN_EX +"calcualtor successfully loaded!")

def console_settings():
      while True:
        print(Fore.LIGHTYELLOW_EX + "Loading settings... ")
        print(Fore.LIGHTYELLOW_EX + "The settings UI is currently under construction!")
        time.sleep(2)
        print(Fore.LIGHTGREEN_EX + "Settings UI successfully loaded! ")
        time.sleep(1)
        
        print(Fore.LIGHTMAGENTA_EX + "1. In construction (placeholder)")
        print(Fore.LIGHTMAGENTA_EX + "2. Back to console")
        print(Fore.LIGHTMAGENTA_EX + "3. Back to calcualtor!")
        setting_choice = input(Fore.LIGHTYELLOW_EX + "What would you like to do?: ")

        # choice logic (settings)
        if setting_choice == ("1"):
            print(Fore.LIGHTRED_EX + "currently under construction...")
            continue
        elif (setting_choice == "2"):
             print(Fore.LIGHTYELLOW_EX + "Fetching Console...")
             time.sleep(1)
             console_logic()
        elif(setting_choice == "3"):
             print(Fore.LIGHTYELLOW_EX + "Loading Calcualtor...")
             time.sleep(2)
             break
def super_helper():
     while True:
          print(Fore.LIGHTYELLOW_EX + "Loading...") 
          print(Fore.LIGHTMAGENTA_EX + "Sorry you are having issues, Here are all the commands!")
          time.sleep(1)
          print(Fore.LIGHTMAGENTA_EX + "Commands:")
          print(Fore.LIGHTCYAN_EX + "1. Help")     
          print(Fore.LIGHTCYAN_EX + "2. Console/cmd")     
          print(Fore.LIGHTCYAN_EX + "3. restart")
          print(Fore.LIGHTCYAN_EX + "4. clear")
          print(Fore.LIGHTCYAN_EX + "5. back")
          byebye = input("Y/N: Exit now?")

          if byebye == "y" or byebye == "Y":
               print(Fore.LIGHTYELLOW_EX + "loading...")
               console_logic()
               break
          elif(byebye == "n" or byebye == "N"):
               super_helper()
               break
          else:
               print(Fore.LIGHTRED_EX + "Invalid Character y/n")
               continue

def settings_helper():
     while True:
          print(Fore.LIGHTYELLOW_EX + "fetching user settings...")
          time.sleep(2)
          print(Fore.LIGHTGREEN_EX + "Success!!")
          time.sleep(1)
          print(Fore.LIGHTMAGENTA_EX + "Settings UI")
          print(Fore.LIGHTMAGENTA_EX + "1.Performance Mode")
          print(Fore.LIGHTMAGENTA_EX + "2.Fast Math")
          print(Fore.LIGHTMAGENTA_EX + "3.Kill program ")
          settings_choice = input(Fore.LIGHTYELLOW_EX + "What would you like to do?: ")
          
          if settings_choice == "1" or settings_choice == "Performance mode" or settings_choice == "performance mode":
               print(Fore.LIGHTYELLOW_EX + "Applying Performance Patch...")
               time.sleep(2)
               print(Fore.LIGHTGREEN_EX +"Performance Mode activated!")

        

def clear():
     print("\n"*50) #prints a bunch of lines (fake restart or clear)
          
        


#console logic!! brains of the op
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
            elif (console == "settings"):
                 console_settings()
                 break
            elif(console == "help"):
                 super_helper()
            elif console == "cmd" or console == "console":
                 print(Fore.LIGHTRED_EX +"already in the console!!")
                 continue
            elif console == "clear":
                 clear()
                 console_launcher()
                 
                

            else:
                print(Fore.LIGHTRED_EX + "invalid input!")   
                continue
    
def go_back():
    return

go_back()





            


#planned updates
#TODO: add error if user already in console 