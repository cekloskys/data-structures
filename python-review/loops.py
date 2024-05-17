# Python supports the for and while 
# looping structures.  Loops are used to
# repeat a block of code.

# The for loop is used for sequential traversal. It is 
# used for iterating over an iterable like a String, Tuple, 
# List, or Dictionary. 

# String
iterable = "987654321"
for i in iterable:
    print(i, end=" ")
print('blastoff!')

# Tuple
iterable = (9,8,7,6,5,4,3,2,1)
for i in iterable:
    print(i, end=" ")
print('blastoff!')

# List
iterable = [9,8,7,6,5,4,3,2,1]
for i in iterable:
    print(i, end=" ")
print('blastoff!')

# Dictionary
iterable = dict({'nine': 9, 
                 'eight': 8, 
                 'seven': 7, 
                 'six': 6, 
                 'five': 5, 
                 'four': 4, 
                 'three': 3, 
                 'two': 2, 
                 'one': 1})
for i in iterable:
    print("%d" % (iterable[i]), end=" ")
print('blastoff!')

# The while loop must be provided a condition.
# As long as the condition is true, its code
# block will be executed.
i = 9
while (i > 0):
    print(i, sep=" ", end=" ")
    # There must be a line of code in the code
    # block that forces the condition to become
    # false, else the loop will repeat infinitely.
    i = i - 1
print("blastoff!")

# Write a while loop that prints out the 
# odd numbers between 1 and 10.
i = 1
while (i <= 10):
    print(i, sep=" ", end=" ")
    i = i + 2