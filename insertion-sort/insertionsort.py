def sort (data, first: int):
    """Sorts a list of integers from smallest to largest
    bypassing the elements to the left of first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin
    """
    # declare loop counter variables
    i = 1 
    j = 0    
        
    # declare variable for next value
    nextVal = 0

    # loop through list as many times as specified by
    # data length and first 
    while (i < len(data) - first):
        # store copy of the number in index position first + i in 
        # next value
        nextVal = data[first + i]

        # loop through the list starting at same index as next value
        # and iterate back toward first as long as the element 
        # to the left of next value is greater than
        # next value and we're not the whole way back first
        j = first + i
        while ((j > first) and (data[j - 1] > nextVal)):
            # shift element to the left of next value rightward one position
            data[j] = data[j - 1];  
            # insert next value in element that was just shifted
            data[j - 1] = nextVal; 
            
            # decrement j
            j = j - 1
        
        # increment i
        i = i + 1