# The Python dictionary is a collection of keys values.
# A dictionary can be created by placing a sequence of 
# elements within curly {} braces, separated by ‘comma’.
# Values in a dictionary can be of any data type and can be duplicated, 
# whereas keys can’t be repeated and must be immutable. 
# Dictionary keys are case sensitive, the same name but 
# different cases of key will be treated distinctly.

# This line of code is creating an empty dictionary.
nums = {}
print(nums)

# This line of code is creating a dictionary
# that has 5 key values.
nums = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five'}
print(nums)

# This line of code is creating the same dictionary
# using the dict function.
nums = dict({1:'one', 2:'two', 3:'three', 4:'four', 5:'five'})
print(nums)

# These lines of code are accessing an element value
# in the dictionary by using its key.
print(nums[1])
nums[4] = 'six'
print(nums)

# If an attempt is made to access an element  
# that does not exist in the dictionary a KeyError 
# will be thrown.  These lines of code illustrate such
# an error.
# print(nums[6])
# nums[6] = nums[0]

# The Python len function tells the number of elements in the dictionary.
print(len(nums))

# This line of code is creating a dictionary
# of mixed values.
mixed_values = {1:1, 2:'one', 3:2, 4:'two', 5:3, 6:'three'}
print(mixed_values)

# This line of code is creating a dictionary
# of mixed keys.
mixed_keys = {1:1, 'one':1, 2:2, 'two':2, 3:3, 'three':3}
print(mixed_keys)

# A very handy way to step through the keys in a 
# dictionary is by using a for loop.
for key in nums:
    print(key, end=" ")
print()

# A very handy way to step through the values in a 
# dictionary is by using a for loop.
for val in nums.values():
    print(val, end=" ")
print()

# A very handy way to step through the keys and values in a 
# dictionary is by using a for loop.
for key, val in nums.items():
    print(key, val, end=" ")
print()

# We may also use a while loop to step through the values
# in a dictionary.
i = 1
while (i <= len(nums)):
    print(nums[i], end=" ")
    i += 1
print()

# This line of code is creating a dictionary
# of 13 characters.
name = {1:'G', 2:'U', 3:'I', 4:'D', 5:'O', 6:'V', 7:'A', 8:'N', 9:'R', 10:'O', 11:'S', 12:'S', 13:'U', 14:'M'}
print(name)

# This line of code is creating a second character dictionary, 
# and assigning the previous character dictionary to it.
# Now name and fullName refer to the same dictionary.
fullname = name
print(fullname)

# This line of code is changing the value at
# key 8 of the list dictionary name.
name[8] = 'B'
# Because fullName refers to the same dictionary, its value is
# changed too.
print(name, ' - name')
print(fullname, ' - fullname')

# Python has a copy method that may be used to create a copy of a dictionary.
# Changes made to the original dictionary, don’t affect the 
# copy. Changes made to the copy, don’t affect the 
# original dictionary.
copyname = name.copy()
print(name, ' - name')
print(copyname, ' - copyname')

name[8] = 'V'
print(name, ' - name')
print(copyname, ' - copyname')

# Python has inbuilt functions that may be used to manipulate
# dictionaries.
  
# The get function gets the value for the specified key.
print(nums.get(1))
print(nums)
  
# The pop function removes the element with specified key.
nums.pop(4)
print(nums, " - pop function")
  
# The popitem function removes the last inserted key-value pair.
nums.popitem()
print(nums, " - popitem function")
  
# The update function updates the dictionary with specified key-value pairs.
nums.update({3: 'python'})
print(nums, " - update function")

# The clear function removes all the elements from the dictionary.
nums.clear()
print(nums, " - clear function")