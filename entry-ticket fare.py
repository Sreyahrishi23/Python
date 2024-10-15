'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to determine the entry-ticket fare in a zoo based on age
Version;3.11.4
'''
Age=int(input("Enter your age:"))
if Age<10:
    print("Fare=7")
elif Age>=10 and Age<60:
    print("Fare=10")
else:
    print("Fare=5")