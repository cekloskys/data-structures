from selectionsort import *

def main():
    
    names = ['Emma', 'Brian', 'Evelyn', 'Frank', 'Alex', 'Felecia', 'Carl']
    scores = [99, 85, 64, 78, 95, 50, 88]
    
    print("ORIGINAL LISTS")
    print("%s\t\t%s" % ("Names", "Scores"))
    i = 0
    while (i < len(names)):
        print("%s\t\t%d" % (names[i], scores[i]))
        i += 1

    # Call sort method
    sort(names, scores, 0)

    print("\nSORTED LISTS")
    print("%s\t\t%s" % ("Names", "Scores"))
    i = 0
    while (i < len(names)):
        print("%s\t\t%d" % (names[i], scores[i]))
        i += 1
    
if __name__ == "__main__":
    main()