from circle.circle import *
from cylinder.cylinder import *

def main():
    # create a circle object named circle1 that has a radius of 3.0
    circle1 = circle(3.0)

    # display a string representation of circle1
    print(circle1)

    # create a circle object named circle2 that has a radius of 4.0
    circle2 = circle(4.0)

    # display a string representation of circle2
    print(circle2)

    # display the result of testing if circle1 is equal to circle2
    print("Is circle1 equal to circle2?", circle1.__eq__(circle2))

    # set the radius of circle2 to the radius of circle1
    circle2.setRadius(circle1.getRadius())

    # display a string representation of circle2
    print(circle2)

    # display the result of testing if circle1 is equal to circle2
    print("Is circle1 equal to circle2?", circle1.__eq__(circle2))

    # create a circle object named circle3 that has a radius of 5.0
    circle3 = circle(5.0)

    # create a circle object named circle4 that has a radius of 6.0
    circle4 = circle(6.0)

    # get the areas of circle1, circle2, circle3, and circle4
    # and store them in a list named areas
    areas = [circle1.getArea(), circle2.getArea(), circle3.getArea(), circle4.getArea()]

    # display the areas list
    print(areas)

    # sort the areas list from largest to smallest using the static
    # sort method in the circle class
    circle.sort(areas, 0)

    # display the areas list
    print(areas)

    # create a cylinder object named cylinder1 that has a radius of 7.0
    # and a height of 5.0
    cylinder1 = cylinder(7.0, 5.0)

    # display a string representation of cylinder1
    print(cylinder1)

    # create a cylinder object named cylinder1 that has a radius of 5.0
    # and a height of 7.0
    cylinder2 = cylinder(5.0, 7.0)

    # display a string representation of cylinder2
    print(cylinder2)

    # display the result of testing if cylinder1 is equal to cylinder2
    print("Is cylinder1 equal to cylinder2?", cylinder1.__eq__(cylinder2))

    # get the circumferences of circle1, circle2, circle3, circle4,
    # cylinder1, and cylinder2 and store them in a list named circumferences
    circumferences = [circle1.getCircumference(), circle2.getCircumference(), circle3.getCircumference(), circle4.getCircumference(),
                      cylinder1.getCircumference(), cylinder2.getCircumference()]
    
    # display the circumferences list
    print(circumferences)

    # using the static search method in the circle class iteratively search the 
    # circumferences list for the circumference of cylinder2
    # starting at index position 0 with the first iteration and going up to index
    # position len(circumferences) - 1 with the last iteration
    i = 0
    while (i < len(circumferences)):
        retval = circle.search(circumferences, i, len(circumferences), cylinder2.getCircumference())
        if retval == -1:
            print("Circumference %f no longer appears in list." % (cylinder2.getCircumference()))
        else:
            print("Circumference %f appears %d times." % (cylinder2.getCircumference(), retval))
        i += 1

if __name__ == "__main__":
    main()