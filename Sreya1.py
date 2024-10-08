'''
Author: Sreya
Date: 08-10-2024
Version: 1.0
Create, concatenate, and print a string and access a sub-string from a given string.
'''

first_name="Sreya"
last_name="Hrishikesh"
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
print(length)
extracted_first_name=full_name[length+1:]
print(extracted_first_name)