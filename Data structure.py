# abc =["shivali", "soni", "priya", 7, "shejal"]
# print(abc[2])
# print(abc[-2])
# print(abc[2:4])

# xyz =[1, 4, 8, "shipra", "akriti", "rewati", "komal", "khushi", "shruti","ankita"]
# # print(xyz[3])
# print(xyz[-4])
# print(xyz[3:6])

# xyz.append("AIPA")    #Append
# print(xyz)

# xyz.insert(2,"NSTI")   #Insert
# print(xyz)

# xyz.remove("rewati")    #Remove
# print(xyz)
# LAB 32:
#Task 1: implementation of creating a list
#1. Creating a list
fruits = ["apple", "banana", "cherry", "mango", "orange"]
# # print("original list:", fruits)

# Task 2: Implementation of accessing elements in a list
# first_fruit = fruits[0]
# last_fruit = fruits[-1]
# print("first fruits:", first_fruit)
# print("last_fruits:", last_fruit)

# Task 3. Slicing a list
# sublist_fruits = fruits[:3]
# print("sublist of first three fruits:", sublist_fruits)

#Task 4. Adding elements to a list
# fruits.append("grape")
# print("list after adding 'grape':", fruits)

# Task 5. Inserting elements into a list
# fruits.insert(1, "pineapple")
# print("list after inserting 'pineapple' at position 1:", fruits)

# Task 6. Removing elements from a list
# fruits.remove("banana")
# print("list after removing 'banana':", fruits)

#Task 7. Popping elements from a list
# popped_fruit = fruits.pop()
# print("popped fruit:", popped_fruit)
# print("list after popping the last element:", fruits)

#Task 8. Finding the length of a list
# length = len(fruits)
# print("number of fruits in the list:", length)

# Task 9. Checking membership in a list
# is_in_list = "apple" in fruits
# print("is 'apple' in the list?", is_in_list)

# Task 10. Iterating over a list
# print("interating over the list:")
# for fruit in fruits:
#     print(fruit)

#Task 11. Sorting a list
# fruits.sort()
# print("list after sorting alphabetically:", fruits)

# Task 12. Reversing a list
# fruits.reverse()
# print("list after reversing the order:", fruits)

# Task 13. List comprehensions
# long_fruits = [fruit for fruit in fruits if len(fruit) > 5]
# print("fruits with more then 5 letters:", long_fruits)

# Task 14. Copying a list
fruits_copy = fruits.copy()
# print("copied list:", fruits_copy)

# Task 15. Clearing a list
# fruits.clear()
# print("list after clearing all elements:", fruits)


#Task 16: Extending a list with another list
# vegetables = ["caroot", "brocoli", "spinach"]
# fruits_copy.extend(vegetables)
# print("list after extending with vegetables:", fruits_copy)

#Task 17: Counting occurrences of an element in a list
# num_apples = fruits_copy.count("apple")
# print("Number of'apple' in the list:", num_apples)

#Task 18: Finding the index of an element
# if "carrot" in fruits_copy:
# caroot_index = fruits_copy.index("carrot")
# print("Index of 'carrot':", carrot_index)

#Task 19: Removing an element by index
# if len(fruits_copy)> 2:
#     del fruits_copy[2]
#     print("List after removing element at index 2:", fruits_copy)

#Task 20: Nested lists
# nested_list = [fruits_copy, vegetables]
# print("Nested list:", nested_list)

# USE FOR TUPLE:

# TUPLE 
# a = ("shivali", "soni", "priya", "shejal", "akriti")
# b = list(a)
# b.append("shipra")
# print(b)

# x = (1, "AIPA", 2, "CSA", 3, "EM")
# y = (4, "COSMO", 5, "DM", 6, "FDT")
# z = x+y
# print(z)

# Control flow 
# colours = ("red", "black", "white", "pink", "green")
# for s in colours:
# #    if s == "black":
# #      continue
#    if s == "pink":
#       break
#    print(s)

# trade = ("aipa", "copa", "cosmo", "csa", "dm", "em") 
# for i in trade:
#     if i == "em":
#         continue
#     print(i)
# print("em trade skipped")
# #   if i == "csa":
#      break
#   print(i)
# OR
# print(trade[:4])
# print("end of condication") 



