'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to calculate the sum of the digits of a number
Version;3.11.4
'''
number=int(input("Enter a number:"))
sum=0
while number>0:
    remainder=number%10
    number=number//10
    sum=sum+remainder
print(sum)