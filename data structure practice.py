#Task 1: Creating a Tuple
# my_tuple = (10,20,30,40,50,60)
# print("Tuple:", my_tuple)

# #TASK 2: Accessing elements in a tuple
# print("First element:", my_tuple[0])
# print("Last element:", my_tuple[-1])

# #TASK 3:Slicing a Tuple
# print("slice[1:4]:", my_tuple[1:4])
# print("silce from beginning to index 3:", my_tuple[:3])
# print("slice from index 2 to end:", my_tuple[2:])

# #TASK4: Concatenating two tuples
# extra_tuple = (70,80,90)
# concatenated = my_tuple + extra_tuple
# print("concatenated tuple:", concatenated)

# #TASK 5: Iterating through a tuple
# for item in my_tuple:
#     print("Item:", item)

# #TASK 6: Membbership test in a tuple
# print("is 30 in tuple?", 30 in my_tuple)
# print("is 100 not in tuple?", 100 not in my_tuple)

# #TASK 7: Nested tuples and accessing their elements
# nested_tuples = (my_tuple, (70,80,90))
# print("Nested tuple:", nested_tuples)
# print("Accessing nested element (my_tuple [2]):", nested_tuples[0][2])
# print("Accessing nested element (90):", nested_tuples[1][2])

# #TASK 8: Applying built-in frncations on tuples
# print("Length of tuple:", len(my_tuple))
# print("Maximum value:", max(my_tuple))
# print("Minimum value:", min (my_tuple))
# print("Sum of elements:", sum(my_tuple))

# #TASK 9: Updating a tuple(using list conversion)
# tem_list = list(my_tuple)
# tem_list[2] = 99 # update 3rd element
# update_tuple = tuple(tem_list)
# print("Updating tuple:", update_tuple)

# #TASK 10: Deleting a Tuple
# del my_tuple
# # print(my_tuple) 



# #LAB 34 PRACTICE

# #TASK 1: Creating and Acciessing Strings
# my_string = "Heelo, shivali!"
# print("Original string:", my_string)
# print("First charxcter:", my_string[0])
# print("Last element:", my_string[-1])

# #TASK 2: String Conactenation and repetition
# str1 = "shivali"
# str2 = "singh"
# concat_str = str1 + " " + str2
# repeated_str = concat_str * 3
# print("Concatenated string:", concat_str)
# print("Repeated string:", repeated_str)

# #TASK 3: String case Manipolation
# upper_str = my_string.upper()
# lower_str = my_string.lower()
# title_str = my_string.title()
# swapcase_str = my_string.swapcase()
# print("Uppercase:", upper_str)
# print("Lowercase:", lower_str)
# print("Title case:", title_str)
# print("Swap case:", swapcase_str)


# #TASK 4: Serching in Strings
# substring = "Shivali"
# found_index = my_string.find(substring)
# if found_index != -1:
#     print(f"Substring '{substring}' found at index {found_index}")
# else:
#     print(f"Substring '{substring}' not found")

# #TASK 5: Replacing substrings
# new_string = my_string.replace("shivali", "World")
# print("String after replacement:", new_string)

# # #TASK 6: String Formatting
# # name = "soni"
# # age = 23
# formatted_str = f"My name is {name}" and I am {age} years old."
# print("Formatted string:", formatted_str)

# #TASK 7: Trimming and Padding String
#Original string with extra spaces
# text = "    extra spaces   "

# #Padding exmaple (manually adding* charaters)
# padded = "*** Hello, shivali!***"
# print("padded string:", padded)

# #Trimming example (removing leading and trailing spaces)
# trimmed = text.strip()
# print("Trimmed string:", trimmed)

# #TASK 8: SPLITTING AND JOINING STRINGS
# sentence = "Python is fun"
# words = sentence.split()
# joined_sentence = '-'.join(words)
# print("Splitted words:", words)
# print("Joined sentence:", joined_sentence)

# #TASK 9: Counting Characters
# char_count = my_string.count("o")
# print(f"Character 'o' appears {char_count} times in the string")

