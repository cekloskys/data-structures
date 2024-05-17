def sort (names, grades, first: int):
    """Sorts a list of grades from largest to smallest and 
    sorts the list of names according to the order defined by 
    the sorted grades.

    Args:
        names: list of names
        grades: list of grades
        first (int): the list index at which the sort will begin
    """
    # declare loop counter variables
    i = len(grades) - first - 1 
    j = 0    
        
    # declare variable named small to store index of smallest value
    small = 0

    # declare variable named temp used to swap array values
    temp = ''

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
            if (grades[small] > grades[j]):
                # set small equal to the index of current value
                small = j
            
            # increment j
            j = j + 1
        
        # swap the data in first + i with the data in small
        # set temp to value in first + i
        temp = grades[first + i]
        # set value in first + i to value in small
        grades[first + i] = grades[small]
        # set value in small to temp
        grades[small] = temp

        # set temp to value in first + i
        temp = names[first + i]
        # set value in first + i to value in small
        names[first + i] = names[small]
        # set value in small to temp
        names[small] = temp
        
        # decrement i
        i = i - 1