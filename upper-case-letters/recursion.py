class recursion:
    @staticmethod 
    def count(string: str, count: int):
        """Uses recursion to count the uppercase letters
        in a specified string.

        Args:
            string (str): specified string
            count (int): count of uppercase letters

        Returns:
            int: count of uppercase letters
        """  
        if (len(string) == 0):
            return count
        else:
            if (string[0].isupper()):
                count += 1
                return recursion.count(string[1:], count)
            else:
                return recursion.count(string[1:], count)