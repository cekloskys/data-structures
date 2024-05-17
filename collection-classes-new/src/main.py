from node.node import *
from linkedlist.linkedlist import *
from stack.stack import *
from stack.balancedparens import *
from stack.calculator import *
from queue.queue import *
from queue.palindrome import *
from queue.palindrome2queues import *
from queue.palindromedetected import *
from stack.serialsearch import *
from stack.binarysearch import *
from stack.insertionsort import *
from stack.selectionsort import *

def main():
    
    # testConstructor()
    # testGettersAndSetters()
    # testAddNodeAfter()
    # testRemoveNodeAfter()
    # review()
    # testListLength()
    # testListSearch()
    # testListPosition()
    # testListCopy()
    # testListCopyWithTail()
    # testListPart()
    # module6PracticeAssignment()
    # assignment()
    
    # linked list unit test methods
    # testAdd()
    # testAddMany()
    # testAddAll()
    # testRemove()
    # testEquals()

    # stack unit test methods
    # testPush()
    # testPeek()
    # testPop()
    # testIsEmpty()
    # print("Parenthesis are balanced ?", balancedparens.isBalanced("{X+Y"))
    # print("Parenthesis are balanced ?", balancedparens.isBalanced("{X+Y)"))
    # print("Parenthesis are balanced ?", balancedparens.isBalanced("({X+Y}*Z)"))
    # print("Parenthesis are balanced ?", balancedparens.isBalanced("[A+B]*({X+Y}*Z)"))
    # print("(((6+9)/3)*(6-4)) =", calculator.evaluate("(((6+9)/3)*(6-4))"))
    # print("(6+(3*(6-4))) =", calculator.evaluate("(6+(3*(6-4)))"))
    # print("((5+2)-(3*(6/9))) =", calculator.evaluate("((5+2)-(3*(6/9)))"))
    # print("((5*2)-(3*(6/2))) =", calculator.evaluate("((5*2)-(3*(6/2)))"))

    # testSerialSearch()
    # testBinarySearch()
    # testInsertionSort()
    # testSelectionSort()

    # queue unit test methods
    # testEnqueue()
    # testDequeue()
    # testQueueIsEmpty()
    # testPeekQueue()
    # testIsPalindrome()
    # isPalindrome2queues()
    isPalindromeDetected()

def testEnqueue():
    print("Testing Enqueue Method in Queue Class")

    q = queue()
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    q.enqueue('S')
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    q.enqueue('B')
    # q.enqueue(1)
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    q.enqueue('O')
    # q.enqueue((1,2))
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    q.enqueue('J')
    # q.enqueue([1,2,3])
    print("Queue size is:", q.size())
    print("Queue contains:", q)

def testDequeue():
    print("Testing Dequeue Peek Function")

    q = queue()
    q.enqueue('J')
    q.enqueue('O')
    q.enqueue('B')
    q.enqueue('S')

    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Just dequeued:", q.dequeue())

    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Just dequeued:", q.dequeue())

    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Just dequeued:", q.dequeue())

    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Just dequeued:", q.dequeue())
       
def testQueueIsEmpty():
    print("Testing Queue Is Empty Function")

    q = queue()
    q.enqueue('J')
    q.enqueue('O')
    q.enqueue('B')
    q.enqueue('S')

    print("Queue size is:", q.size())
    print("Queue contains:", q)

    while(not q.isEmpty()):
        print("Just dequeued:", q.dequeue())

    print("Queue size is:", q.size())
    print("Queue contains:", q)

def testPeekQueue():
    print("Testing Queue Peek Function")

    q = queue()
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    q.enqueue('J')
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Front element in queue is:", q.peek())
    q.enqueue('O')
    # q.push(1)
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Front element in queue is:", q.peek())
    q.enqueue('B')
    # q.push((1,2))
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Front element in queue is:", q.peek())
    q.enqueue('S')
    # q.push([1,2,3])
    print("Queue size is:", q.size())
    print("Queue contains:", q)
    print("Front element in queue is:", q.peek())

def testIsPalindrome():
    print("Testing Is Palindrome Function")

    exp = input("Please enter an expression: ")
    exp = exp.upper()

    if (palindrome.isPalindrome(exp)):
        print("Your expression is a palindrome.")
    else:
        print("Your expression is not a palindrome.")

