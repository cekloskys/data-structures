from serialsearchcomplete import *

print(__name__)

def main():
    """Prompts user for input and calls serial search function.
    """
    # Set up local variables to store the list 
    # first, size, and target.
    a = []
    first = 0
    size = 0
    target = 0

    # Prompt the user for the elements and input
    # them into the list.
    a = list(map(int, input("Enter seven numbers separated by a space: ").split()))

    # Prompt user for index at which search will 
    # begin.
    first = int(input("Enter the index at which the search will begin: "))

    # Prompt the user for the number of elements that 
    # will be searched.
    size = int(input("Enter the size of the array that will be searched: "))

    # Prompt the user for the target.
    target = int(input("Enter the element to search for: "))

    # Call search method and display its return.
    # print('Target found at index ... ', search(a, first, size, target))

    if (search(a, first, size, target) == -1):
        print(target, "not found.")
    else:
        print(target, "found at index position", search(a, first, size, target))
        i = search(a, first, size, target) + 1
        print("Values not searched:")
        while (i < len(a)):
            print(a[i], sep=" ", end=" ")
            i += 1
        print()

def mainstr():
    # set up local variables to store the list, first, size, and target
    a = []
    first = 0
    size = 0
    target = ''

    # prompt the user for the elements and input them into the list
    a = list(map(str, input("Enter seven names separated by a space: ").split()))

    # promt the user for the index at which the search will begin
    first = int(input("Enter the index at which the search will begin: "))

    # prompt the user for the number of elements to search 
    size = int(input("Enter the size of the list that will be searched: "))

    # prompt the user for the target
    target = input("Enter the target value to search for: ")

    # call search and display its return
    print('Target found at index ... ', search(a, first, size, target))

# When a Python script is run, the interpreter sets the __name__ variable to the string 
# ‘__main__‘ if the script is the main program being executed. If the script is being 
# imported as a module, then the __name__ variable is set to the name of the module instead.

# By checking the value of name using the if __name__ == '__main__' condition, 
# you can control which code is executed in different scenarios. If the condition is True, 
# then the indented code block following the conditional statement is executed. If it is 
# False, the code block is skipped. This allows you to create scripts that can be used 
# both as standalone programs and as modules in larger projects.
if __name__ == "__main__":
    main()
else:
    mainstr()

""" FIRST DATA SET
        a = -7 42 70 39 3 63 8
        first = 0
        size = 7
        target = 39 
        
    SECOND DATA SET
        a = -7 42 70 39 3 63 8
        first = 2
        size = 7
        target = 39 
    THIRD DATA SET
        a = -7 42 70 39 3 63 8
        first = 0
        size = 7
        target = 5 
        
    FOURTH DATA SET
        a = -7 42 70 39 3 63 8
        first = 2
        size = 7
        target = 5 
        
    FIFTH DATA SET
        a = -7 42 70 39 3 63 8
        first = 0
        size = 10
        target = 39 
        
    SIXTH DATA SET
        a = -7 42 70 39 3 63 8
        first = 0
        size = 10
        target = 5 
        
    SEVENTH DATA SET
        a = -7 42 70 39 3 63 8
        first = 10
        size = 7
        target = 5 
        
    EIGHTH DATA SET
        a = -7 42 70 39 3 63 8
        first = 10
        size = 7
        target = 39 """