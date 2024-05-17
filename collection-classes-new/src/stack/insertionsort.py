from node.node import *
from stack.stack import *

def insertionsort (data: stack, first: int):
    """Sorts a stack from smallest to largest
    bypassing the nodes to the left of first.

    Args:
        data (stack): stack to be sorted
        first (int): the node position at which 
        the sort will begin
    """
    # declare loop counter variables
    i = 1 
    j = 0    
        
    # declare variable for next value
    nextVal = 0

    # loop through stack as many times as specified by
    # the size of data and first 
    while (i <= data.size() - first):
        # store copy of the number in node position first + i in 
        # next value
        # nextVal = data[first + i]
        nextVal = node.listPosition(data.getHead(), first + i).getData()

        # loop through the stack starting at same node position as next value
        # and iterate back toward first as long as the node value 
        # to the left of next value is greater than
        # next value and we're not the whole way back first
        j = first + i
        
        # while ((j > first) and (data[j - 1] > nextVal)):
        while ((j > first) and (node.listPosition(data.getHead(), j - 1).getData() > nextVal)):
            # shift node value to the left of next value rightward one position
            # data[j] = data[j - 1];  
            data.getHead().setDataAtPosition(j, node.listPosition(data.getHead(), j - 1).getData())
            # insert next value in node value that was just shifted
            # data[j - 1] = nextVal; 
            data.getHead().setDataAtPosition(j - 1, nextVal)
            
            # decrement j
            j = j - 1
        
        # increment i
        i = i + 1