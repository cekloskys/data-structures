from serialsearch import *

def main():
    """Prompts user for input and calls serial search function.
    """
    # Set up local variable to store the list values.
    # sorted_list = [1, 1, 2, 2, 4, 4, 5, 5, 6, 6]
    # sorted_list = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8]
    sorted_list = [1, 1, 3, 3, 4, 4, 5, 5, 7, 7, 8] 

    # Set up local variable to store value that appears only once.
    # Initialize variable to -1. Initial value will be changed to value 
    # that appears only once if such value exists in array.
    ans = -1

    # Loop through array incrementing counter by 2 with each iteration.
    i = 0
    while (i < len(sorted_list)):
        # Search for the same value, sorted_list[i], in consecutive index positions
        if((search(sorted_list, i, 1, sorted_list[i]) == -1) or 
           (search(sorted_list, i + 1, 1, sorted_list[i]) == -1)):
            # If the same value isn't in consecutive index positions, then
            # we have a value that appears only once, so we store it in ans.
            ans = sorted_list[i];
            break;
        i += 2
    
    # Display results.
    if (ans == -1):
        print("All values appear twice.")
    else:
        print(ans, "appears only once.")

if __name__ == "__main__":
    main()