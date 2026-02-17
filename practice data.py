# Question 1: Create a list
# cities = ["delhi", "mumbai", "lucknow", "patna", "gorakhpur"]
# print(cities)
# Question 2: 
# fruits = ["mango", "apple", "orange", "banana"]
# print("first element:", fruits[0])
# print("last element:", fruits[-1])
# Quistion 3:
# numbers = [10, 20, 30, 40, 50, 60]
# print(numbers[1:4])
# Question 4:




#   Tuple practice:
# x = ("shruti", "saumya", "khushi", "nisha", "ankita")
# # print("nisha" in x)
# print(len(x))
# a = [2, 4, 5, 6]
# # # print(max(a))
# # # print(min(a))
# # # print(sum(a))

# b = a.pop(2)
# print(b)
# print(a)

# Create a tuple
# fruits = ("mango","banana","papaya", "chiku", "apple", "orange")
# print(fruits)

# number =(10,20,30,40,50,60)
# print("first element:",number[0])
# print("last element:", number[-1])

# SLICING 
# colours = ("red", "pink", "green", "black", "blue", "white")
# print("middel three colours:")
# print( colours[2:5])

# CONCATENATEING
# x = (1,2,3)
# y = (4,5,6)
# z = x+y
# print(z)

#ITERATING 
# animal = ("cat","dog", "rabbit", "elephant")
# print(animal)

# MEMBERSHIP TEST IN A TUPLE
#fruits names upper likha hai
# print("papaya" in fruits)
# print("papaya is present")
# print("grapes" in fruits)
# print("grapes not found")

# NESTED TUPELS 
# student = ("rahul", (85, 90, 92))
# print("rahul second marks:", student)

# APPLUING BUILT IN FUNCATIONS
# num=(5,10,15,20,25)
# print(len(num)) 

#UPDATING A TUPLE
#fruits name upar likha hai

# fruit=list(fruits)
# fruit.append("banana"with"orange")
# print(fruit)


#DELETING TUPAL
# cities =("delhi","mumbai","kolkata","chennai")
# del cities
# print("tuple is successecful")
 
#SET USE
# x = {1,2,3,4,5}
# # x.add("shivali")
# x.update(["soni","priya",8,9,"shipra"])
# print(x)

# a = {"cat","dog","elephant","tiger","lion"}
# b = {"cow","monkey","dog","tiger"}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))

# print(a.issubet(b))

# DICTICONARY
#variable = {"key": "value"}

# students = {"name":"shivali","age":19,"trade":"aipa"}
# print(students["age"])
# print(students["name"])

# students["marks"]=89
# students["address"]= "lucknow"
# print(students)

# #REMOVING FROM DICTIONARY
# students.pop("age")
# print(students)
 

# print("age" in students)
# print("name" in students)
# print("phone" in students)


# #ITERATE OVER DICTIONARY
# for key, value in students.items():
#  if key == "trade":
#   continue
#  print(key,":",value)

# # #  #MERGING DICTIONARY
#  x = {"name":"soni","age":"20"}
#  y = {"trade":"csa","address":"delhi"}
#  x.update(y)
#  print(x)


 #NASTED DICTIONARY
# students={
#   "AIPA":{"name":"shivali","age":20,"trade":"AIPA","address":"delhi"},
#   "COPA":{"name":"soni","age":22,"trade":"COPA","address":"naini"},
#   "EM":{"name":"priya","age":20,"trade":"EM","address":"teliyarganj"}
#  }

 
# print(students)
# print(students["EM"]["address"])

# #COPY DICTIONARY
# students2=students.copy()

# print(students2)

# # CLEAR DICTIONARY

# students.clear()
# print(students)