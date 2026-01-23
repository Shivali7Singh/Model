# import SS
# print(SS.add(6,8))
# print(SS.hello)


# import math
# print(math.sqrt(9))
# print(math.pi)
# print(math.pow(2,4))
# print(math.factorial(5))

#DATETIME MODULE(IN BILED)
# import datetime
# now = datetime.datetime.now()
# print(now)
# print(now.year)
# print(now.month)
# print(now.day)

# today = datetime.date.today()
# print(today)
# future =today+datetime.timedelta(days=15)
# print(future)

#SYSTEM MODULE
# import sys
# print(sys.version)
# print(sys.executable)
# print(sys.platform)

#RANDOM MODULE
# import random
# print(random.randint(1,10))
# print(random.random())
# print(random.choice(["AIPA","COPA","CSA"]))

# trade =["AI","COPA","EM","DM"]
# random.shuffle(trade)
# print(trade)

#OS MODULE
# import os
# # print(os.getcwd())
# print(os.listdir())
# os.mkdir("AIPA")
# os.rmdir("AIPA")

# import time
# import time
# print(time.ctime())
# time.sleep(5)
# print("after 5sec")

#practice
# import math
# x = pow(3,6)
# print(math.pi*x)

# print(math.factorial(int(input("enter factorial num:"))))
# print(math.sqrt(int(input("enter sqrt num:"))))

# import random
# # print("and the number is:",random.choices([1,2,3,4,5,6,7,8,9]))

# # def guessing_game():
# x = int(input("Guess a number beetwen 1 and 10:"))
# print(random.randint(1,10))

# import time
# print(time.ctime())

# import datetime
# today = datetime.date.today()
# # print(today)
# past = today-datetime.timedelta(days=10)
# print(past)
# future =today+datetime.timedelta(days=10)
# print(future)

# import datetime
# import calendar
# day_names=datetime.date.today().weekday()
# day_name=calendar.day_name[day_names]
# print(day_name)

# Exceptional Handling:
# try:
#     a=5
#     b=int(input("number"))
#     print(a/b)
# except ZeroDivisionError:
#     print("no can't be divided by 0")
# x=10
# y=9
# print(x-y)

# try:
#     x=int(input("enter no"))
#     print(10/x)
# except ZeroDivisionError:
#     print("can't divide by 0")
# except ValueError:
#     print("can't divide by string")
# else:
#     print("The input was:",x)
# finally:
#     print("All code done")

# #Index Error:
# x=["A","B","C","D"]
# print(x[5])

#Name Error:
# trade="AIPA"
# print(trade)
                                                
#Logical Error:
# a=(1,2,3,4,5,6,7)
# b=len(a)/sum(a)
# print(b)

#AttributeError:
# x="shivali"
# x.upper()
# print(x)


# class nstiadmission(Exception):
#     pass
# try:
#     x=int(input("enter qulification"))
#     if x<12:
#         raise nstiadmission("you are not eligible for admission")
#     else:
#         print("you are eligible for admission")
# except nstiadmission as shivali:
#     print("reason:",shivali)

# class invalidnumber(Exception):
#     pass
# try:
#     a=input("Enter your aadhar no:")
#     if len(a) !=12:
#       raise invalidnumber("enter vailid aadhar no with 12 digit")
#     else:
#       print("Aadhar accepted")
# except invalidnumber as ad
# print(ad)



#FILE HANDILING
# x=open("abc.txt","r")
# y=x.read()
# print(y)

# x=open("xyz.txt","w")
# x.write("This is new content\n")
# x.write("welcome to new code")
# x.close()

# x=open("xyz.txt","a")
# x.write("New line added\n")

# # remove=3
# file =open ("abc.txt","r")
# file.close()

#File Ko Read Krne Ke Liye
with open("abc.txt","r")as file:
  print(file.read())

#Add Krne Ke Liye:
# with open("abc.txt","a")as file:
#   file.write("we are from Siddhartnager\n")
#   file.write("our country is india.\n")
#   file.write("india is grate country.\n")
#   print("Data appended successfuly!")

#Remove Krne Ke Liye:
# with open("abc.txt","r")as file:
#    lines=file.readlines()
#    word="we are from Siddhartnager"
# with open("abc.txt","w")as file:
#      for line in lines:
#        if word not in line:
#          file.write(line)


# Index Number Delete:
# remove=4
# with open("abc.txt","r")as file:
#    lines=file.readlines()
# with open("abc.txt","w")as file:
#     for i, line in enumerate(lines):
#       if i!= remove:
#        file .write(line)