# #TASK 10: Checking String Properties
# is_alpha = "Hello".isalpha()
# is_digit = "12345".isdigit()
# is_alnum = "Hello123".isalnum()
# is_space = "  ".isspace()
# print("Is 'Hello' alphabetic?", is_alpha)
# print("Is '12345' numeric?", is_digit)
# print("Is 'Hello123' alphanumeric?", is_alnum)
# print("Is '   ' all spaces?", is_space)


# #LAB 35
#TASK 1: Creating Sets
# set_a = {1,2,3,4,5}
# set_b = {4,5,6,7,8}
# print("set A:", set_a)
# print("set B:",set_b)

# #TASK 2: Adding and Removing elements in a set
# set_a.add(6)
# set_a.remove(1)
# print("Set A after adding 6 and removing 1:", set_a)
# print("set A:", set_a)
# print("set B:",set_b)
 
#  #TASK 3: Union of Sets
# union_set = set_a.union(set_b)
# print("Union of Set A and B:", union_set)


# #TASK 4: Intersection of Sets
# intersection_set = set_a.intersection(set_b)
# print("Intersection of Set A and Set B:", intersection_set)

# #TASK 5: Difference of Sets
# difference_set = set_a.difference(set_b)
# print("Difference of Set A and Set B (A - B):", difference_set)

# #TASK 6: Symmetric Difference of Sets
# sym_diff_set = set_a.symmetric_difference(set_b)
# print("Symmetric Difference of set A and Set B:", sym_diff_set)

# #TASK 8: Set Membership Testing
# is_member = 3 in set_a
# print("Is 3 in Set A?", is_member)

# #TASK 9: Removing Duplicates Using Sets
# numbers_list = [1,2,3,4,4,5,6,6,7]
# unique_numbers = set (numbers_list) #Removing dupicates
# print("List of numbers after removing duplicates:", unique_numbers)

# #TASK 10: Set Comprehension
# squares_set = {x ** 2 for x in range(1,11)}
# print("Set of squares of numbers from 1 to 10:", squares_set)

# #TASK 11: Clearing a Set
# set_a.clear()
# print("Set A after clearing:", set_a)


#LAB 36:
#TASK 1: Creating a Dictionary
student_grades = {
    "Maria": 85,
    "Soumya": 78,
    "Ramar": 62
}
print("Student Grades:", student_grades)

#TASK 2:Accessing Dictionary Values
alice_grade = student_grades["Maria"]
print("Maria's Grade:", alice_grade)

#TASK 3: Adding a New Key-Value Pair
student_grades["Rashmi"] = 88
print("Updated Student Grades:", student_grades)

#TASK 4: Removing a Key-Value Pair
student_grades.pop("Soumya")
print("Student Grades after removing Soumya:", student_grades)

#TASK 5: Checking Key Membership
is_rashmi_in_dict = "Rashmi" in student_grades
print("Is Rashmi in the dictionary?", is_rashmi_in_dict)

#TASK 6: Iterating Over a Dictionary (Key and Values)
print("Iterating over  student names and grades:")
for student, grade in student_grades.items():
    print(f"{student}: {grade}")

#TASK 7: Using the get()Method
ramar_grade = student_grades.get("Ramar", "Not found")
print("Ramar's Grade:",ramar_grade)

#TASK 8: Merging Dictionaries
additional_grades = {"Bhawani": 60, "Usha": 75}
student_grades.update(additional_grades)
print("Student Grades after merging with additional data:",student_grades)

#TASK 9:Dictionary Comprehension
squared_numbers = {x: x ** 2 for x in range(1,6)}
print("Dictionary of numbers and their squares:", squared_numbers)

#TASK 10: Handling Neted Dictionaries
nested_dict = {
    "USA":{"New York": 8000000, "Los Angeles": 4000000},
    "India":{"Mumbai": 20000000, "Delhi": 15000000}
}
print("Nested dictionary of countries and cities:", nested_dict)

#TASK 11: Accessing Nested Values
ny_population = nested_dict["USA"]["New York"]
print("Population of New York:", ny_population)








