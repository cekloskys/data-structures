from node.node import *

class queue:
    """Queue class that uses nodes as its underlying data structure.
    """    
    def __init__(self):
        """Constructs an empty queue.
        """        
        self.__head = None
        self.__tail = self.__head
        self.__manyNodes = 0

    def size(self):
        """Returns the number of nodes in the calling queue.

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getHead(self):
        """Returns a reference to the head of the calling queue.

        Returns:
            linkedlist: reference to the head of the calling queue
        """        
        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail of the calling queue.

        Returns:
            linkedlist: reference to the tail of the calling queue
        """ 
        return self.__tail
    
    def size(self):
        """Returns the number of nodes in this queue.

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getData(self):
        """Returns the data values in the calling queue.

        Returns:
            str: data values in the calling queue
        """        
        cursor = self.__head    # used to step through head 
        data = ""               # string representation of data values in the calling queue
        i = 1                   # used to count nodes

        # loop through calling queue, get data value in each node and concatenate it to data
        while (i <= self.__manyNodes):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i = i + 1

        # return data values
        return data
    
    def __str__(self):
        """Returns string representation of the calling queue.

        Returns:
            str: string representation of the calling queue
        """
        return f"[ {self.getData()}]"
    
    def enqueue(self, element):
        """Add a specified element to the rear of the calling queue.

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
            # add the node to tail if head is not None
            self.__tail.addNodeAfter(element)
            # advance to next node in tail
            self.__tail = self.__tail.getLink()

        # get the number of nodes in the calling linkedlist
        self.__manyNodes = node.listLength(self.__head)

    def dequeue(self):
        """Return and remove an element from the front of the calling queue.

        Raises:
            ValueError: indicates calling queue is empty

        Returns:
            _type_: data in element from the front of the calling queue
        """        
        try:  
            # if the calling queue is empty raise error          
            if (self.isEmpty()):
                raise ValueError("Queue is empty.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # get data in node at position 1 of the calling queue
            top = node.listPosition(self.__head, 1).getData()

            # advance head to the next node
            self.__head = self.__head.getLink()

            # get the number of nodes in the calling queue
            self.__manyNodes = node.listLength(self.__head)

            return top
    
    def peek(self):
        """Returns the element at the top of the calling queue, but does not remove it.

        Raises:
            ValueError: indicates calling queue is empty

        Returns:
            _type_: element from the front of the calling queue
        """        
        try:  
            # if the calling queue is empty raise error          
            if (self.isEmpty()):
                raise ValueError("Queue is empty.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            return node.listPosition(self.__head, 1).getData()
    
    def isEmpty(self):
        """Checks if the calling queue is empty.

        Returns:
            Boolean: True if the calling queue is empty, else False.
        """      
        return self.size() == 0