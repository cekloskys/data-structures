class recursion:
    # Question 8
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