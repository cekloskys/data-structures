from node.node import *
from stack.stack import *
from queue.queue import *
from loops import *
from recursion import *

def main():
    testNode()
    evenOrOdd()
    testRecursion()

def testNode():

    # Question 1
    s = node('K', None)
    s = node('C', s)
    s = node('A', s)
    s = node('T', s)
    s = node('S', s)
        
    # Question 2
    q = node('E', None)
    q = node('U', q)
    q = node('E', q)
    q = node('U', q)
    q = node('Q', q)
        
    # Question 3
    selection = s
        
    # Question 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
        
    # Question 5
    selection.setLink(q)
        
    # Question 6
    print('S contains', node.listLength(s), ('node' if node.listLength(s) == 1 else 'nodes'))
    print('Q contains', node.listLength(q), ('node' if node.listLength(q) == 1 else 'nodes'))

# Question 7
def evenOrOdd():
    odd = queue()
    even = stack()

    numbers = list(map(int, input("Enter ten numbers separated by a space: ").split()))
    for num in numbers:
        if (num % 2 != 0):
            odd.enqueue(num)

    for num in reversed(numbers):
        if (num % 2 == 0):
            even.push(num)

    print('Numbers is queue are', end=" ")
    while (not odd.isEmpty()):
        print(odd.dequeue(), end=" ")
    print()

    print('Numbers in stack are', end=" ")
    while (not even.isEmpty()):
        print(even.pop(), end=" ")
    print()

# Question 8
def testRecursion():
    # loops.sing(3)
    recursion.sing(3)
    
if __name__ == "__main__":
    main()