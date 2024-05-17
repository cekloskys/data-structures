from node.node import *
from stack.stack import *

def selectionsort (data: stack, first: int):
    """Sorts a stack from smallest to largest
    bypassing the nodes to the left of first.

    Args:
        data (stack): stack to be sorted
        first (int): the node position at which 
        the sort will begin
    """
    # initialize loop counter variables
    i = data.size() - first # - 1 
    j = 0    
        
    # initialize variable named big to store index of biggest value
    big = 0

    # initialize variable named temp used to swap array values
    temp = 0

    # loop through list as many times as specified by
    # data length and first 
    # blue arrow
    while (i > 0):
        # set big equal to first
        big = first

        # loop through list starting with element at first + 1
        # and continue until reach first + i
        # yellow arrow
        j = first + 1
        while (j <= first + i):
            # if the value in big is less than the current value
            # if (data[big] < data[j]):
            if (node.listPosition(data.getHead(), big).getData() < node.listPosition(data.getHead(), j).getData()):
                # set big equal to the index of current value
                big = j
            
            # increment j
            j = j + 1
        
        # swap the data in first + i with the data in big
        # set temp to value in first + i
        # temp = data[first + i]
        temp = node.listPosition(data.getHead(), first + i).getData()
        # set value in first + i to value in big
        # data[first + i] = data[big]
        data.getHead().setDataAtPosition(first + i, node.listPosition(data.getHead(), big).getData())
        # set value in big to temp
        # data[big] = temp
        data.getHead().setDataAtPosition(big, temp)
        
        # decrement i
        i = i - 1