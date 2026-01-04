from colorama import Fore 

#calculator launch 
print(Fore.LIGHTMAGENTA_EX + "Thank you for using my calculator! I will try to update it with new features!")
print(Fore.LIGHTMAGENTA_EX) + 'Feel free to press "P" to quit!' 


def mainLauncher():
    num1 =  int(input(Fore.LIGHTBLUE_EX + "First number: ")) #prompts user for the first number
    sign = input(Fore.LIGHTYELLOW_EX + "sign (eg: + | - | * | /): ") #prompts the user for the sign 
    num2 = int(input(Fore.LIGHTBLUE_EX +"Second number: ")) #prompts user for the sec number 

#number logic (magic)
    if sign == "+":
        print(f"{Fore.LIGHTGREEN_EX}Sum: {num1 + num2}")
    elif (sign == "-"):
        print(f"{Fore.LIGHTGREEN_EX}Difference: {num1 - num2}")
    elif (sign == "*"):
        print(f"{Fore.LIGHTGREEN_EX}Product: {num1 * num2}")
    elif(sign == "/"):
        print(f"{Fore.LIGHTGREEN_EX}Quotient: {num1 / num2}")
    else:
        print(Fore.LIGHTRED_EX + "invalid! Please try again!")   

#launcher 
mainLauncher()


    #planned updates!
    #TODO: add auto refresh (after a 2-3 secs make the page reset back the first prompt)
    #TODO: add memory system! (make the user be able to go back to previous outputs)
    #TODO: add settings launcher for the user to able adjust things like: auto refresh time, if they want sys memory or na.
    #TODO: make the calculator launch on a cmd/terminal window 
    #TODO: Advanced styling (RGB Animations for intro and other parts of the calculator)
    #TODO: Make logo for calculator and make it more professional looking such as a official exe file.

    