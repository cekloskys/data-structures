from selectionsort import *

def main():
    
    names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felecia', 'Carl']
    grades = ['A', 'B', 'D', 'C', 'A', 'F', 'B']
    
    print("ORIGINAL LISTS")
    print("%s\t\t%s" % ("Names", "Grades"))
    i = 0
    while (i < len(names)):
        print("%s\t\t%s" % (names[i], grades[i]))
        i += 1

    # Call sort method
    sort(names, grades, 0)

    print("\nSORTED LISTS")
    print("%s\t\t%s" % ("Names", "Grades"))
    i = 0
    while (i < len(names)):
        print("%s\t\t%s" % (names[i], grades[i]))
        i += 1
    
if __name__ == "__main__":
    main()