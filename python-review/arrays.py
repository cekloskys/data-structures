import array as arr

# creating an array with integer type
a = arr.array('i', [1, 2, 3])
# print(a)

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()