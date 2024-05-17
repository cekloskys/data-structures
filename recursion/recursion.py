class recursion:
    @staticmethod
    def factorial(n: int):
        # this is the stopping case
        if (n == 1):
            return n
        else:
            # this is the recursive call
            return n * recursion.factorial(n - 1)
        
    @staticmethod
    def power (number: int, power: int):
        # this is the stopping case
        if (power == 0):
            return 1
        else:
            # this is the recursive call
            return number * recursion.power(number, power - 1)
        
    @staticmethod
    def computeMin(nums, i: int, min: int):
        # this is the stopping case
        if (i == len(nums)):
            return min
        else:
            if (nums[i] <= min):
                min = nums[i]
            i = i + 1
            # this is the recursive call
            return recursion.computeMin(nums, i, min)
        
    @staticmethod
    def reverse(s: str, i: int):
        # this is the stopping case
        if (i == 0):
            print(" is the reverse of %s using recursion." % (s))
        else:
            print(s[i - 1], end="")
            i = i - 1
            # this is the recursive call
            recursion.reverse(s, i)

    @staticmethod
    def sing(num: int):
        # this is the stopping case
        if (num == 0):
            print("There are no more bottles of beer on the wall!")
        else:
            print("%d bottles of beer on the wall. %d bottles of beer." % (num, num))
            print("Take one down, pass it around, %d bottles of beer on the wall." % (num - 1))
            # this is the recursive call
            recursion.sing(num - 1)