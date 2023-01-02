strin=input("enter the string")

def check(str):
    count1 = 0
    count2 = 0
    for i in str:
        if i.islower():
            count1=count1+1
        else:
            count2=count2+1
    print(count1)
    print(count2)
check(strin)

