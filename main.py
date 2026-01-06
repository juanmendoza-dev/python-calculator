from colorama import Fore 

#calculator launch 
print(Fore.LIGHTMAGENTA_EX + "Thank you for using my calculator! I will try to update it with new features!")
print(Fore.LIGHTMAGENTA_EX + 'Feel free to press "E" to exit!')


def mainLauncher():
    while True:
        num1 =  input(Fore.LIGHTBLUE_EX + "First number: ") #prompts user for the first number
        clean_num1 = num1.strip()
        
            
        #checks before number logic 
        if clean_num1.lower() == "e":                     
            break                               #kicks the user out from calcualtor
        

            
        
        num1 = int(clean_num1) #converts num1 back into a integer  (string -------> int)
        sign = input(Fore.LIGHTYELLOW_EX + "sign (+ | - | * | /): ") #prompts the user for the sign 
        num2 = int(input(Fore.LIGHTBLUE_EX +"Second number: ")) #prompts user for the sec number
     


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
    #TODO: fix user putting in random letter instead of number (checks)
    #TODO: add settings launcher for the user to able adjust things like: auto refresh time, if they want sys memory or na.
    #TODO: add performance mode (delayed refresh, anti spam)
    #TODO: make the calculator launch on a cmd/terminal window 
    #TODO: Advanced styling (RGB Animations for intro and other parts of the calculator)
    #TODO: Make logo for calculator and make it more professional looking such as a official exe file.


    #messed up things 
    #BUG: if the user enters space as num1 the whole program crashes 
    