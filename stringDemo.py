'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to check whether the given number is positive or not
Version;3.11.4
'''
number=int(input("Enter a number:"))
if number>0:
    print("The given number:",number,"is positive")
elif number<0:
    print("The given number is negative")
else:
    print("The given number:",number,"is zero")
