lyrics = {1: "A partridge in a pear tree",
          2: "Two turtledoves",
          3: "Three French hens",
          4: "Four calling birds",
          5: "Five golden rings",
          6: "Six geese a-laying",
          7: "Seven swans a-swimming",
          8: "Eight maids a-milking",
          9: "Nine ladies dancing",
          10: "Ten lords a-leaping",
          11: "Eleven pipers piping",
          12: "Twelve drummers drumming"}

number = {1: "first",
          2: "second",
          3: "third",
          4: "fourth",
          5: "fifth",
          6: "sixth",
          7: "seventh",
          8: "eighth",
          9: "nineth",
          10: "tenth",
          11: "eleventh",
          12: "twelfth"}

day = int(input("Please enter a number (1 - 12): "))

if (day >= 1 and day <= 12):
    print("On the %s day of Christmas, my true love gave to me ..." % (number[day]))
    i = day
    while (i >= 1):
        print(lyrics[i])
        i -= 1
else:
    print("Invalid number!")