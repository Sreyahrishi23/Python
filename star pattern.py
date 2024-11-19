'''
Author:Sreya Hrishikesh
Date:19-11-2024
Python program to construct patterns of stars(*) using a nested for loop
'''

#Increasing triangle
a="*"
row=int(input("Enter number of rows:"))
for i in range(1,row+1):
    for j in range(i):
        print(a,end="")
    print()

#Decreasing triangle
b="*"
row=int(input("Enter number of rows:"))
for i in range(row,0,-1):
    for j in range(i):
        print(b,end="")
    print()

#Hill pattern
c="*"
row=int(input("Enter number of rows:"))
for i in range(1,row+1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

#Reverse hill pattern
d="*"
row=int(input("Enter number of rows:"))
for i in range(row,0,-1):
    for j in range(row-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()