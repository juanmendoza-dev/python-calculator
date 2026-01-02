#calculator launch 
print("Thank you for using my calculator! I will try to update it with new features ")


num1 = input (int("First number: ")) #prompts user for the first number
sign = input ("sign (eg: +,-,*,/)") #prompts the user for the sign 
num2 = input (int("Second number: ")) #prompts user for the sec number 

#number logic (magic)
if sign == "+":
    print("sum: " + num1 + num2)
elif (sign == "-"):
    print("difference: " + num1 - num2)
elif (sign == "*"):
    print("product: " + num1 * num2)
elif(sign == "/"):
    print("quotient: "+ num1 / num2)
else:
    print("invalid! Please try again!")
    

    