def sort (data, last: int):
    """Sorts a list of ints from smallest to largest
    bypassing the elements to the right of last.

    Args:
        data (int): list of integers
        last (int): the list index at which the sort will end
    """
    # declare loop counter variables
    i = 0
    j = 0    
        
    # declare variable named small to store index of smallest value
    small = 0

    # declare variable named temp used to swap array values
    temp = 0

    # loop through list as many times as specified by last 
    while (i < last):
        # set small equal to last
        small = last

        # loop through list starting with element at last - 1
        # and continue until reach the first element
        j = last - 1
        while (j >= i):
            # if the value in small is greater than the current value
            if (data[small] > data[j]):
                # set small equal to the index of current value
                small = j
            
            # decrement j
            j = j - 1
        
        # swap the data in i with the data in small
        # set temp to value in i
        temp = data[i]
        # set value in i to value in small
        data[i] = data[small]
        # set value in small to temp
        data[small] = temp
        
        # increment i
        i = i + 1