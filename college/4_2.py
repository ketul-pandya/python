# import math
# num1=int(input("enter the number 1 "))
# num2=int(input("enter the number 2 "))
# num3=int(input("enter the number 3 "))

# print(max(num1,num2,num3))

def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest
a = int(input("Enter first value : "))
b = int(input("Enter second value : "))
c = int(input("Enter third value : "))
result=maximum(a,b,c)
print(result)