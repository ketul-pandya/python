import math
# def sqr(num):
#     return num*num

# number=int(input("enter the number"))
# ans=sqr(number)
# print(ans)


# def length(str1,str2):
#     return len(str1),len(str2)
#
# str1=input("enter the string")
# str2=input("enter the another string")
# leng=length(str1,str2)
# print(leng)

def square(list):
    for i in range(len(list)):
        # print(math.pow(list[i], 2))
        return [i*i for i in list]
list=[2,4,7,9,10]
list1=square(list)
print(list1)