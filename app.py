

# items = [10,20,"hello",30,40,50,60,70]

# a,b,*c = items
# print(a)
# print(b)
# print(c)

# cities = ["delhi","mumbai","chennai"]

# for city in range(len(cities)):
#     print(cities[city],city)

# for city in enumerate(cities):
#     print(city)

# for city in enumerate(cities):
#     print(city[0]," ",city[1])

# for index,city in enumerate(cities):
#     print(index," ",city)

# chars = list("welome")

# print(chars)

# num = list(range(20))
# print(num)

# num = [4,7,2,1,9,8]

# new = sorted(num) #creates new list

# print(num)
# print(new)

# products = [
#     ("product1",50),
#     ("product2",12),
#     ("product3",5),
#     ("product4",30)
# ]

# def sort_item(item):
#     return item[1]

# products.sort(key=sort_item)

# print(products)


# students = [
#     {"roll":10,"name":"Raj","marks":800},
#     {"roll":12,"name":"Saj","marks":820},
#     {"roll":14,"name":"Rlaj","marks":700},
#     {"roll":16,"name":"Suaj","marks":720}
# ]

# students.sort(key= lambda student:student["name"],reverse=True)

# for student in students:
#     print(student)

# from newmath import *


# from newmath import add,product as multiply

# add(10,20)
# product(17,14)

# print(nm.x)

# nm.add(2,3)

# nm.product(23,3)

# import newmath #newmath would run its contents 1 time
# import sys
# print("welcome to python web dev")

# # print(dir(newmath))
# print(sys.path)




# # newmath.__name__

import random



# print(random.random())
# #here we get a floating point number between 0 and 1

# print(random.randint(1,10)) 
# #this method will generate a random number between 1 and 10

# print(random.choice([1,2,3,5,8,15,10])) 
# # this method will generate a random number from the given list values

# print(random.choices([1,2,3,5,8,15,10], k=2)) 
# # this method will generate 2 random number from the given list, if we provide k(keyword # value) as 3 then it will generate 3 numbers inside a list

# str = "".join(random.choices("AARYAMAN", k=8))
              
# print(str)

# print(random.choices("abcdefghi", k=4)) 
# # it will generate a random list of 4 character each time

 
# str = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=4))

# str = "".join(random.choices("1234567890", k=4)) 
# #here comma will be joined

# print(str)

# import string
# import random

# str = "".join(random.choices(string.ascii_letters + string.digits, k=8))

# print(str)


# colors = ["red","blue","green"]

# random.shuffle(colors)
# print(colors)

# import requests

# response=requests.get("https://google.com")

# print(response)

