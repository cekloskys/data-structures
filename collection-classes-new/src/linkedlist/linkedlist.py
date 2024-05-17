from node.node import *

class linkedlist:
    """The linkedlist class holds a collection of characters using a linked list of nodes.  
    It includes methods that allow the linkedlist to be manipulated and modified.
    """
    def __init__(self):
        """Constructs an empty linkedlist.
        """        
        self.__head = None
        self.__tail = self.__head
        self.__manyNodes = 0

    def size(self):
        """Returns the number of nodes in this linkedlist.

        Returns:
            int: number of nodes
        """        
        return self.__manyNodes
    
    def getHead(self):
        """Returns a reference to the head of the calling linkedlist.

        Returns:
            linkedlist: reference to the head of the calling linkedlist
        """        
        return self.__head
    
    def getTail(self):
        """Returns a reference to the tail of the calling linkedlist.

        Returns:
            linkedlist: reference to the tail of the calling linkedlist
        """ 
        return self.__tail
    
    def add(self, element):
        """Adds a node that contains the specified character to the 
        head of the calling linkedlist if the head is None, else it adds
        the node to the tail.

        Args:
            element (str): specified character
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

    def addMany(self, *args):
        """Adds a variable number of nodes that contain the specified characters to the 
        head of the calling linkedlist if the head is equal to None, else it adds
        them to the tail.
        """   
        # loop through all the specified characters and add them to the calling linkedlist
        # as nodes  
        for a in args:
            self.add(a)

    def addAll(self, addend):
        """Adds the contents of the specified linkedlist to the end of the calling linkedlist.

        Args:
            addend (linkedlist): specified linkedlist

        Raises:
            ValueError: indicates addend is None
        """        
        try:       
            # if addend is None, raise error   
            if (addend == None):
                raise ValueError("Addend may not be None.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # if addend has one or more nodes
            if(addend.size() > 0):
                # get a reference to the head and tail of a copy of addend
                copyInfo = node.listCopyWithTail(addend.getHead())
                # set tail's link to the head of the copy
                self.__tail.setLink(copyInfo[0])
                # make tail refer to the same node as the tail of the copy
                self.__tail = copyInfo[1]

                # get the number of nodes in the calling linkedlist
                self.__manyNodes = node.listLength(self.__head)

    def remove(self, target):
        """Removes a node containing the specified target from the calling linkedlist.

        Args:
            target (str): specified target

        Returns:
            Boolean: False if the specified target exists in the calling linkedlist,
            else True
        """   
        # get a reference to the node thats data matches the specified target
        # and assign the reference to targetNode     
        targetNode = node.listSearch(self.__head, target)

        # if targetNode is None, return False
        if (targetNode == None):
            return False
        else:
            # if a targetNode was found, get the data in the node head
            # refers to and set it in the node that targetNode refers to
            targetNode.setData(self.__head.getData())
            # advance to next node in head
            self.__head = self.__head.getLink()
            # get the number of nodes in the calling linkedlist
            self.__manyNodes = node.listLength(self.__head)
            # return True
            return True

    def getData(self):
        """Returns the data values in the calling linkedlist.

        Returns:
            str: data values in the calling linkedlist
        """        
        cursor = self.__head    # used to step through head 
        data = ""               # string representation of data values in the calling linkedlist
        i = 1                   # used to count nodes

        # loop through calling linkedlist, get data value in each node and concatenate it to data
        while (i <= self.__manyNodes):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i = i + 1

        # return data values
        return data
    
    def __str__(self):
        """Returns string representation of the calling linkedlist.

        Returns:
            str: string representation of the calling linkedlist
        """
        return f"[ {self.getData()}]"
    
    def __eq__(self, other):
        """Tests if the calling linkedlist is equal to the specified object.

        Args:
            other: the specified object

        Returns:
            Boolean: True if the calling linkedlist is equal to the specified
            object, else False
        """
        if other is not None:
            if isinstance(other, linkedlist):
                if other.__head == self.__head:
                    if other.__tail == self.__tail:
                        if other.__manyNodes == self.__manyNodes:
                            return True
        return False