def isPalindrome2queues():

    while True:
        exp = input("Please enter an expression: ")
        exp = exp.upper()

        if (len(exp.strip()) == 0):
            break

        if (palindrome2queues.isPalindrome2queues(exp)):
            print("Your expression is a palindrome.")
        else:
            print("Your expression is not a palindrome.")

    print("Good bye!")

def isPalindromeDetected():

    while True:
        exp = input("Please enter an expression: ")

        if (len(exp.strip()) == 0):
            break

        palindromedetected.isPalindromeDetected(exp)
        
    print("Good bye!")

def testSelectionSort():

    # create an empty stack
    a = stack()
    # initialize first
    first = 6

    # push -7 onto the top of the stack
    a.push(-7)
    # push 42 onto the top of the stack
    a.push(42)
    # push 70 onto the top of the stack
    a.push(70)
    # push 39 onto the top of the stack
    a.push(39)
    # push 3 onto the top of the stack
    a.push(3)
    # push 63 onto the top of the stack
    a.push(63)
    # push 8 onto the top of the stack
    a.push(8)     # [8 63 3 39 70 42 -7]

    # print unsorted stack
    print("Unsorted stack:", a)

    # call selection sort method
    selectionsort(a, first)

    # print sorted stack
    print("Sorted stack:",a)

def testInsertionSort():

    # create an empty stack
    a = stack()
    # initialize first
    first = 6

    # push -7 onto the top of the stack
    a.push(-7)
    # push 42 onto the top of the stack
    a.push(42)
    # push 70 onto the top of the stack
    a.push(70)
    # push 39 onto the top of the stack
    a.push(39)
    # push 3 onto the top of the stack
    a.push(3)
    # push 63 onto the top of the stack
    a.push(63)
    # push 8 onto the top of the stack
    a.push(8)     # [8 63 3 39 70 42 -7]

    # print unsorted stack
    print("Unsorted stack:", a)

    # call insertion sort method
    insertionsort(a, first)

    # print sorted stack
    print("Sorted stack:",a)

def testBinarySearch():
    # create an empty stack
    a = stack()
    # initialize first
    first = 1
    # initialize target
    target = 2

    # push 7 onto the top of the stack
    a.push(7)
    # push 6 onto the top of the stack
    a.push(6)
    # push 5 onto the top of the stack
    a.push(5)
    # push 4 onto the top of the stack
    a.push(4)
    # push 3 onto the top of the stack
    a.push(3)
    # push 2 onto the top of the stack
    a.push(2)
    # push 1 onto the top of the stack
    a.push(1)   # [1 2 3 4 5 6 7]

    # print the stack
    print(a)

    # call serial search method and display its return.
    print(target, 'found at node position', binarysearch(a, first, target))

def testSerialSearch():
    # create an empty stack
    a = stack()
    # initialize first
    first = 6
    # initialize size
    size = 2
    # initialize target
    target = 70

    # push -7 onto the top of the stack
    a.push(-7)
    # push 42 onto the top of the stack
    a.push(42)
    # push 70 onto the top of the stack
    a.push(70)
    # push 39 onto the top of the stack
    a.push(39)
    # push 3 onto the top of the stack
    a.push(3)
    # push 63 onto the top of the stack
    a.push(63)
    # push 8 onto the top of the stack
    a.push(8)   # [8 63 3 39 70 42 -7]

    # print the stack
    print(a)

    # call serial search method and display its return.
    print(target, 'found at node position', serialsearch(a, first, size, target))

