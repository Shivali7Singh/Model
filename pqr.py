# Check the value of factorial from a user-defined list
import math 
def check_factorial(list):
     for num in list:
        fact = math.factorial(num)
     print(f"The factorial if of{num} is {fact}")
numbers = [1,2,3,4,5,6]
check_factorial(numbers)
# #
number = int(input("enter the factorial number:"))
factorial = 1
for i in range(1,number+1):
    factorial = factorial*i
print("factorial of", number, "is",factorial)

Remove duplicate elements from a list without using set()
list = [1,2,3,3,4,5,5,6]
new_list = []

for x in list:
    if x not in new_list:
        new_list.append(x)
print(new_list)

#Find second largest number without sorting
num =[20,6,7,25,8,3]
largest = second = float("-inf")
for y in num:
   if y> largest:
      second = largest
      largest = y
   elif y > second and y != largest:
      second = y
print(second)

# Count many times each element appears and return a dictionary
def merge_lists(A, B):
   return sorted(A + B)
A = [1,2,3]
B = [2,4,6]
print(merge_lists(A, B))

# Return a new list of elements without duplicate
def commen_elements(A, B):
   return list(set(A) & set(B))

A = [1,2,3,3,4,5,6,6]
B = [3,4,6]
print(commen_elements(A, B))

#Replaced each elements with its square
def square_list(list):
   return [num ** 2 for num in list]

numbers = [1,2,3,4,5,6]
print(square_list(numbers))

#Seprate even and odd numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 != 0]

print("Even numbers:", evens)
print("Odd numbers:", odds)

#Rotate list to right by N steps
def rotate_list(list, N):
    N = N % len(list)
    return list[-N:] + list[:-N]
numbers = [1,2,3,4,5,6,7,8]
N = 2
# print(rotate_list(numbers, N))
#Find the elements that appear in all three
def common_elements(A, B, C):
    return list(set(A) & set(B) & set(C))
A = [1,2,3,4]
B = [2,3,5]
C = [3,2,6]
print(common_elements(A,B,C))