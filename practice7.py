# Single-quoted strings
 single_quoted = 'Hello, world!'

# String oprations with single-quoted strings
length = len(single_quoted)       # Length of the string
upper_case = single_quoted.upper()           # Convert to uppercase
lower_case = single_quoted.lower()         # Convert to lowercase
contains_substring = 'World' in single_quoted                 # Check if substring is present

# Printing results
print("single-quoted string:", single_quoted)  
print("length of the string:", length)
print("uppercase version:", upper_case)
print("lowercase version:", lower_case)
print("contains 'World':", contains_substring)

# Double-quoted string
double_quoted = "Akriti is awesome!"

# String operations
length = len(double_quoted)                       # length of the string
replaced_string = double_quoted.replace("awesome", "great")            # replace word
words = double_quoted.split()                    # split into words

# Printing results
print("double-quoted string:", double_quoted)
print("length of the string:", length)
print("string after replacement:", replaced_string)
print("words in the string:", words)
