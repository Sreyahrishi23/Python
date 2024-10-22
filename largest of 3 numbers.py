'''
Date:20-10-2024
Author:Sreya Hrishikesh
Python program to find the largest of three numbers
Version;3.11.4
'''

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if num2<num1 and num3<num1:
    print("The largest number is:",num1)
elif num1<num2 and num3<num2:
    print("The largest number is:",num2)
else:
    print("The largest number is:",num3)