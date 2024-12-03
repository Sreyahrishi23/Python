'''
Author:Sreya Hrishikesh
Date:03-12-2024
Python program to define a module to find Fibonacci numbers and input the module to another program
'''
from calendar import firstweekday


def fibonacci_number(n):
    sequence=[]
    first_no,second_no=0,1
    for i in range(n):
        sequence.append(first_no)
        first_no,second_no=second_no,first_no+second_no
    return sequence

