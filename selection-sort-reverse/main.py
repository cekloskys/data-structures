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

    # Prompt user for index at which sort will 
    # end.
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