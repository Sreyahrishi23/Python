'''
Author:Sreya Hrishikesh
Date:30-11-2024
Python program to check whether given number is a valid mobile number or not using functions.
'''

def mob_no():
    mob_no=input("Enter your mobile number:")
    if mob_no[0]=="7" or mob_no[0]=="8" or mob_no[0]=="9" and len(mob_no)==10:
        print("The given mobile number is valid")
    else:
        print("The given mobile number is invalid")
mob_no()



