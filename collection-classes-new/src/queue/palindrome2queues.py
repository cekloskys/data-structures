from queue.queue import *
from stack.stack import *

class palindrome2queues:
    @staticmethod
    def isPalindrome2queues(expression: str):
        """Checks if the specified expression reads the same
        forward and backward.

        Args:
            expression (str): specified expression

        Returns:
            Boolean: True if the specified expression reads the same, else Fals.
        """        
        q1 = queue() # queue to read the expression forward
        q2 = queue() # queue to read the expression backward

        mismatches = 0  # used to keep track of the differences in the queue and stack

        # loop through expression forward to backward a character at a time
        for e in expression: 
            # if the current character is an alphabetic character
            if e.isalpha():
                # enqueue it
                q1.enqueue(e)

        # loop through expression backward to forward a character at a time
        i = len(expression) - 1
        while (i >= 0):
            # if the current character is an alphabetic character
            if expression[i].isalpha():
                # enqueue it
                q2.enqueue(expression[i])
            i -= 1

        # while the queue isn't empty
        while(not q1.isEmpty()):
            # if the element at the front of the queue 1 isn't
            # equal to the element at the front of the queue 2
            if (q1.dequeue() != q2.dequeue()):
                # increment mismatches
                mismatches = mismatches + 1

        # return True if mismatches equals 0, else return False
        return (mismatches == 0)