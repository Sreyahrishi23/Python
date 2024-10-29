'''
Author: Sreya
Date: 29-10-2024
Version: 1.0
Python program to extract a student's grade based on thier marks
'''

marks=int(input("Enter your marks:"))
if marks>=90:
    print("Your grade is A")
elif marks>80 and marks<89:
    print("Your grade is B")
elif marks<79 and marks>70:
    print("Your grade is C")
elif marks<69 and marks>60:
    print("Your grade is D")
else:
    print("Your garde is F")