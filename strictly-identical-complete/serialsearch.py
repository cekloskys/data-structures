def search (a, first: int, size: int, target):
    """Searches for a desired element in an list of elements
    starting at a[first].

    Args:
        a : the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target (int): the element to search for

    Returns:
        int: If target appears in the list, index of the, element 
        that contains target; else -1.
    """
    # set an int counter variable i to 0
    i = 0

    # set a boolean variable found to false
    # will be set to true if the target is found
    found = False

    # while there are more elements to search
    # and the target hasn't been found
    # and i plus first doesn't exceed the length
    # of the list
    while ((i < size) and (i + first < len(a)) and not found):
        # if the current element is the target
        if (a[i + first] == target):
            # set found to true
            found = True
        else:
            # increment counter variable i by 1
            i = i + 1
    # check if the target was found
    if (found):
        # return index of target
        return i + first
    else:
        # return negative 1
        return -1