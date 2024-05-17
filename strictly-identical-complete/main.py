from serialsearch import *

def main():
    # Initialize the lists.
    list1 = ['E', 'B', 'E', 'F', 'A', 'F']
    list2 = ['E', 'B', 'E', 'F', 'A', 'F'] 

    # list1 = ['E', 'B', 'E', 'F', 'A', 'C']
    # list2 = ['E', 'B', 'E', 'F', 'A', 'F'] 

    # list1 = ['E', 'B', 'E', 'F', 'A', 'F', 'C']
    # list2 = ['E', 'B', 'E', 'F', 'A', 'F'] 

    # Initialze variable that will store the return
    # from the serial search function.
    index = 0

    # Check if two lists are the same length.
    strictlyIdentical = (len(list1) == len(list2))

    # If the two lists are the same length.
    if (strictlyIdentical):

        # Loop through list1 an element at a time.
        i = 0
        while (i < len(list1)):
            # Search list2 (a = list2), 
            # Starting at index position i (first = i),
            # Searching only 1 element (size = 1)
            # Searching for the current element in list1 (target = list1[i]) 
            # index = search(list2, i, 1, list1[i])
            index = search(list2, i, 1, list1[i])
            # If list2[i] = list1[i], search will return i
            # If list2[i] != list1[i], search will return -1 and this means the lists
            # are not strictly identical.
            if (index != i):
                strictlyIdentical = False
            # Increment loop counter variable.
            i += 1

    if (not strictlyIdentical):
        print("Two lists aren't strictly identical!")
    else:
        print("Two lists are strictly identical!")

    print(list1)
    print(list2)

if __name__ == "__main__":
    main()