'''
Author: Sreya
Date: 29-10-2024
Version: 1.0
Python program to check if the given number is prime or not
'''

check_prime=int(input("Enter a number:"))
for i in range(2,(check_prime//2)+1):
    print(f"value of i {i} and {check_prime}%{1}={check_prime%i}")
    if check_prime%i==0:
        break
if i==(check_prime//2):
    print(f"The given number {check_prime} is prime")
else:
    print(f"The given number {check_prime} is not a prime")