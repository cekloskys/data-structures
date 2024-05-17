from node.node import *

class stack:
    """Stack class that uses nodes as its underlying data structure.
    """
    def __init__(self):
        """Constructs an empty stack.
        """        
        self.__head = None
        self.__tail = self.__head
        self.__manyNodes = 0

    def size(self):
        """Returns the number of nodes in the calling stack.

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getHead(self):
        """Returns a reference to the head of the calling stack.

        Returns:
            stack: reference to the head of the calling stack
        """        
        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail of the calling stack.

        Returns:
            stack: reference to the tail of the calling stack
        """ 
        return self.__tail
    
    def size(self):
        """Returns the number of nodes in the calling stack.

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getData(self):
        """Returns the data values in the calling stack.

        Returns:
            str: data values in the calling stack
        """        
        cursor = self.__head    # used to step through head 
        data = ""               # string representation of data values in the calling stack
        i = 1                   # used to count nodes

        # loop through calling stack, get data value in each node and concatenate it to data
        while (i <= self.__manyNodes):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i = i + 1

        # return data values
        return data
    
    def __str__(self):
        """Returns string representation of the calling stack.

        Returns:
            str: string representation of the calling stack
        """
        return f"[ {self.getData()}]"
    
    def push(self, element):
        """Adds the specified element to the top of the calling stack.

        Args:
            element (_type_): specified element
        """        
        # if head is None    
        if (self.__head == None):
            # add node to head
            self.__head = node(element, None)
            # make tail refer to the same node as head
            self.__tail = self.__head
        else:
            # add node to head of head
            self.__head = node(element, self.__head)

        # get the number of nodes in the calling linkedlist
        self.__manyNodes = node.listLength(self.__head)

    def peek(self):
        """Returns the element at the top of the calling stack, but does not remove it.

        Raises:
            ValueError: indicates calling stack is empty

        Returns:
            _type_: element at the top of the calling stack
        """        
        try:  
            # if the calling stack is empty raise error         
            if (self.isEmpty()):
                raise ValueError("Stack is empty.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:  
            # return data in node at position 1 of the calling stack   
            # return node.listPosition(self.__head, 1).getData()
            return self.__head.getData()
    
    def pop(self):
        """Returns and removes the element at the top of the calling stack.

        Raises:
            ValueError: indicates calling stack is empty

        Returns:
            _type_: element at the top of the calling stack
        """
        try:  
            # if the calling stack is empty raise error          
            if (self.isEmpty()):
                raise ValueError("Stack is empty.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # get data in node at position 1 of the calling stack
            # top = node.listPosition(self.__head, 1).getData()
            top = self.__head.getData()

            # advance head to the next node
            self.__head = self.__head.getLink()

            # get the number of nodes in the calling stack
            self.__manyNodes = node.listLength(self.__head)

            # return data in node at position 1 of the calling stack 
            return top
    
    def isEmpty(self):
        """Checks if the calling stack is empty.

        Returns:
            Boolean: True if the calling stack is empty, else False.
        """        
        return self.size() == 0