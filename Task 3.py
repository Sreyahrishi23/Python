'''
Author:Sreya
Date:07-10-2024
Write a Python program that demonstrates the usage of arithmentic,comparison and logical operators,perform a few operations and print the results
Version:3.11.4
'''
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
sum=num1+num2
division=num1/num2
print("sum=",sum,"division=",division)
print("is",num1,"greater than",num2,"?",num1>num2)
print("are",num1,"and",num2,"equal?",num1==num2)
print("logical AND:",num1>num2 and num2<num1)
print("logical OR:",num1>num2 or num2>num1)