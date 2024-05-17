# from selectionsort import *
# from selectionsortdecreasing import *
from selectionsortreverse import *

def main():
    """Prompts user for input and calls selection sort function.
    """
    # Set up local variables to store the list 
    # first, size, and target.
    data = []
    first = 0

    # Prompt the user for the elements and input
    # them into the list.
    data = list(map(int, input("Enter ten numbers separated by a space: ").split()))
    # data = list(map(str, input("Enter ten strings separated by a space: ").split()))

    # Prompt user for index at which sort will 
    # begin.
    first = int(input("Enter the index at which the search will end: "))

    # Display the original unsorted array.
    for i in data:
        print(i, end=" ")

    # Call sort method
    # Data is being passed by reference.
    sort(data, first)

    print()

    # Display the sorted array.
    for i in data:
        print(i, end=" ")
    
if __name__ == "__main__":
    main()

""" TEST DATA
        FIRST DATA SET
        a = 80 10 50 70 60 90 20 30 40 0
        first = 0
        
        SECOND DATA SET
        a = 80 10 50 70 60 90 20 30 40 0
        first = 5
        
        THIRD DATA SET
        a = 80 10 50 70 60 90 20 30 40 0
        first = 10
        
        FOURTH DATA SET
        a = 80 10 80 70 60 90 20 30 40 80
        first = 0 """