def assignment():
    print("Assignment")

    # Question 1
    head = node('2', None)    
    head = node('=', head)             
    head = node('1', head)             
    head = node('+', head) 
    head = node('1', head) 
        
    # Question 2
    operator = head
        
    # Question 3
    operator = operator.getLink()
        
    # Queston 4
    result = head
        
    # Question 5
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
    result = result.getLink()
        
    # Question 6
    operator.setData('-')
    result.setData('0')
        
    # Question 7
    operator.setData('*')
    result.setData('1')
        
    # Question 8
    operator.setData('/')
        
    # Question 9
    head.setData('7')
    result.setData('7')
        
    # Question 10
    operator = operator.getLink()
        
    # Question 11
    head.removeNodeAfter()
    operator.removeNodeAfter()
        
    # Question 12
    print("Head contains", node.listLength(head), ('Node' if (node.listLength(head) == 1) else 'Nodes'))
    print("Operator contains", node.listLength(operator), ('Node' if (node.listLength(operator) == 1) else 'Nodes'))
    print("Result contains", node.listLength(result), ('Node' if (node.listLength(result) == 1) else 'Nodes'))
    
    # Question 13
    if (node.listSearch(head, '1') != None):
        print("Head contains character", node.listSearch(head, '1').getData())
    if (node.listSearch(operator, '1') != None):
        print("Operator contains character", node.listSearch(operator, '1').getData())
    if (node.listSearch(result, '1') != None):
        print("Result contains character", node.listSearch(result, '1').getData())
    else:
        print("Result doesn't contain character 1")
        
    # Question 14
    copy = node.listCopyWithTail(head)
        
    # Question 15
    print("Copy[0] contains", node.listLength(copy[0]), ('Node' if (node.listLength(copy[0]) == 1) else 'Nodes'))
    print("Copy[1] contains", node.listLength(copy[1]), ('Node' if (node.listLength(copy[1]) == 1) else 'Nodes'))
        
    # Question 16
    if node.listSearch(copy[0], '1') != None:
        print("Copy[0] contains character", node.listSearch(copy[0], '1').getData())
    if node.listSearch(copy[1], '1') != None:
        print("Copy[1] contains character", node.listSearch(copy[0], '1').getData())
    else:
        print("Copy[1] doesn't contain character 1")

def module6PracticeAssignment():
    print("Testing Module 6 Practice Assignment")

    # Question 1
    head = node('T', None)
    head = node('K', head)
    head = node('N', head)
    head = node('I', head)
    head = node('L', head)

    # Question 2
    selection = head

    # Question 3
    selection = selection.getLink()
    selection = selection.getLink()
    selection = selection.getLink()

    # Question 4
    selection.addNodeAfter('E')

    # Question 5
    selection = selection.getLink()

    # Question 6
    selection.addNodeAfter('D')

    # Question 7
    selection = selection.getLink()

    # Question 8
    selection.addNodeAfter('L')

    # Question 9
    selection = selection.getLink()

    # Question 10
    selection.addNodeAfter('I')

    # Question 11
    selection = selection.getLink()

    # Question 12
    selection.addNodeAfter('S')

    # Question 13
    print("How many nodes does head contain?", node.listLength(head))
    print("How many nodes does selection contain?", node.listLength(selection))

    # Question 14
    tail = selection

    # Question 15
    tail = tail.getLink()
    tail = tail.getLink()

    # Question 16
    print("How many nodes does tail contain?", node.listLength(tail))

    # Question 17
    selection.removeNodeAfter()
    selection.removeNodeAfter()

    # Question 18
    print("How many nodes does head contain?", node.listLength(head))
    print("How many nodes does selection contain?", node.listLength(selection))
    print("How many nodes does tail contain?", node.listLength(tail))

    # Question 19
    head.removeNodeAfter()
    head.removeNodeAfter()

    # Question 20
    tail = tail.getLink()

    # Question 21
    print("How many nodes does head contain?", node.listLength(head))
    print("How many nodes does selection contain?", node.listLength(selection))
    print("How many nodes does tail contain?", node.listLength(tail))

    # Question 22
    print("Head contains the letter", node.listSearch(head, 'K').getData())
    print("Selection contains the letter", node.listSearch(selection, 'I').getData())

    # Question 23
    copy = node.listCopyWithTail(head)
    print("Copy[0] contains", node.listLength(copy[0]), "nodes")
    print("Copy[1] contains", node.listLength(copy[1]), "node")

    # Question 24
    print("First node in copy[0] contains the letter", copy[0].getData())
    print("First node in copy[1] contains the letter", copy[1].getData())

    # Question 25
    i = 1
    while (i <= 10):
        if node.listPosition(head, i) != None:
            print("Head contains position", i)
        else:
            print("Head doesn't contain position", i)
        i += 1

