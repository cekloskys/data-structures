from loops import *
from recursion import *

print("Factorial of 6 using a loop is :", loops.factorial(6))
print("Factorial of 5 using a loop is :", loops.factorial(5))

print("Factorial of 6 using recursion is :", recursion.factorial(6))
print("Factorial of 5 using recursion is :", recursion.factorial(5))

print("2 to the 5th power using a loop is :", loops.power(2, 5))
print("2 to the 5th power using recursion is :", recursion.power(2, 5))

nums = [5,12,3,4]
print("Minimum number using a loop is :", loops.computeMin(nums))
print("Minimum number using recursion is :", recursion.computeMin(nums, 0, nums[0]))

loops.reverse("CAT")
recursion.reverse("CAT", len("CAT"))

loops.sing(3)
recursion.sing(3)