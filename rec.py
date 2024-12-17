def add_numbers(n1,n2):
    if n2==0:
        return n1
    else:
        result=add_numbers(n1+1,n2-1)
    return result
n1=int(input("Enter a no:"))
n2=int(input("Enter a no:"))
print(add_numbers(n1,n2))
