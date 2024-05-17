from times.time import *

class datetime(time):
    """The datetime class stores general information about a datetime.
    """ 
    def __init__(self, hour: int, minute: int, second: int, year: int, month: int, day: int):
        """Constructs a datetime object having the specified hour, minute, and second, year,
        month, day and universal datetime in the format YYYY-mm-dd HH:MM:SS.

        :ivar __hour: hour of this datetime object
        :ivar __minute: minute of this datetime object
        :ivar __second: second of this datetime object
        :ivar __year: hour of this datetime object
        :ivar __month: minute of this datetime object
        :ivar __day: second of this datetime object
        :ivar __datetime: universal datetime of this time object in the format YYYY-mm-dd HH:MM:SS

        Args:
            hour (int): specified hour
            minute (int): specified minute
            second (int): specified second
            year (int): specified year
            month (int): specified month
            day (int): specified day

        Raises:
            ValueError: indicates specified month is less than 0 or greater than 12
            ValueError: indicates specified day is less than 0 or greater than 31
        """
        super().__init__(hour, minute, second)
        try:
            if (month <= 0 or month > 12):
                raise ValueError("Invalid month!") 
            if (day <= 0 or day > 31):
                raise ValueError("Invalid day!")           
        except ValueError as e:
            exit(e)
        else:
            self.__year = year
            self.__month = month
            self.__day = day
            self.__datetime = f"{self.__year}-{self.__month:02d}-{self.__day:02d} {self.getTime()}"

    def getYear(self):
        """Returns the year of the calling datetime object.

        Returns:
            int: year of the calling datetime object
        """
        return self.__year
    
    def setYear(self, year: int):
        """Sets the year of the calling datetime object to the specified year and
        recomputes the universal datetime of the calling datetime object.

        Args:
            year (int): specified year
        """
        self.__year = year
        self.__datetime = f"{self.__year}-{self.__month:02d}-{self.__day:02d} {self.getTime()}"

    def getMonth(self):
        """Returns the month of the calling datetime object.

        Returns:
            int: month of the calling datetime object
        """
        return self.__month
    
    def setMonth(self, month: int):
        """Sets the month of the calling datetime object to the specified month and
        recomputes the universal datetime of the calling datetime object.

        Args:
            month (int): specified month

        Raises:
            ValueError: indicates specified month is less than 0 or greater than 12
        """
        try:
            if (month <= 0 or month > 12):
                raise ValueError("Invalid month!")          
        except ValueError as e:
            exit(e)
        else:
            self.__month = month
            self.__datetime = f"{self.__year}-{self.__month:02d}-{self.__day:02d} {self.getTime()}"

    def getDay(self):
        """Returns the day of the calling datetime object.

        Returns:
            int: day of the calling datetime object
        """
        return self.__day
    
    def setDay(self, day: int):
        """Sets the day of the calling datetime object to the specified day and
        recomputes the universal datetime of the calling datetime object.

        Args:
            day (int): specified day

        Raises:
            ValueError: indicates specified day is less than 0 or greater than 31
        """
        try:
            if (day <= 0 or day > 31):
                raise ValueError("Invalid day!")          
        except ValueError as e:
            exit(e)
        else:
            self.__day = day
            self.__datetime = f"{self.__year}-{self.__month:02d}-{self.__day:02d} {self.getTime()}"
    
    def __str__(self):
        """Returns string representation of the calling datetime object.

        Returns:
            str: string representation of the calling datetime object
        """
        return f"datetime={self.__datetime}"
    
    def __eq__(self, other):
        """Tests if the calling datetime object is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling datetime object is equal to the specified
            object, else False
        """
        if other is not None:
            if isinstance(other, datetime):
                if other.__datetime == self.__datetime:
                    return True
        return False