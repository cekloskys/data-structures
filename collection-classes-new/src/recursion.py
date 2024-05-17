class recursion:
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

    @staticmethod
    def evens (start: int, end: int):
        # this is the stoppping case
        if (start > end):
            print()
        else:
            if (start % 2 == 0):
                print(start, end=" ")
            # this is the recursive call
            recursion.evens(start + 1, end)