def testPush():
    print("Testing Push Function")

    s = stack()
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    s.push('S')
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    s.push('B')
    # s.push(1)
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    s.push('O')
    # s.push((1,2))
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    s.push('J')
    # s.push([1,2,3])
    print("Stack size is:", s.size())
    print("Stack contains:", s)

def testPeek():
    print("Testing Peek Function")

    s = stack()
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    s.push('S')
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Top element in stack is:", s.peek())
    s.push('B')
    # s.push(1)
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Top element in stack is:", s.peek())
    s.push('O')
    # s.push((1,2))
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Top element in stack is:", s.peek())
    s.push('J')
    # s.push([1,2,3])
    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Top element in stack is:", s.peek())

def testPop():
    print("Testing Pop Function")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Just popped:", s.pop())

    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Just popped:", s.pop())

    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Just popped:", s.pop())

    print("Stack size is:", s.size())
    print("Stack contains:", s)
    print("Just popped:", s.pop())

def testIsEmpty():
    print("Testing Is Empty Function")

    s = stack()
    s.push('S')
    s.push('B')
    s.push('O')
    s.push('J')

    print("Stack size is:", s.size())
    print("Stack contains:", s)

    while(not s.isEmpty()):
        print("Just popped:", s.pop())

    print("Stack size is:", s.size())
    print("Stack contains:", s)

def testEquals():
    print("Testing Equals Function")

    first = linkedlist()
    first.addMany('S', 'U', 'E')
    print("First contains:", first)

    last = linkedlist()
    last.addMany('C', 'E', 'K', 'L', 'O', 'S', 'K', 'Y')
    print("Last contains:", last)
    print("First is equal to last ?", first.__eq__(last)) # False

    sue = first
    print("First is equal to sue ?", first.__eq__(sue)) # True

    ceklosky = linkedlist()
    ceklosky.addMany('C', 'E', 'K', 'L', 'O', 'S', 'K', 'Y')
    print("Ceklosky is equal to last ?", ceklosky.__eq__(last)) # False

    name = 'Sue'
    print("Sue is equal to name ?", sue.__eq__(name)) # False

    name = None
    print("Sue is equal to name ?", sue.__eq__(name)) # False

def testRemove():
    print("Testing Remove Function")

    first = linkedlist()
    first.addMany('S', 'U', 'E')
    print("First contains:", first)

    first.remove('E')
    print("First head contains ", first.getHead())
    print("First tail contains ", first.getTail())

def testAddAll():
    print("Testing Add All Function")

    first = linkedlist()
    first.addMany('S', 'U', 'E')
    print("First contains:", first)

    last = linkedlist()
    last.addMany('C', 'E', 'K', 'L', 'O', 'S', 'K', 'Y')
    print("Last contains:", last)

    first.addAll(last)
    print("First contains:", first)
    print("First size is:", first.size())

def testAddMany():
    print("Testing Add Many Function")

    l = linkedlist()
    print("List size is:", l.size())
    print("List contains:", l)

    l.addMany('J', 'O', 'B', 'S')
    print("List size is:", l.size())
    print("List contains:", l)

def testAdd():
    print("Testing Add Function")

    l = linkedlist()
    print("List size is:", l.size())
    print("List contains:", l)
    l.add('J')
    print("List size is:", l.size())
    print("List contains:", l)
    l.add('O')
    # l.add(1)
    print("List size is:", l.size())
    print("List contains:", l)
    l.add('B')
    # l.add((1,2))
    print("List size is:", l.size())
    print("List contains:", l)

def testListPart():
    print("Testing List Part Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to start
    start = node('S', None)

    # create a new node with data equal to B and link equal to start
    # assign its reference to start
    start = node('B', start)

    # create a new node with data equal to O and link equal to start
    # assign its reference to start
    start = node('O', start)

    # create a new node with data equal to J and link equal to start
    # assign its reference to start
    start = node('J', start)

    # create a new node with data equal to S and link equal to None
    # assign its reference to end
    end = node('S', None)

    # create a new node with data equal to B and link equal to end
    # assign its reference to end
    end = node('B', end)

    copy = node.listPart(start, end)
    
    print("Copy head contains", node.listPosition(copy[0], 1).getData(), 
          node.listPosition(copy[0], 2).getData(),
          node.listPosition(copy[0], 3).getData())
    
    print("Copy tail contains", node.listPosition(copy[1], 1).getData())

def testListPosition():
    print("Testing List Position Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to head
    head = node('S', None)

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)

    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head)

    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head)

    print("First node contains data : ", node.listPosition(head, 1).getData())
    print("Second node contains data : ", node.listPosition(head, 2).getData())
    print("Third node contains data : ", node.listPosition(head, 3).getData())
    print("Four node contains data : ", node.listPosition(head, 4).getData())

    if (node.listPosition(head, 5) != None):
        print("Fifth node contains", node.listPosition(head, 5).getData())
    else:
        print("There is no fifth node")

    # print("First node contains data : ", node.listPosition(head, -1).getData())

