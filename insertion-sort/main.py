from insertionsort import *

def main():
    """Prompts user for input and calls insertion sort function.
    """
    # Set up local variables to store the list 
    # first, size, and target.
    data = []
    first = 0

    # Prompt the user for the elements and input
    # them into the list.
    data = list(map(int, input("Enter ten numbers separated by a space: ").split()))
    # data = list(map(str, input("Enter ten numbers separated by a space: ").split()))

    # Prompt user for index at which sort will 
    # begin.
    first = int(input("Enter the index at which the search will begin: "))

    # Display the original unsorted array.
    for i in data:
        print(i, end=" ")

    # Call sort method
    sort(data, first)

    print()

    # Display the sorted array.
    for i in data:
        print(i, end=" ")
    
if __name__ == "__main__":
    main()

    """ TEST DATA 
        FIRST DATA SET
        data = 80 10 50 70 60 90 20 30 40 0
        first = 0
        
        SECOND DATA SET
        data = 80 10 50 70 60 90 20 30 40 0
        first = 5
        
        THIRD DATA SET
        data = 80 10 50 70 60 90 20 30 40 0
        first = 10
        
        FOURTH DATA SET
        data = 80 10 80 70 60 90 20 30 40 80
        first = 0 """