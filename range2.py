'''
Author: Sreya
Date: 29-10-2024
Version: 1.0
Python program to find n prime numbers
'''

limit=10
for number in range(2,limit+1):
    isPrime=True
    for i in range(2,(number//2)+1):
        if number%i==0:
            isPrime=False
    if isPrime:
        print(number)