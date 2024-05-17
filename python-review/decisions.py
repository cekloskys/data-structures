# Press “Ctrl + Shift + P” to open the Command Palette.
# Start typing “Python: Select Interpreter” and press Enter.
# Click on the Python Interpreter you want to use.

# Expressions in Python evaluate to true
# or false.  Expressions use the 
# comparison operators: <, >, <=, >=, 
# ==, !=.

# Declare a primitive int variable named x and
# initialize it to 4.
x = 4

# The print function may be given an expression.
print(x < 5)
print(x > 5)
print(x == 5)
print(x != 5)

# Write the lines of code that give the print
# function expressions.  The first line of code should
# output false.  The second line of code should output
# true.  Both expressions should use the variable x
# that was declared and initialized above.

# Python supports the if, if-else, if-elif-else, and  
# nested if decision structures.
        
# The if decision structure tests its condition
# and if the condition is true, it executes the
# code block it's given.
if (x < 5):
    print('x is less than 5 is true.')

# Here is the shorthand version of the if decision.
# It may be used when there is only one statement
# to be executed when the condition is true.
if (x < 5): print('x is less than 5 is true.')

# Write an if decision structure that tests if x is equal 
# to 4 and produces the output 'x is equal to 4 is true.' 
# if its condition is true.
if (x == 4):
    print('x is equal to 4 is true.')

# The if-else decision structure tests its condition
# and if the condition is true, it executes the
# code block it's given.  If the condition is false, 
# the code block given to the else is executed.
if (x == 5):
    print('x is equal to 5 is true.')
else:
    print('x is equal to 5 is false.')

# Here is the shorthand version of the if-else decision.
# It may be used when there is only one statement
# to be executed.
print('x is equal to 5 is true.') if (x == 5) else print('x is equal to 5 is false.')

# Write an if-else decision structure that tests if x is greater   
# than 4 and produces the output 'x is greater than 4 is true.' 
# if its condition is true.  If its condition is false, it produces
# the output 'x is greater than 4 is false.'.
if (x > 4):
    print('x is greater than 4 is true.')
else:
    print('x is greater than 4 is false.')

# The if-elif-else  decision structure tests multiple
# conditions.  The code block given to the condition
# that's true is executed.  If none of the conditions
# are true, the code block given to the else is 
# executed.
if (x > 5):
    print('x is greater than 5 is true.')
elif (x == 5):
    print('x is equal to 5 is true.')
else:
    print('None of the conditions are true.')

# Write the lines of code that include a third condition, x < 5,
# to the if-elif-else decision structure above.  When this third
# condition is true, the decision structure should produce
# the output 'x is less than 5 is true.'
if (x > 5):
    print('x is greater than 5 is true.')
elif (x == 5):
    print('x is equal to 5 is true.')
elif (x < 5):
    print('x is less than 5 is true.')
else:
    print('None of the conditions are true.')

# If more than one true condition is provided, the code
# block associated with the first one will be executed.
if (x > 5):
    print('x is greater than 5 is true.')
elif (x == 5):
    print('x is equal to 5 is true.')
elif (x < 5):
    print('x is less than 5 is true.')
elif (x != 5):
    # This code block won't be executed even though its
    # condition is true.
    print('x is not equal to 5 is true.')
else:
    print('None of the conditions are true.')

# A nested if is an if statement that is the target of another if statement. 
# Nested if statements mean an if statement inside another if statement.
if (x < 5):
    print('x is less than 5 is true.')
    if (x != 5):
        print('x is not equal to 5 is true.')

# Write the lines of code that nest an if-else condition
# in the if (x < 5) condition above instead of an if condition. 
# The condition given to the if should be (x != 4). When this
# condition is true, 'x is not equal to 4 is true.' should be
# output, else 'x is not equal to 4 is false.' should be output.
if (x < 5):
    print('x is less than 5 is true.')
    if (x != 4):
        print('x is not equal to 4 is true.')
    else:
        print('x is not equal to 4 is false.')

# In Python, comparison operators may be chained together.
a = 5
b = 10
c = 15

if a < b < c:
	print('b is greater than a and less than c')
        
# Python supports the match-case decision structure.  This 
# decision structure is useful when many conditions
# need to be tested. It requires Python 3.10 or newer.
grade = 'A'

match grade:
    case 'A':
        print('Super work!!')
    case 'B':
        print('Good job!')
    case 'C':
        print('You made it.')
    case 'D', 'F':
        print('Oh, dear ...')
    case _:
        print('Invalid grade.')

# Python supports the ternary operator. It resembles the
# shorthand if-else statement. 
result = 'x is equal to 5 is true.' if (x == 5) else 'x is equal to 5 is false.'
print(result)
print(('x is equal to 5 is true.' if (x == 5) else 'x is equal to 5 is false.'))

# It may be written using tuples.
# (false value, true value)[expression to test]
# if [x == 5] is true it returns 1, so the value at index 1 will be returned
# else if [x == 5] is false it returns 0, so the value at index 0 will be returned
result = ('x is equal to 5 is false.', 'x is equal to 5 is true.')[x == 5]
print(result)

# It may be written using dictionaries.
# if [x == 5] is true then the value of the True key will be returned
# else if [x == 5] is false then the value of the False key will be returned
result = {True: 'x is equal to 5 is true.', False: 'x is equal to 5 is false.'}[x == 5]
print(result)

# Expressions in Python evaluate to true
# or false.  Expressions may also use the Python
# logical operators: and, or, not.

# Declare a primitive int variable named num and
# initialize it to 50.
num = 50

# Write an if decision structure that tests if num is between
# 1 and 100 and produces the output 'num is between 1 and 100 is true.'
# if it's condition is true, else it produces 'num is between 1 and 100 is false.'.
if (num >= 1 and num <= 100):
    print('num is between 1 and 100 is true.')
else:
    print('num is between 1 and 100 is false.')

        
# Write an if decision structure that tests if num is not between 
# 1 and 100 and produces the output 'num is not between 1 and 100 is true.'
# if it's condition is true, else it produces 'num is not between 1 and 100 is false.'.
if (num < 1 or num > 100):
    print('num is not between 1 and 100 is true.')
else:
    print('num is not between 1 and 100 is false.')
        
# Declare a primitive boolean variable named foundIt and
# initialize it to false.
foundIt = False
        
# Write an if decision structure that tests if foundIt is false
# and produces the output 'foundIt is false.', else it produces
# 'foundIt is true.'.
if (not foundIt):
    print('foundIt is false.')
else:
    print('foundIt is true.')