'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to check whether the given number is an armstrong number or not
Version;3.11.4
'''
number=int(input("Enter a number:"))
armstrong=number
sum=0
while (number>0):
    r=number%10
    number=number//10
    sum=sum=r**3
if sum==armstrong:
    print("Number is armstrong")
else:
    print("Number is not armstrong")
