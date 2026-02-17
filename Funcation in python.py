def add(x,y):
    return x+y
print(add(26,45))

# def sub(x,y):
#     return x-y
# print(sub(56,34))

# def multi(x,y):
#     return x*y
# print(multi(7,8))

# def div(x,y):
#     return x/y
# print(div(9,3))

# def square(x,y):
#     return x**3
# print(square(9)) 


# def div(x,y):
#     if y != 0:
#         return x/y
#     else:
#         return "0"
# print(div(10,0))

# import SS
# print(SS.cube(3))


#ARGUMENTS (args):
# def list (*args):
#     print("list of students:")
#     for i in args:
#       print(i)
# list("AIPA","CSA","EM","COPA")

# def add(*args):
#    print("Added number are:")
#    sum=0
#    for i in args:
#       sum +=i
#    return sum
# print(add(1,2,3,4,5,6,7))

# def marks(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# num = input("Enter your number:")
# added_list=[int(x) for x in num.split()]
# print(marks(*added_list)

# x = {"name": "shivali", "age":19, "phone":6306259681, "address":"lucknow"}
# print(x)   

# def xyz(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# xyz(name="shivali", trade="AIPA",Phone=6786853489,age=19)

# def send_mail(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# send_mail(name="priya", trade = "AIPA",application="give me leave for five days",date= '03/11/25')



# def largest_num(*args):
#     print("The largest number:", max(args))
# largest_num(5,8,10,4,9)

# def average(*args):
#     print("Average:", sum(args)/len(args))
# nums = input("Enter the numbers:").split()
# nums = [float(n)for n in nums]
# average(*nums)

# def mix (nsti, opening=1992,*trade,**details):
#     print(nsti)
#     print(opening)
#     print(trade)
#     if trade:
#         print("trades in nsti:", trade)
#     if details:
#       for key,values in details.items():
#          print(key,":",values)
# mix("Allahabad",2005,"AIPA","CSA",phone = 7848959484,pin = 212002,email = "nstiwallahabad@gmail.com")

# def student_report(name,*subjects,**marks):
#    print(name)
# #    print(subjects)
# #    print(marks)
#    for key,values in marks.items():
#       print(key,":",values)
# student_report("shivali","hindi","english","math",hindi = 89,english=78,math =90)

# def travel_booking(destination,days=1,*activities,**details):
#    print(destination)
#    print(days)
#    print(activities)
#    for key,values in details.items():
#       print(key,":",values)
# travel_booking("manali",6,"walking on the mountain",hotel="renest river country",price =5000,transport = "flight")
   
# def add(a,b):
#    return a+b
# def hello():
#    print("welecom nsti")




    
