# import string
# w="hello"
# print(w)
# txt = "i can and i will"[::-1]
# print(txt)

# txt1 = "i can and i will"
# x=txt1.replace("i","ketul")
# print(x)

# y=txt1+" "+w
# print(y)

# print(txt1.find("can"))

# print(txt1.split("a"))

# dct={
#     "id":"21dce066",
#     "name":"ce",
#     'department':'CE',
#     'subject':"python",
#     "color":"white"
# }
# print(dct.keys())
# print(dct.values())

# print(dct.get("id"))
# dct.update({"color":"white"})
# print(dct)
# print(dct.pop('name'))
# print(dct)
# print(dct.items())
# del dct["color"]
# print(dct)
# print(dct.clear())


# movie={
#     'name1':'bahubali',
#     'rating':'4.5',
#     '100cr_club':True,
#     'hero':'keval_hingu'
# }

# clg={
#     'name':'DA-IICT',
#     'NAAC':True,
#     "NIRF_RANK":1,
# }

# dct={
#     "id":"21dce066",
#     "name":"ce",
#     'department':'CE',
#     'subject':"python",
#     "color":"white"
# }

# movie.update(clg)
# movie.update(dct)
# print(movie)

# thisdict = {
#   "collage": "depstar",
#   "branch":"ce",
#   "id": "21DCE066",
#   "subject": "python programing",
# }
# print(thisdict)
# #print keys
# key1 = thisdict.keys()
# print(key1)
# #print values
# value1 = thisdict.values()
# print(value1)
# #update element
# thisdict.update({"id":"21dce000"})
# print(thisdict)
# #get element
# get1 = thisdict.get("branch")
# print(get1)
# #del element
# del thisdict["id"]
# print(thisdict)
# #print not pop element
# thisdict.pop("collage","depstar")
# print(thisdict)
# #pop element
# pop1 = thisdict.popitem()
# print(thisdict)
# #clear
# thisdict.clear()
# print(thisdict)
# print("21DCE066")
# # merge
# Dictionary={'A':'harsh'}
# Dictionary1 = {1:'001',2:'010',3:'011'}
# Dictionary2 = {"harsh":7,"parekh":1}
# Dictionary.update(Dictionary1)
# Dictionary.update(Dictionary2)
# print(Dictionary)
# print("21DCE066")


# p=int(input("Enter Principle amount:"))
# r=int(input("Enter rate of interest:"))
# n=int(input("Enter number of years:"))
# i = ((p*n*r)/100)
# print("your interset:"+str(i))
# print("21DCE066")


# L = [2, 1, 3, 5, 4, 3, 8]
# L1 = [10,11,14,12,13]
# L.append(9)
# print("append:",L)
# L.extend(L1)
# print("extend:",L)
# L.remove(5)
# print("remove:",L)
# L.reverse()
# print("reverse:",L)
# L.sort()
# print("ascending order:",L)
# L.sort(reverse=True)
# print("descending order:",L)
# print("21DCE066")

# l=[3,4,5,66,7,22]
# print("original list"+ str(l))
# m=l[:]
# print("copied list"+str(m))
# print("21DCE066")

# list1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]
# List= list1*5
# print("five time print list = ",List)
# print("word Python = ",list1[4][0])
# print("word orenge =",list1[8][2])
# print("20 number =",list1[4][3][1])
# print("21DCE066")


A = (2, 1, 3, 5, 4, 3)

print("sum:",sum(A))
print("min:",min(A))
print("max:",max(A))
print("21DCE066")
