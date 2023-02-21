# list = [1,2,3,4,5,6,7,8,9,10]  
# n = 2  
# for i in list:  
#     x = n*i  
#     print(x)

# i=1   
# while(i<=10):    
#     print(i)    
#     i=i+1    
# else:  
#     print("The while loop exhausted")  


# c=list(range(3, 8))
# print(c)

# from random import random
# a=0.1
# b=0.9
# i=0
# while i<10_000:
#     n=random()
#     if n<a:
#         a=n
#     elif n>b:
#         b=n 
#     i +=1
# print ("%.16f"%a)
# print(b)

# import random 
# a=10 
# b=100 
# for i in range(5): 
#     print(random.randint(a, b))

# import random

# random_number = random.randrange(1, 100, 5)
# print(random_number)


# задача 1
# a = int (input())
# b = int(input())
# for i in range(a, b+1):
#     print(i)

# задача 2
# a = int (input())
# b = int(input())
# if a<b:
#     for i in range(a, b+1):
#         print(i)
# else:
#     for i in range(a, b -1, -1):
#         print(i)

# задача3
a = int (input())
b = int(input())
for i in range(a - (a+1) % 2, b - b % 2, -2):
    print(i, end=' ')


