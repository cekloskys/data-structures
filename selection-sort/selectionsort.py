def sort (data, first: int):
    """Sorts a list of ints from smallest to largest
    bypassing the elements to the left of first.

    Args:
        data (int): list of integers
        first (int): the list index at which the sort will begin
    """
    # initialize loop counter variables
    i = len(data) - first - 1 
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
            if (data[big] < data[j]):
                # set big equal to the index of current value
                big = j
            
            # increment j
            j = j + 1
        
        # swap the data in first + i with the data in big
        # set temp to value in first + i
        temp = data[first + i]
        # set value in first + i to value in big
        data[first + i] = data[big]
        # set value in big to temp
        data[big] = temp
        
        # decrement i
        i = i - 1