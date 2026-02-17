# task-1 creating a dictionary
# student={"name":"adit","age":20,"grade":"A"}
# print(student)

# # task 2: accessing dictionary values
# student={"name":"adit","age":20,"grade":"A"}
# print("name:",student["name"],"grade:",student["grade"])

# # task 3: adding a new key-value pair
# student={"name":"adit","age":20}
# student["course"]="python"
# print(student)

# # task 4: removing a key-value pair
# student={"name":"adit","age":20,"grade":"A"}
# student.pop("age")
# print(student)

# # task 5: checking key membership
# student={"name":"adit","age":20,"grade":"A"}
# print("grade" in student)
# print(student)



# students = ["soni","priya","khushi","rewati","shipra","komal","shruti","ankita","nisha","tannu"]
# # trade = ("AIPA")
# # subjects = {"math","english","hindi","physics","chemistry"}
# marks = {
#     "soni":{87,67,59,78,68},
#     "priya":{78,89,56,77,66},
#     "khushi":{76,74,65,66,56},
#     "rewati":{89,68,67,72,56},
#     "komal":{90,75,80,69,59}
# }
# # print(students)
# # print(trade)
# # print(subjects)
# # print(marks)

# # #DATA CHECK
# # print("priya" in students)

# # #ADDING USING APPEND
# students.append("supriya")
# print(students)
# marks ["supriya"]=[90,78,60,55,45]
# print(marks)





# # KAHI BHI USE KRNE KE LIYE
# students.insert(3,"shiksha")
# print(students)
# students.remove("shruti")
# print(students)



# 
#     



# NASTED USE
# marks = {
#     "soni":{"math":87,"english":67,"hindi":59,"physics":78,"chemistry":68},
#     "priya":{"math":78,"english":89,"hindi":56,"physics":77,"chemistry":66},
#     "khushi":{"math":76,"english":74,"hindi":65,"physics":66,"chemistry":57},
#     "rewati":{"math":89,"english":68,"hindi":72,"physics":67,"chemistry":56},
#     "komal":{"math":90,"english":75,"hindi":80,"physics":69,"chemistry":59},
# }
# print(marks["khushi"]["english"])



books_name = ["My journey", "The problem of the rupee", "A devloped economy"]
country = ("India")
author = {"APJ Abdul kalam","Dr.B.R. Ambedkar's", "Atal bihari vajpayee"}
# # # year = {
# # #     "My journey":{"APJ Abdul kalam":2013},
# # #     "The problem of the rupee":{"Dr.B.R. Ambedkar":1990},
# # #     "A devloped economy":{"Atal bihari vajpayee":2000}
# # #  }
# # # print(year,author,country)

x={
      "my journey":{"author":"APJ abdul kalam","year":2013,"country":"india"},
      "The problem of the rupee":{"author":"dr bheem rao ambedkar","year":1990,"country":"india"},
      "A devloped economy":{"author":"Atal bihari bajpayee","year":2000,"country":"india"},
}
print(x["my journey"]["country"])




#SCOOP IN PYTHON:

# #Local variable and globle variable
# collage = "NSTIW"
# def globles():
#     collage = "Allahabad"
#     print(collage)
# globles()
# print(collage)

# # def local():
# #     collage="Allahabad"
# #     print(collage)
# # local()

# def local():
#     student_name ="priya tiwari"
#     print(student_name)
# local()

# course = "python"
# def show_course():
#     print("enrolled in",course)
# show_course()
# print(course)

# institute = "NSTI Allahabad"
# def welcome():
#     print("welcome",institute)
# def  info():
#     print("institute",institute)
# welcome()
# info()
# count=0
# def increase():
#     global count
#     count += 1
#     print(count)
# increase()
# increase()



# def function1():      
#     x = "shivali"
#     print(x)
# def function2():
#         y = "singh"
#         print(y)
# function1()
# function2()
#  
#FACTORIAL:
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# num=int(input("Enter number:"))
# print("fectorial of",num,"is:",factorial(num))


    



# name = "shivali"
# def gk():
#     global name
#     name = "soni"
#     print(name)
# gk()
# print(name)

































    








 

