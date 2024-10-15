'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to generate n odd numbers
Version;3.11.4
'''
limit=int(input("Enter the limit:"))
odd_number=1
count=0
while count<limit:
    print(odd_number,"\t",end="")
    count+=1
    odd_number+=2
