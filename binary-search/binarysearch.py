def search (a, first: int, target: int):
    """Searches part of a sorted list for a specified target starting at a[first].

    Args:
        a (int): the list to search
        first (int): the list index at which the search will start
        target (int): the element to search for

    Returns:
        int: If target appears in the list, index of the, element 
        that contains target; else -1.
    """
    # set a boolean variable found to false
    # will be set to true if the target is found
    found = False
        
    # Set an int variable size to the list
    # length minus first.
    size = len(a) - first
        
    # Set an int variable middle to first
    # plus size divided by two.
    middle = int(first + size / 2)
        
    # If there are no more elements to search (size is 
    # less than or equal to zero), target element isn't
    # in list; therefore return -1.
    if (size <= 0):
            return -1
    else:
        # While there are no more elements to search 
        # (size is greater than zero) and the target 
        # hasn't been found.
        while ((size > 0) and not found):
            # If the middle element is the target
            # set found to true
            if (a[middle] == target):
                found = True
            elif (a[middle] > target):
                # Else if middle element is greater
                # than the target, recompute size.
                size = int(size / 2)
            else:
                # Else if middle element is less
                # than the target, recompute first
                # and size.
                first = middle + 1
                size = int((size - 1) / 2)
                
            # Recompute middle.
            middle = int(first + size / 2)
        
    # Check if target was found.  If it
    # was, return middle, else return -1.
    if (found):
        return middle
    else:
        return -1