import math

class circle:
    """The Circle class stores general information about a circle.
    """    
    def __init__(self, radius: float):
        """Constructs a circle using the specified radius.

        :ivar __radius: radius of this circle
        :ivar __area: area of this circle
        :ivar __circumference: circumference of this circle

        Args:
            radius (float): specified radius

        Raises:
            ValueError: indicates specified radius isn't a float
            ValueError: indicates specified radius isn't positive
        """        
        try:
            if (not isinstance(radius, float)):
                raise ValueError("Radius must be a float!") 
            if (radius < 0.0):
                raise ValueError("Radius must be positive!")             
        except ValueError as e:
            exit(e)
        else:
            self.__radius = radius
            self.__area = math.pi * pow(self.__radius, 2)
            self.__circumference = 2 * math.pi * self.__radius

    def getRadius(self):
        """Returns the radius of the calling circle.

        Returns:
            float: radius of the calling circle
        """        
        return self.__radius
    
    def setRadius(self, radius: float):
        """Sets the radius of the calling circle to the specified radius and
        recomputes the area and circumference of the calling circle.

        Args:
            radius (float): specified radius

        Raises:
            ValueError: indicates specified radius isn't a float
            ValueError: indicates specified radius isn't positive
        """        
        try:
            if (not isinstance(radius, float)):
                raise ValueError("Radius must be a float!") 
            if (radius < 0.0):
                raise ValueError("Radius must be positive!")             
        except ValueError as e:
            exit(e)
        else:
            self.__radius = radius
            self.__area = math.pi * pow(self.__radius, 2)
            self.__circumference = 2 * math.pi * self.__radius

    def getArea(self):
        """Returns the area of the calling circle.

        Returns:
            float: the area of the calling circle
        """   
        return self.__area
    
    def getCircumference(self):
        """Returns the circumference of the calling circle.

        Returns:
            float: the circumference of the calling circle
        """
        return self.__circumference
    
    def __str__(self):
        """Returns string representation of the calling circle.

        Returns:
            str: string representation of the calling circle
        """
        return f"{self.__radius}, area={self.__area}, circumference={self.__circumference}"
    
    def __eq__(self, other):
        """Tests if the calling circle is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling circle is equal to the specified
            object, else False
        """
        if other is not None:
            if isinstance(other, circle):
                if other.__radius == self.__radius:
                    if other.__area == self.__area:
                        if other.__circumference == self.__circumference:
                            return True
        return False
    
    @staticmethod
    def sort(data, first: int):
        """Sorts a list from largest to smallest using the insertion sort
        algorithm bypassing the elements to the left of first.

        Args:
            data: list to sort
            first (int): list index at which the sort will begin
        """        
        # initialize loop counter variable i to 1
        i = 1

        # initialize loop counter variable j to 0
        j = 0
    
        # initialize next value to 0
        nextVal = 0

        # loop through list as many times as specified by the
        # length of the list and first
        # this loop represents the blue arrow
        while(i < len(data) - first):
            # store a copy of the number in index position first + i
            # in next value
            nextVal = data[first + i]

            # loop through the list starting at the same index as 
            # next value and iterate back toward first as long as
            # the element to the left of next value is less than
            # next value and we're not the whole way back to first
            j = first + i
            while (j > first and data[j - 1] < nextVal):
                # shift the element to the left of next value right
                # ward one position
                data[j] = data[j - 1]

                # insert next value into the element that was just 
                # shifted
                data[j - 1] = nextVal

                # decrement j by 1
                j = j - 1

            # increment i by 1
            i = i + 1

    @staticmethod
    def search (a, first: int, size: int, target):  
        """Searches for a target value in a list of elements
        starting at a[first] using the serial search algorithm.

        Args:
            a: list to sort
            first (int): list index at which the search will begin
            size (int): the number of elements to search
            target (_type_): the value to search for

        Returns:
            int: If target appears in the list, count of the number
            of times it appears; else -1.
        """        
        # set an int variable i to 0
        i = 0

        # set a boolean variable found to false
        found = False

        # set an int variable count to 0
        count = 0

        # while there are more elements to search
        # and i plus first doesn't exceed the length of
        # the list
        while ((i < size) and (i + first < len(a))):
            # if the current element is the target
            if (a[i + first] == target):
                # set found to true
                found = True
                # increment count by 1
                count += 1
                # increment i by 1
                i += 1
            else:
                # increment i by 1
                i += 1

        # check if the target was found
        if (found):
            # return count
            return count
        else:
            # return negative 1
            return -1