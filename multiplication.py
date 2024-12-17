def product_numbers(n1,n2):
    if n2==1:
        return n1
    else:
        result=n1+product_numbers(n1,n2-1)
    return result
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
product_numbers(n1,n2)
print(product_numbers(n1,n2))