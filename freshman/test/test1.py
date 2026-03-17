# import string
# import time
# def gradual2_print(text.txt):
#     lowercase_alphabet = list(string.ascii_lowercase)
#     Punctation_mark = list(string.punctuation)
#     Full_Characters = lowercase_alphabet + Punctation_mark
#     i = x = 0
#     Words = list(text.txt)  # 你需要print的words
#     length = len(Words)
#     while x < length:
#         while i < 57:
#             Printing_number = Full_Characters[i]  # 快速通过的字母+符号
#             b = Words[:x]  # 需要的字母前x-1位
#             c = Words[x]  # 需要的字母第x位
#             d = [s.lower() for s in c]  # 全部小写再根据原本大写
#             e = ','.join(map(str, d))
#             if ' ' in c:
#                 time.sleep(0.05)
#                 print(" ",end="",flush=True)
#                 break
#             else:
#                 if Printing_number == e:
#                     print(c,end="",flush=True)
#                     time.sleep(0.05)
#                     break
#                 else:
#                     print(Printing_number,end="")
#                     time.sleep(0.05)
#                     print("\b",end="",flush=True)
#             i = i + 1
#         i = 0
#         x = x + 1
#     print()
# gradual2_print("What is your name?")
# name=input()
# gradual2_print("Hello!")
# print("\r",end="")
# gradual2_print(name)
# gradual2_print("Whats ur weight?")
# weight=input()
# gradual2_print("Okay....and ur height?")
# height=input()
import string

# a=6
# # while 10:
#
#     # print("c")
# while a:
#     print(a)
#     if a == 1:
#         print("b")
#         break

# #     a=a-1
#
# import string
#
# # lowercase_alphabet = list(string.ascii_lowercase)
# # Punctation_mark = list(string.punctuation)
# # Full_Characters = lowercase_alphabet + Punctation_mark
# # for num1, num2 in zip(Full_Characters,Full_Characters):
# #    print(num1, num2)
# a = input()
# b = input()
# # # print(a * 10)
# # # print(eval(a+b))
# # for i in range(100,1,-2):
# #     print(i)
# #     if i == 50:
# #         return i
# # def osppd(text.txt):
# list=[" "," "]
# if list[0]==" ":
#     print("12")
# try:
# # 可能出错的代码
#     num = int(input("请输入一个数字: "))
#     result = 10 / num
#     print(f"结果是: {result}")
#
# except ValueError:
#     print("错误：请输入有效的数字！")
# except ZeroDivisionError:
#     print("错误：不能除以零！")
# except Exception as e:
#     print(f"发生了未知错误: {e}")
# else:
#     print("计算成功完成！")
# finally:
#     print("程序执行结束。")
# f=open("text.txt")
# for i in f:
#     print(i)
#     if not f:
# #         break
# # f.close()
# f = open("words.txt","r")
# lines = f.readlines()
# for line in lines:
#     line = line.strip()
#     print(line)
# # price= 6.8772
# # print("Total: {0:.2f}".format(price))
# import time
# def gradual_typing(text, speed=0.01.txt):
#     lowercase_alphabet = list(string.ascii_lowercase)
#     punctation_mark = list(string.punctuation)
#     full_characters = lowercase_alphabet + punctation_mark
#     i = x = 0
#     words = list(text)  # 你需要print的words
#     length = len(words)
#     while x < length:
#         while i < 57:
#             printing_number = full_characters[i]  # 快速通过的字母+符号
#             c = words[x]  # 需要的字母第x位
#             d = [s.lower() for s in c]  # 全部小写再根据原本大写
#             e = ','.join(map(str, d))   # 将列表转换回字符
#             if ' ' in c:
#                 time.sleep(speed)
#                 print(" ",end="",flush=True)
#                 break
#             else:
#                 if printing_number == e:
#                     print(c,end="",flush=True)
#                     time.sleep(speed)
#                     break
#                 else:
#                     print(printing_number,end="")
#                     time.sleep(speed)
#                     print("\b",end="",flush=True)
#             i = i + 1
#         i = 0
#         x = x + 1
#     print()
# def test_choice():
#     guess_time=0
#     while guess_time<=3:
#         try:
#             choice = int(input())
#             if 1<= choice <= 4:
#                 guess_time = 3
#                 return choice
#             else:
#                 print("Please enter a valid choice.")
#                 guess_time = guess_time + 1
#         except:
#             if guess_time >= 2:
#                 gradual_typing("No way, you write wrong again", 0.002)
#                 gradual_typing("so, u dont like that number", 0.002)
#                 gradual_typing("don't worry, I can start it for you", 0.002)
#                 gradual_typing("--playing dumb mode--")
#                 global dumb_mode
#                 dumb_mode = True
#                 return 1
#             else:
#                 gradual_typing("it seems like you didn't enter a number")
#                 gradual_typing("please try again:D")
#                 guess_time=guess_time+1
#
# print("开始")
# test_choice()
# class Person:
#     def __init__(self, name,age):
#         self.age = age
#         self.name = name
# Person(name='zhangsan', age=18)
# print(Person.age)
#
# def tallest(c):
#     a=0
#     for i in c:
#         if i.weight<c[a].weight:
#             a=i
#     return c[a]
# class person:
#     def __init__(self,height,weight):
#         self.height=height
#         self.weight=weight
#     def __str__(self):
#         return str(self.height)+"."+str(self.weight)
#     def __repr__(self):
#         return str(self.height)+"."+str(self.weight)
# pe=person
# l=[person(180,18)]
# print(l)


# def read_2D_list(a):
#     with open(a, "r") as f:
#         lines = f.readlines()
#         i = 1
#         whole = []
#         while i < len(lines):
#             line = lines[i]
#             i += 1
#             b = []
#             for x in line.split():
#                 b.append(int(x))
#             whole.append(b)
#     print(whole)
#     return whole
# def add_one(a):
#     for row in a:
#         for i in range(len(row)):
#             row[i] += 1
#
# numbers = read_2D_list("01.txt")
# add_one(numbers)
# for row in numbers:
#     for num in row:
#         print(num, end=" ")
#     print()


