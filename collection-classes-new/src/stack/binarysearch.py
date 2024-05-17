from node.node import *
from stack.stack import *

def binarysearch (a: stack, first: int, target: int):
    """Searches part of a sorted stack for a specified target starting at node position first.

    Args:
        a (stack): the stack to search
        first (int): the node posision at which the search will start
        target: the target value to search for

    Returns:
        int: If target appears in the stack, position of the node 
        that contains target value; else -1.
    """
    # set a boolean variable found to false
    # will be set to true if the target is found
    found = False
        
    # Set an int variable size to the stack
    # size minus first.
    size = a.size() - first
        
    # Set an int variable middle to first
    # plus size divided by two.
    middle = int(first + size / 2)
        
    # If there are no more elements to search (size is 
    # less than or equal to zero), target element isn't
    # in stack; therefore return -1.
    if (size <= 0):
            return -1
    else:
        # While there are no more elements to search 
        # (size is greater than zero) and the target 
        # hasn't been found.
        while ((size > 0) and not found):
            # If the middle element is the target
            # set found to true
            # if (a[middle] == target):
            if (node.listPosition(a.getHead(), middle).getData() == target):
                found = True
            # elif (a[middle] > target):
            elif (node.listPosition(a.getHead(), middle).getData() > target):
                # Else if middle element is greater
                # than the target, recompute size.
                size = int(size / 2)
            else:
                # Else if middle element is less
                # than the target, recompute first
                # and size.
                first = middle + 1
                size = int((size - 1) / 2)
                
            # Recompute middle.
            middle = int(first + size / 2)
        
    # Check if target was found.  If it
    # was, return middle, else return -1.
    if (found):
        return middle
    else:
        return -1