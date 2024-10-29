'''
Author: Sreya
Date: 29-10-2024
Version: 1.0
Python program to check whether the given number is prime or not
'''
check_prime=int(input("Enter a number"))
s="Prime"
for i in range(2,(check_prime//2)+1):
    if check_prime%i==0:
        print("Not prime")
print(s)