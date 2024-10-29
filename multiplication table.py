'''
Author: Sreya
Date: 29-10-2024
Version: 1.0
Python program to extract a number's multiplication table upto 12
'''

num=int(input("Enter a number"))
for i in range(1,13):
    x=num*i
    print(f"{num}*{i}={x}")