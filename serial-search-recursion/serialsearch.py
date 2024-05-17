def search (a, first: int, size: int, target, i: int, found: bool):
    """Searches for a desired element in a list of elements
    starting at a[first].

    Args:
        a: the list to search
        first (int): the list index at which the search will start
        size (int): the number of elements to search
        target: the element to search for
        i: the counter variable used to iterate through list
        found: the variable used to denote if the target has been found

    Returns:
        int: If target appears in the list, index of the element
        that contains the target, else -1.
    """  
    if (i == size or found or i + first == len(a)):
            if (found):
                # return the index of the target
                return i + first
            else:
                # return negative 1
                return -1
    else:
        # if the current element is the target
        if (a[i + first] == target):
            # set found to True
            found = True
            return search(a, first, size, target, i, found)
        else:
            # increment the counter variable i by 1
            i += 1
            return search(a, first, size, target, i, found)