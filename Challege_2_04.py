# Challenge_1
# number = int(input("Please enter a number:\t"))
# for i in range(number):
#     print(i**2)

# Challenge_2
# def is_leap(year):
#     leap = False
#     if year % 4 == 0:
#         if year % 100 != 0:
#             if year % 400 == 0:
#                 leap = leap
#             else:
#                 leap = not leap
#         elif year % 100 == 0:
#             if year % 400 == 0:
#                 leap = not leap
#             else:
#                 leap = leap
#
#     return leap
#
# year = 1992
# print(is_leap(year))

# Challenge 4
# n = int(input())
# n1 = range(1,n+1)
# n3 = ''
# for n2 in n1:
#     n3 += str(n2)
#     n4 = ''.join(n3)
#
# print(n4)

# Challenge_5
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# i = range(0,x+1)
# j = range(0,y+1)
# k = range(0,z+1)
# tol = []
# for a in range(0,x+1):
#     for b in range(0,y+1):
#         for c in range(0,z+1):
#             if a+b+c == n:
#                 continue
#             else:
#                 tol += [[a,b,c]]
#
# print(tol)

# -----------------------------------------------------
# Splitting numbers in a list Method # 1
# n3 = ""
# for n2 in numm:
#     n3 += str(n2)
#     n4 = ' '.join(n3)

# Splitting numbers in a list Method # 2
# s = input()
# numbers = list(map(int, s.split()))

# Splitting numbers in a list Method # 3
# a = [int(x) for x in input().split()]
# print(a)
# -----------------------------------------------------


# Challenge 6
# p = int(input())
# a = [int(x) for x in input().split()]
# maxxy = max(a)
# new=[]
# new1=[]
# for num in a:
#     if num < maxxy:
#         new = new1.append(num)
# print(max(new1))


# Challenge 7
# stu = []
# scorey = []
# final = []
# final2 = []
# i = range(int(input()))
# for _ in i:
#     name = input()
#     score = float(input())
#     stu.append([name,score])
#     scorey.append(score)
# for n in scorey:
#     minny = min(scorey)
#     if n != minny:
#         final.append(n)
#         final2 = sorted(final)
# for a, c in sorted(stu):
#     if c == final2[0]:
#         print("{}".format(a))

# Challenge 8
# n = int(input())
# students = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     students[name] = scores
# query_name = input()
# for student in students:
#     if query_name == student:
#         sele_stu = students[query_name]
#         lenny = float(len(sele_stu))
#         average = sum(sele_stu) / lenny
#         print("%.2f" % average)

# Challenge 9
# N = int(input())
# while N <= range(N):


# Revision on Classes
# class User():
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#
#     def greeting(self):
#         return (f"My name is {self.name} and I am {self.age} years old!")
#
#
# class Customer(User):
#     def __init__(self, name, email, age):
#         self.name = name
#         self.email = email
#         self.age = age
#         self.balance = 0
#
#     def set_balance(self, balance):
#         self.balance = balance
#
#     def greeting(self):
#         return (f"My name is {self.name} and I am {self.age} years old! I weigh an amazing {self.balance} pounds")
#
# # el = User('Elvis','el@gmail.com',32)
# # print(el.greeting())
# es = Customer('Easter','esa@gmail.com',43)
# es.set_balance(652)
# print(es.greeting())