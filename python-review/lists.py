# The list is one of Python's main ordered 
# collections.

# This line of code is creating an empty list.
nums = []
print(nums)

# This line of code is creating a list
# of 5 integers.
nums = [1,2,3,4,5]
print(nums)

# These lines of code are accessing an element value
# in the list by using its index.
print(nums[1])
nums[4] = 6
print(nums)

# If an attempt is made to access an element outside 
# of the bounds of the list an IndexError 
# will be thrown.  These lines of code illustrate such
# an error.
# print(nums[5])
# nums[-6] = 0
# We may use negative indices in the square brackets.
# In the case of this list, -5, -4, -3, -2, -1 are valid
# indices with -1 being the index for the last element
# and -5 being the index for the first element.
print(nums[-5])
print(nums[-1])

# The Python len function tells the number of elements in the list.
print(len(nums))

# This line of code is creating a list
# of values of mixed types.
mixed = [1, 'one', 2, 'two', 3, 'three']
print(mixed)

# A very handy way to step through the elements in an 
# list is by using a loop.
# For loop
for i in mixed:
    print(i, end=" ")
print()

# While loop
i = 0
while (i < len(nums)):
    print(nums[i], end=" ")
    i = i + 1
print()

# Rewrite the while loop so that it outputs only the numbers
# in nums that are less than 6.
i = 0
while (i < len(nums)):
    if (nums[i] < 6):
        print(nums[i], end=" ")
    i = i + 1
print()

# SKIP THIS - Rewrite the while loop so that it outputs the appropriate
# day representation of each number in num3; for example, 1 is Sunday,
# 2 is Monday, etc.
i = 0
while (i < len(nums)):
    match nums[i]:
        case 1:
            print('Sunday')
        case 2:
            print('Monday')
        case 3:
            print('Tuesday')
        case 4:
            print('Wednesday')
        case 5:
            print('Thursday')
        case 6:
            print('Friday')
        case 7:
            print('Saturday')
        case _:
            print('Invalid number.')
    i = i + 1
print()

# This line of code is creating a list
# of 14 strings.
name = ['G', 'U', 'I', 'D', 'O', 'V', 'A', 'N', 'R', 'O', 'S', 'S', 'U', 'M']
print(name)

# This line of code is creating a second character list, 
# and assigning the previous character list to it.
# Now name and fullName refer to the same list.
fullname = name
print(fullname)

# This line of code is changing the value in the element 
# at index position 8 of the list named name.
name[8] = 'B'
# Because fullName refers to the same list, its value is
# changed too.
print(name, ' - name')
print(fullname, ' - fullname')

# Python has a copy method that may be used to create a copy of a list.
# Changes made to the original list, don’t affect the 
# copy. Changes made to the copy, don’t affect the 
# original list.
copyname = name.copy()
print(name, ' - name')
print(copyname, ' - copyname')

name[8] = 'V'
print(name, ' - name')
print(copyname, ' - copyname')

# Python has inbuilt functions that may be used to add elements
# to a list.

# The append function may be used to add one element at a time to the list. 
# For the addition of multiple elements with the append function, loops are used. 
# Tuples can also be added to the list with the use of the append function. 
# Lists can also be added to an existing list with the use of the append function.

# This line of code creates an empty list.
names = []
print(names)

# These lines of code add elements one at a time to the list.
names.append('Sammy')
names.append('Mia')
names.append('Dean')
names.append('Copper')
print(names)

# These lines of code add multiple elements to the list using a loop.
for i in range(1,5):
    names.append(i)
print(names, ' - add multiple elements using a loop')

# This line of code adds a tuple to the list.
names.append(("Chessie", "Lexi"))
print(names, ' - add tuple')

# This line of code adds a list to the list.
names.append([1,2])
print(names, ' - add list')

# The insert function may be used to add elements at a desired position in a list.
names.insert(0, 'Pixie')
names.insert(5, 0)
print(names, ' - insert function')

# The extend function may be used to add multiple elements at the end of a list.
names.extend(['Lea', 'Fritz', 'Lea'])
print(names, ' - extend function')

# The reverse function may be used to reverse the elements in a list.
names.reverse()
print(names, ' - reverse function')

# The remove function may be used to remove a desired value from a list.
names.remove(('Chessie', 'Lexi'))
print(names, ' - remove function')

# An error will be generated if the value doesn’t exist in the list.
# names.remove([1,2,3])

# Only the first occurrence of the value will be removed from the list.
names.remove('Lea')
print(names, ' - remove function first occurrence')

# The remove function only removes one element at a time.
# To remove a range of elements, a loop must be used.
names.reverse()
print(names)
for i in range(0, 5):
    names.remove(i)
print(names, ' - remove function range')

# The pop function can also be used to remove and return an element from the list.
# By default, it removes only the last element of the list. 
# To remove an element from a specific position of the list, the index of the element 
# must be passed as an argument.

# This line of code pops the last element in the list.
last = names.pop()
print(last)
print(names, ' - pop function')

# This line of code pops the element at index position 0.
first = names.pop(0)
print(first)
print(names, ' - pop function with index')

# SKIP
# We can get sublists using a slice. Slice  is performed with the use of a colon(:). 
#  0        1      2       3         4       5
# ['Sammy', 'Mia', 'Dean', 'Copper', [1, 2], 'Lea']
#  -6       -5     -4      -3        -2      -1

# This line of code slices elements in the index range 1 - 4 (excluding 4).
slicedlist = names[1:4]
print(slicedlist)

# This line of code slices elements from 
# index position 3 to the end of the list.
slicedlist = names[3:]
print(slicedlist)

# This line of code slices elements from 
# the beginning of the list up to (but not including) index position 3.
slicedlist = names[:3]
print(slicedlist)

# This line of code slices elements from 
# the beginning of the list up to (but not including) index position 3.
slicedlist = names[:-3]
print(slicedlist)

# This line of code slices elements from 
# index position 3 to the end of the list.
slicedlist = names[-3:]
print(slicedlist)

# This line of code slices elements in the index range 1 - 4 (excluding 4).
slicedlist = names[-5:-2]
print(slicedlist)

# This line of code will slice the entire list.
slicedlist = names[:]
print(slicedlist)

# This line of code will slice the entire list in reverse.
slicedlist = names[::-1]
print(slicedlist)

# Python list comprehensions may be used for creating new lists from other lists.
# Syntax: newList = [ expression for element in old list if condition ]
x = [x for x in range(1, 11)]
print(x)
x_square = [x ** 2 for x in range(1, 11)]
print(x_square)
x_odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(x_odd_square)