def testListCopy():
    print("Testing List Copy Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to head
    head = node('S', None)

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)

    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head)

    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head)

    copy = node.listCopy(head)

    print("Head contains", node.listPosition(head, 1).getData(), 
          node.listPosition(head, 2).getData(),
          node.listPosition(head, 3).getData(),
          node.listPosition(head, 4).getData())
    
    print("Copy contains", node.listPosition(copy, 1).getData(), 
          node.listPosition(copy, 2).getData(),
          node.listPosition(copy, 3).getData(),
          node.listPosition(copy, 4).getData())

def testListCopyWithTail():
    print("Testing List Copy With Tail Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to head
    head = node('S', None)

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)

    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head)

    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head)

    copy = node.listCopyWithTail(head)

    print("Head contains", node.listPosition(head, 1).getData(), 
          node.listPosition(head, 2).getData(),
          node.listPosition(head, 3).getData(),
          node.listPosition(head, 4).getData())
    
    print("Copy head contains", node.listPosition(copy[0], 1).getData(), 
          node.listPosition(copy[0], 2).getData(),
          node.listPosition(copy[0], 3).getData(),
          node.listPosition(copy[0], 4).getData())
    
    print("Copy tail contains", node.listPosition(copy[1], 1).getData())
    
def testListSearch():
    print("Testing List Search Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to head
    head = node('S', None)

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)

    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head)

    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head)

    print("Head contains", node.listSearch(head, 'J').getData())
    print("Head contains", node.listSearch(head, 'O').getData())
    print("Head contains", node.listSearch(head, 'B').getData())
    print("Head contains", node.listSearch(head, 'S').getData())

    if (node.listSearch(head, 'J') != None):
        print("Head contains", node.listSearch(head, 'J').getData())
    else:
        print("Head doesn't contain J")

    if (node.listSearch(head, 'Z') != None):
        print("Head contains", node.listSearch(head, 'Z').getData())
    else:
        print("Head doesn't contain Z")

def testListLength():
    print("Testing List Length Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to head
    head = node('S', None)

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)

    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head)

    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head)

    print("Length of head is : ", node.listLength(head))

def review():
    print("Practice!")

    # Question 1
    head = node('X', None)  
    head = node('X', head)             
    head = node('X', head)             
    head = node('X', head) 

    # Question 2
    selection1 = head
        
    # Question 3
    selection1.addNodeAfter('O')
        
    # Queston 4
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()
        
    # Question 5
    selection1.addNodeAfter('O')
        
    # Question 6
    selection1 = selection1.getLink()
    selection1 = selection1.getLink()
        
    # Question 7
    selection1.addNodeAfter('O')
        
    # Question 8
    tail = head
        
    # Question 9
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()
        
    # Question 10
    selection2 = head
        
    # Question 11
    selection2 = selection2.getLink()
    selection2 = selection2.getLink()
        
    # Question 12
    head.setData('A')
    selection2.setData('A')
    selection1.setData('A')
    tail.setData('A')

    # Question 13
    head.removeNodeAfter()
    selection2.removeNodeAfter()
    selection1.removeNodeAfter()

def testRemoveNodeAfter():
    print("Testing Remove Node After Function")

    # create a new node with data equal to S and link equal to None
    # assign its reference to head
    head = node('S', None)

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)

    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head)

    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head)

    print("The head node contains the following data: ", head.getData()) # J

    # remove the node after the node head refers to (node that has data equal to O)
    head.removeNodeAfter()

    # get head's link and assign its reference to head
    head = head.getLink()

    print("The head node contains the following data: ", head.getData()) # B

    # remove the node after the node head refers to (node that has data equal to S)
    head.removeNodeAfter()

    print("The head node contains the following data: ", head.getData()) # B
    print("The head node contains the following link: ", head.getLink()) # None

    # this will generate an AttributeError
    # head.removeNodeAfter()

