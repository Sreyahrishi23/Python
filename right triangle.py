'''
Author:Sreya Hrishikesh
Date:30-11-2024
Python program to check if the given sides make a right triangle
'''
def right_triangle():
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False

side1=int(input("Enter a side"))
side2=int(input("Enter a side"))
side3=int(input("Enter a side"))
if right_triangle():
    print(f"The given sides are of a right triangle")
else:
    print(f"The given sides are not of a right triangle")
