def sort (data, first: int):
    """Sorts a list of integers from largest to smallest
    bypassing the elements to the left of first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin
    """
    # declare loop counter variables
    i = len(data) - first - 1 
    j = 0    
        
    # declare variable named small to store index of smallest value
    small = 0

    # declare variable named temp used to swap array values
    temp = 0

    # loop through list as many times as specified by
    # data length and first 
    while (i > 0):
        # set small equal to first
        small = first

        # loop through list starting with element at first + 1
        # and continue until reach first + i
        j = first + 1
        while (j <= first + i):
            # if the value in small is greater than the current value
            if (data[small] > data[j]):
                # set small equal to the index of current value
                small = j
            
            # increment j
            j = j + 1
        
        # swap the data in first + i with the data in small
        # set temp to value in first + i
        temp = data[first + i]
        # set value in first + i to value in small
        data[first + i] = data[small]
        # set value in small to temp
        data[small] = temp
        
        # decrement i
        i = i - 1