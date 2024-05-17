class loops:
    @staticmethod
    def factorial(n: int):
        """Computes the factorial of a specified number.

        Args:
            n (int): specified number

        Returns:
            int: computed factorial
        """
        # the counter variable in the loop for all
        # intents and purposes is one and the same as
        # the parameter n
        
        # the loop will repeat as long as i > 1
        # the condition that will cause the loop to stop
        # is i == 1 -> stopping case for the loop
        
        # with each iteration of the loop, we're
        # decrementing the counter variable by 1
        i = n - 1
        while (i > 1):
            n = n * i
            # n = 6 * 5
            # n = 30 * 4
            # n = 120 * 3
            # n = 360 * 2
            i = i - 1

        return n
    
    @staticmethod
    def power (number: int, power: int):
        """Takes a specified number to a specified power.

        Args:
            number (int): specified number
            power (int): specified power

        Returns:
            int: computed power
        """
        # the counter variable in the loop for all
        # intents and purposes is one and the same as
        # the parameter power
        
        # the loop will repeat as long as i > 0
        # the condition that will cause the loop to stop
        # is i == 0 -> stopping case for the loop
        
        # with each iteration of the loop, we're
        # decrementing the counter variable by 1
        result = 1
        i = power
        while (i > 0):
            result = result * number
            # result = 1 * 2 : i = 5
            # result = 2 * 2 : i = 4
            # result = 4 * 2 : i = 3
            # result = 8 * 2 : i = 2
            # result = 16 * 2 : i = 1
            i = i - 1

        return result
    
    @staticmethod
    def computeMin(nums):
        """Finds the minimum number in a specified list of numbers.

        Args:
            nums (int): specified list

        Returns:
            int: minimum number
        """
        # the counter variable in the loop is the
        # index used to iterate through the elements
        # in the list 
        
        # the loop will repeat as long as i < len(nums)
        # the condition that will cause the loop to stop
        # is i == len(nums) -> stopping case for the loop
        
        # with each iteration of the loop, we're
        # incrementing the counter variable by 1
        i = 0
        min = nums[i]
        while (i < len(nums)):
            if (nums[i] <= min):
                min = nums[i]
            i = i + 1
        return min
    
    @staticmethod
    def reverse(s: str):
        """Displays a specified String in reverse order.

        Args:
            s (str): specified String
        """
        # the counter variable in the loop is the
        # index used to iterate through the
        # characters in the String
        
        # the loop will repeat as long as i > 0 
        # the condition that will cause the loop to stop
        # is i == 0 -> stopping case for the loop
        
        # with each iteration of the loop, we're
        # decrementing the counter variable by 1
        i = len(s)
        while(i > 0):
            print(s[i - 1], end="")
            i = i - 1
        print(" is the reverse of %s using recursion." % (s))

    @staticmethod
    def sing(num: int):
        i = num
        while(i > 0):
            print("%d bottles of beer on the wall. %d bottles of beer." % (i, i))
            print("Take one down, pass it around, %d bottles of beer on the wall." % (i - 1))
            i = i - 1
        print("There are no more bottles of beer on the wall!")