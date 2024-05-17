def sort (names, scores, first: int):
    """Sorts a list of scores from smallest to largest and 
    sorts the list of names according to the order defined by 
    the sorted scores.

    Args:
        names: list of names
        scores: list of scores
        first (int): the list index at which the sort will begin
    """
    # initialize loop counter variables
    i = len(scores) - first - 1 
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
            if (scores[big] < scores[j]):
                # set big equal to the index of current value
                big = j
            
            # increment j
            j = j + 1
        
        # swap the data in first + i with the data in big
        # set temp to value in first + i
        temp = scores[first + i]
        # set value in first + i to value in big
        scores[first + i] = scores[big]
        # set value in big to temp
        scores[big] = temp

        # set temp to value in first + i
        temp = names[first + i]
        # set value in first + i to value in small
        names[first + i] = names[big]
        # set value in small to temp
        names[big] = temp
        
        # decrement i
        i = i - 1