# prompt user to input integers between 1 and 10 separated by a space
# split input numbers using a white space
# store numbers in a list
nums = [int(nums) for nums in input("Enter multiple integers between 1 and 10 separated by a space\n(push Enter to stop): ").split()]

# output numbers
print("Number are: ", nums)

# create a list of 11 integers
# this list will store the count of the appearances of each input integer
# counts[1] will store the count of the appearances of 1
# counts[2] will store the count of the appearances of 2
# counts[3] will store the count of the appearances of 3
# ...
# counts[10] will store the count of the appearances of 10
counts = [0,0,0,0,0,0,0,0,0,0,0]

# loop through the input integers
i = 0
while (i < len(nums)):
    # increment the appropriate element in counts
    counts[nums[i]] += 1
    i += 1

# loop through counts
i = 1
while (i < len(counts)):
    # print the count of each input integer
    if (counts[i] != 0):
        # use the ternary operator to control when the word times or time appears
        print(i, 'appears', counts[i], ('times.' if (counts[i] > 1) else 'time.'))
    i += 1