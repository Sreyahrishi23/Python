'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to determine the smallest of three numbers
Version;3.11.4
'''
num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if num1>num2 and num3>num2:
    print("num2 is the smallest number")
elif num2>num3 and num1>num3:
    print("num3 is the smallest number")
else:
    print("num1 is the smallest number")