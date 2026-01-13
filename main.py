import time
from colorama import Fore
from console import console_launcher


#calculator launch 
print(Fore.LIGHTYELLOW_EX + "loading...")
time.sleep(2)
print(Fore.LIGHTMAGENTA_EX + "Thank you for using my calculator! I will try to update it with new features!")
print(Fore.LIGHTMAGENTA_EX + 'Feel free to press "E" to exit!')


def mainLauncher():
    while True:
        num1 =  input(Fore.LIGHTBLUE_EX + "First number: ") #prompts user for the first number
        clean_num1 = num1.strip()
              
        #checks before number logic 
        if clean_num1.lower() == "e" or clean_num1.lower() == "exit":                     
            break                               #kicks the user out from calcualtor
        
        if clean_num1.lower() == "console" or clean_num1 == "cmd": 
            console_launcher()
            continue
                                                  
        #checks
        if clean_num1 == (""):
            print(Fore.LIGHTRED_EX + "number can't be blank!!")
            time.sleep(0.7)
            continue
        
        if clean_num1.isalpha():
            print(Fore.LIGHTRED_EX + "variables are not accepted in v1!")
            continue
    
        
            
        
        num1 = int(clean_num1) #converts num1 back into a integer  (string -------> int)
        
        #sign logic + check 
        sign = input(Fore.LIGHTYELLOW_EX + "sign (+ | - | * | /): ") #prompts the user for the sign 
        if sign == (""):
            print(Fore.LIGHTRED_EX +"sign can't be blank")
            time.sleep(0.7)
            continue
        
        #num2 logic + check 
        num2 = input(Fore.LIGHTBLUE_EX +"Second number: ") #prompts user for the sec number
        clean_num2 = num2.strip()

        if clean_num2 == (""):
            print(Fore.LIGHTRED_EX + "number can't be blank!!")
            time.sleep(0.7)
            continue

        num2 = int(clean_num2) #did the same thing here as before 


#number logic (magic)
        if sign == "+":
            print(f"{Fore.LIGHTGREEN_EX}Sum: {num1 + num2}")
            print("-------------------")
        elif (sign == "-"):
            print(f"{Fore.LIGHTGREEN_EX}Difference: {num1 - num2}")
            print("-------------------")
        elif (sign == "*"):
            print(f"{Fore.LIGHTGREEN_EX}Product: {num1 * num2}")
            print("-------------------")
        elif(sign == "/"):
            print(f"{Fore.LIGHTGREEN_EX}Quotient: {num1 / num2}")
            print("-------------------")
        else:
            print(Fore.LIGHTRED_EX + "invalid! Please try again!")  
            print("-------------------")

#launcher 
mainLauncher() #launches calculator 
print(Fore.LIGHTMAGENTA_EX + "thank you for using my awesome calculator please star on github!")

    #planned updates!
    #TODO: add settings launcher for the user to able adjust things like: auto refresh time, if they want sys memory or na.
    #TODO: add performance mode (delayed refresh, anti spam)
    #TODO: make the calculator launch on a cmd/terminal window 
    #TODO: Advanced styling (RGB Animations for intro and other parts of the calculator)
    #TODO: Make logo for calculator and make it more professional looking such as a official exe file.


    #messed up things 
    #BUG: if the user enters space as num1 the whole program crashes 
    