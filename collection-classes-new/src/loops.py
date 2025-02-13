class loops:
    @staticmethod
    def sing(num: int):
        """Displays the lyrics for Bottles of Beer on the Wall
        for as many rounds as specified by num.

        Args:
            num (int): number that specifies how many rounds of 
            Bottles of Beer on the Wall will be displayed
        """        
        i = num
        while(i > 0):
            print("%d bottles of beer on the wall. %d bottles of beer." % (i, i))
            print("Take one down, pass it around, %d bottles of beer on the wall." % (i - 1))
            i = i - 1
        print("There are no more bottles of beer on the wall!")

    @staticmethod
    def evens (start: int, end: int):
        """Finds and displays the even numbers between a specified 
        starting and ending value.

        Args:
            start (int): specified starting value
            end (int): specified ending value
        """        
        i = start
        while (i <= end):
            if (i % 2 == 0):
                print(i, end=" ")
            i += 1
