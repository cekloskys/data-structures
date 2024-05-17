class loops:
    @staticmethod 
    def count(string: str, count: int):
        """Uses a loop to count the uppercase letters
        in a specified string.

        Args:
            string (str): specified string
            count (int): count of uppercase letters

        Returns:
            int: count of uppercase letters
        """        
        while (len(string) != 0):
            if (string[0].isupper()):
                count += 1
            # get substring starting at position 1
            string = string[1:]

        return count