#before running this make sure to install pyfiglet using the command 'pip install pyfiglet'. 

import pyfiglet
banner=pyfiglet.figlet_format("ONE VARIABLE EQUATION CALCULATOR")
print(banner)
print("IMAGINE YOUR EQUATION IN 'ax + b = c' FORMAT AND ENTER THE CORRESPONDING VALUES")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
x=(c-b)/a
print(x)