def testAddNodeAfter():
    print("Testing Add Node After Function")

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('J', None)  
    print("The head node contains the following data: ", head.getData()) # J

    # declare a new node named selection and make it refer to the same 
    # as head
    selection = head  

    print("The head node contains the following data: ", head.getData()) # J
    print("The selection node contains the following data: ", selection.getData()) # J

    # add a node with data equal to O after the node selection refers
    # to
    selection.addNodeAfter('O')

    # get selection's link and assign its reference to selection
    selection = selection.getLink()

    print("The head node contains the following data: ", head.getData()) # J
    print("The selection node contains the following data: ", selection.getData()) # O

    # add a node with data equal to B after the node selection refers
    # to
    selection.addNodeAfter('B')

    # get selection's link and assign its reference to selection
    selection = selection.getLink()

    print("The head node contains the following data: ", head.getData()) # J
    print("The selection node contains the following data: ", selection.getData()) # B

    # add a node with data equal to S after the node selection refers
    # to
    selection.addNodeAfter('S')

    # get selection's link and assign its reference to selection
    selection = selection.getLink()

    print("The head node contains the following data: ", head.getData()) # J
    print("The selection node contains the following data: ", selection.getData()) # S

    # declare a new node named tail and make it refer to the same 
    # as head
    tail = head

    # get tail's link and assign its reference to tail       
    tail = tail.getLink()
    tail = tail.getLink()
    tail = tail.getLink()

    # add a node with data equal to Z after the node tail refers
    # to
    tail.addNodeAfter('Z')

    # get tail's link and assign its reference to tail
    tail = tail.getLink()

    print("The head node contains the following data: ", head.getData()) # J
    print("The selection node contains the following data: ", selection.getData()) # S
    print("The tail node contains the following data: ", tail.getData()) # Z

def testGettersAndSetters():
    print("Testing Getters And Setters")

    # create a new node with data equal to R and a null link
    # assign its reference to head
    head = node('R', None)  # R
    print("The head node contains the following data: ", head.getData()) # R
        
    head.setData('S')   # S
    print("The head node contains the following data: ", head.getData()) # S

    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head)  # B -> S
    print("The head node contains the following data: ", head.getData()) # B

    head = node('O', head) # O -> B -> S
    print("The head node contains the following data: ", head.getData()) # O

    head = node('J', head)  # J -> O -> B -> S
    print("The head node contains the following data: ", head.getData()) # J
        
    # get head's link and assign its reference to head
    head = head.getLink()   # O -> B -> S
    print("The head node contains the following data: ", head.getData()) # O
        
    # get head's link and assign its reference to head
    head = head.getLink()   # B -> S
    print("The head node contains the following data: ", head.getData()) # B
        
    head = head.getLink();  # S
    print("The head node contains the following data: ", head.getData()) # S
        
    """ head = head.getLink();
    # this will generate an AttributeError 
    print("The head node contains the following data: ", head.getData()) """
    
    print("The head node contains the following link: ", head.getLink()) # None
        
    # set head's link to a new node
    head.setLink(node('O', None));

def testConstructor():
    print("Testing Constructor")

    # create a new node with data equal to S and a null link
    # assign its reference to head
    head = node('S', None) # S
        
    # create a new node with data equal to B and link equal to head
    # assign its reference to head
    head = node('B', head) # B -> S
        
    # create a new node with data equal to O and link equal to head
    # assign its reference to head
    head = node('O', head) # O -> B -> S
        
    # create a new node with data equal to J and link equal to head
    # assign its reference to head
    head = node('J', head) # J -> O -> B -> S

    generic = node(1, None)                 # 1
    generic = node(1.5, generic)            # 1.5 -> 1
    generic = node([1,2], generic)          # [1,2] -> 1.5 -> 1      
    generic = node(('A', 'B'), generic)     # ('A', 'B') -> [1,2] -> 1.5 -> 1

if __name__ == "__main__":
    main()