from node.node import *
from stack.stack import *
from queue.queue import *
from loops import *
from recursion import *
from queue.palindrome import *

def main():
    # testNode()
    # evenOrOdd()
    testRecursion()
    # santaClaus()
    getPalindromes()

def santaClaus():
    # Question 1
    s = node('S', None)
    santaCursor = s
    santaCursor.addNodeAfter('A')
    santaCursor = santaCursor.getLink()
    santaCursor.addNodeAfter('N')
    santaCursor = santaCursor.getLink()
    santaCursor.addNodeAfter('T')
    santaCursor = santaCursor.getLink()
    santaCursor.addNodeAfter('A')
        
    # Question 2
    c = node('C', None)
    clausCursor = c
    clausCursor.addNodeAfter('L')
    clausCursor = clausCursor.getLink()
    clausCursor.addNodeAfter('A')
    clausCursor = clausCursor.getLink()
    clausCursor.addNodeAfter('U')
    clausCursor = clausCursor.getLink()
    clausCursor.addNodeAfter('S')
        
    # Question 3
    selection = s
        
    # Question 4
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()
        
    # Question 5
    selection.setLink(c)

def getPalindromes():
    palindrom = stack()
    notPalindrome = stack()

    words = list(map(str, input("Enter ten words separated by a space: ").split()))
    for word in reversed(words):
        if (palindrome.isPalindrome(word)):
            palindrom.push(word)

    for word in reversed(words):
        if (not palindrome.isPalindrome(word)):
            notPalindrome.push(word)

    print('These words are palindromes:', end=" ")
    while (not palindrom.isEmpty()):
        print(palindrom.pop(), end=" ")
    print()

    print('These words are not palindromes', end=" ")
    while (not notPalindrome.isEmpty()):
        print(notPalindrome.pop(), end=" ")
    print()

def testRecursion():
    # loops.sing(3)
    # recursion.sing(3)
    print("LOOP")
    loops.evens(-10, 10)
    print("\nRECURSION")
    recursion.evens(-10, 10)

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
    
if __name__ == "__main__":
    main()