from madlib import *

def main():
    # display madlib without noun, verb, adverb, and adjective
    madlib.show()

    # create an madlib object named m1
    # that has a noun equal to dog, verb equal to walk,
    # adverb equal to quickly, and adjective equal to blue
    m1 = madlib("dog", "walk", "quickly", "blue")

    # display string representation of m1
    print(m1)

    # display formatted madlib of m1
    print(m1.generate())

    # create an madlib object named m2
    # that has a noun equal to peas, verb equal to eat,
    # adverb equal to eagerly, and adjective equal to mushy
    m2 = madlib("peas", "eat", "eagerly", "mushy")

    # display string representation of m2
    print(m2)

    # display formatted madlib of m2
    print(m2.generate())

    # create an madlib object named m3
    # that has a noun equal to Maserati, verb equal to drive,
    # adverb equal to cautiously, and adjective equal to luxury
    m3 = madlib("Maserati", "drive", "cautiously", "luxury")

    # display string representation of m3
    print(m3)

    # display formatted madlib of m3
    print(m3.generate())

    # display the result of testing if m1 is equal to m2
    print("m1 equals m2?", m1.__eq__(m2))

    # display the result of testing if m1 is equal to m3
    print("m1 equals m3?", m1.__eq__(m3))

    # display the result of testing if m3 is equal to m2
    print("m3 equals m2?", m3.__eq__(m2))

    # use getter and setter methods to make m2 the same madlib
    # as m3
    m2.setNoun(m3.getNoun())
    m2.setVerb(m3.getVerb())
    m2.setAdverb(m3.getAdverb())
    m2.setAdjective(m3.getAdjective())

    # display the result of testing if m3 is equal to m2
    print("m3 equals m2?", m3.__eq__(m2))

    # test constructor to ensure ValueErrors are being raised appropriately
    # m4 = madlib(None, "walk", "quickly", "blue")
    # m4 = madlib("dog", None, "quickly", "blue")
    # m4 = madlib("dog", "walk", None, "blue")
    # m4 = madlib("dog", "walk", "quickly", None)

if __name__ == "__main__":
    main()