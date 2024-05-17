# Open a terminal in VS Code.
# Change directories into cmsc-251-data-structures.
# Create a python-review folder in cmsc-251-data-structures.
# Open the python-review in VS Code.
# Make sure python-review is the current directory in the terminal.
# Place the directory under version control: git init
# Add basic-io.py file to directory.
# Write code.
# Add code to staging: git add .
# Commit first version of code locally: git commit -m "First version of python-review"
# Create GitHub repository named python-review.
# Push first version of code to GitHub.

# Use the Run Python File option when running the script
# so that input may be easily typed in the terminal.

# The print method prints its parameter to standard
# out and appends a line separator string to the end
# of its output.
print("Hello World")

# The print method may print its parameter to standard
# out without appending a line separator string to the end
# of its output using the end parameter.
# We can end a print statement with any character/string 
# using this parameter. 
print("Hello World", end=" ")
print("Hello World")

# The print method may be given Strings 
# as well as any of the primitive and  
# object types.
print(100)      # Integer
print(True)     # Boolean
print(100.75)   # Float

# We can pass one or more parameters when using the print() function.
# By default, they are separated by a space.
print(100, True, 100.75)

# The default space can be modified and can be made to any character, 
# integer or string using the sep parameter.
print(100, True, 100.75, sep="-")

# The sep and end parameters may be used together in one print
# statement.
print(100, True, 100.75, sep="-", end="!")

# The string % modulo operator can be used with print for string formatting.
print("\nHello %s %s. You are %d years old." % ("Susan", "Ceklosky", 54))
print("Hello %s %s. You are %.2f years old." % ("Susan", "Ceklosky", 54.5))

# Write the line of code that produces the following output:
# Hello Susan Ceklosky. You are 54 years and 6 months old.
# You must use the string % modulo operator to format the 
# first and last names, and years and months values.

# The input function can be used to get data from standard in.
# The returned object will always be a string.
first = input("Please enter your first name: ") 
last = input("Please enter your last name: ")
print(first, last)

age = input("Please enter your age: ")
print("Hello %s %s. You are %s years old." % (first, last, age))
# This will generate a runtime error.
# print("Hello %s %s. You are %.2f years old." % (first, last, age))
print(type(first), type(last), type(age))

# We must typecast the returned object if we want to work
# with it in a form other than string.
intage = int(input("Please enter your age: "))
print("Hello %s %s. You are %d years old." % (first, last, intage))
floatage = float(input("Please enter your age: "))
print("Hello %s %s. You are %.2f years old." % (first, last, floatage))

# The split function can be used to get multiple values from standard in.
# If a separator is not given to the function then a white space is used.
fname, lname = input("Enter your first and last names separated by a space: ").split()
print(fname, lname)

# A separator, like a comma, may be provided.
fname, lname, tn = input("Enter your first and last names and telephone number separated by a comma: ").split(",")
print("Hello %s %s. Your phone number is %s." % (first, last, tn))

# Write the line of code that prompts the user to input their
# first and last names and age separated by a space. You must use the split
# function to separate the input values and then you must store them in variables.
# Write the line of code that then outputs:
# Hello <first name> <last name>. Your age is <age>.
# You must use the string % operator to format the first and last names and age.
fname, lname, intage = input("Enter your first and last names and age separated by a space: ").split()
print("Hello %s %s. Your age is %d." % (first, last, int(intage)))

# We can take in many inputs at a time.
x = [int(x) for x in input("Enter multiple numbers separated by a space: ").split()]
print("Number are: ", x)

y = list(map(int, input("Enter multiple numbers separated by a space: ").split()))
print("Number are: ", y)