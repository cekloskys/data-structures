from binarysearch import *

def main():
    """Prompts user for input and calls binary search function.
    """
    # Set up local variables to store the list 
    # first, size, and target.
    a = []
    first = 0
    target = 0

    # Prompt the user for the elements and input
    # them into the list.
    a = list(map(int, input("Enter ten numbers in ascending order separated by a space: ").split()))

    # Prompt user for index at which search will 
    # begin.
    first = int(input("Enter the index at which the search will begin: "))

    # Prompt the user for the target.
    target = int(input("Enter the element to search for: "))

    # Call search method and display its return.
    print('Target found at index ... ', search(a, first, target))

if __name__ == "__main__":
    main()

""" TEST DATA
    FIRST DATA SET
        a = 1 2 3 4 5 6 7 8 9 10
        first = 0
        target = 5 
        
    SECOND DATA SET
        a = 1 2 3 4 5 6 7 8 9 10
        first = 5
        target = 5
        
    THIRD DATA SET
        a = 1 2 3 4 5 6 7 8 9 10
        first = 0
        target = 12
        
    FOURTH DATA SET
        a = 1 2 3 4 5 6 7 8 9 10
        first = 5
        target = 7
                
    FIFTH DATA SET
        a = 1 2 3 4 5 6 7 8 9 10
        first = 11
        target = 5 """