'''
Date:15-10-2024
Author:Sreya Hrishikesh
Python program to apply discount based on the total purchase amount
Version;3.11.4
'''
purchase_amount=int(input("Enter the purchase_amount:"))
if purchase_amount>500:
    discount=purchase_amount*0.20
    final_amount=purchase_amount-discount
    print(final_amount)
elif purchase_amount>=200 and purchase_amount<=500:
    discount=purchase_amount*0.10
    final_amount=purchase_amount-discount
    print(final_amount)
else:
    discount=0
    final_amount=purchase_amount-discount
    print(final_amount)