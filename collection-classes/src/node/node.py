class node:
    """The node class holds a collection of values using nodes.  
    It includes methods that allow the nodes to be manipulated and modified.
    """    
    def __init__(self, data, link):
        """Constructs a node using specified data value and link.

        :ivar __data: data value for node
        :ivar __link: link for node

        Args:
            data (str): specified data value
            link (node): specified link
        """           
        self.__data = data
        self.__link = link   

    def getData(self):
        """Returns the data value stored in the calling node.

        Returns:
            str: data value stored in the calling node
        """        
        return self.__data 
    
    def setData(self, data):
        """Sets the data value stored in the calling node to the specified
        data value.

        Args:
            data (str): specified data value
        """        
        self.__data = data

    def setDataAtPosition(self, position: int, data):
        """Sets the data value stored in the calling node at the specified position 
        to the specified data value.

        Args:
            position (int): specified posotion
            data: specified data value

        Raises:
            ValueError: indicates position is less than one
        """        
        cursor = self   # used to step through calling node
        i = 1           # used to count nodes

        try:       
            # if position is less than one, raise error   
            if (position < 1):
                raise ValueError("Position may not be less than 1.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # move cursor forward the correct number nodes
            # keep looping as long as i is less than specified position 
            # and cursor isn't equal to None
            # if cursor becomes None that means specified position was greater than
            # number of nodes in specified node
            while ((i < position) and (cursor != None)):
                # move cursor to next node
                cursor = cursor.getLink()
                # increment counter
                i = i + 1

            # set data value in node cursor refers to
            cursor.setData(data)
        
    def getLink(self):
        """Returns the link stored in the calling node.

        Returns:
            node: link stored in the calling node
        """   
        return self.__link 
    
    def setLink(self, link):
        """Sets the link stored in the calling node to the specified
        link.

        Args:
            link (node): specified link
        """ 
        self.__link = link

    def addNodeAfter(self, element):
        """Adds a new node containing a specified element value
        at a selected position in the calling node.

        Args:
            element (str): specified element value
        """        
        self.__link = node(element, self.__link)

    def removeNodeAfter(self):
        """Removes a node from a selected position in the calling
        node.
        """        
        self.__link = self.__link.__link

    @staticmethod
    def listLength(head):
        """Computes the number of nodes in a specified node.

        Args:
            head (node): specified node

        Returns:
            int: number of nodes
        """        
        cursor = head   # used to step through specified node
        length = 0      # used to count nodes 

        # traverse nodes in specified node as long as cursor
        # isn't null
        while (cursor != None):
            # increment length
            length = length + 1
            # move cursor to next node
            cursor = cursor.getLink()

        # return length
        return length
    
    @staticmethod
    def listSearch(head, target):
        """Searches for a specified target value in a specified node.

        Args:
            head (node): specified node
            target (str): specified target value

        Returns:
            node: reference to node that contains specified target value
            if specified target value is found, else None
        """        
        cursor = head   # used to step through specified node

        # traverse nodes in specified node as long as cursor
        # isn't null
        while (cursor != None):
            # check if data value in cursor is equal to
            # specified target value
            if (target == cursor.getData()):
                # return cursor
                return cursor
            # move cursor to next node
            cursor = cursor.getLink()

        # if specified target value isn't found, return None
        return None
    
    @staticmethod
    def listPosition(head, position: int):
        """Searches for a node in a specified node based on
        a specified position.

        Args:
            head (node): specified node
            position (int): specified posotion

        Raises:
            ValueError: indicates position is less than one

        Returns:
            node: reference to node at specified position if specified 
            position is found, else null
        """        
        cursor = head   # used to step through specified node
        i = 1           # used to count nodes

        try:       
            # if position is less than or equal to zero, raise error   
            if (position < 1):
                raise ValueError("Position may not be less than 1.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:
            # move cursor forward the correct number nodes
            # keep looping as long as i is less than specified position 
            # and cursor isn't equal to None
            # if cursor becomes None that means specified position was greater than
            # number of nodes in specified node
            while ((i < position) and (cursor != None)):
                # move cursor to next node
                cursor = cursor.getLink()
                # increment counter
                i = i + 1

            # return cursor
            return cursor
        
    @staticmethod
    def listCopy(source):
        """Makes a copy of a specified node.

        Args:
            source (node): specified node

        Returns:
            node: reference to head of copy
        """   
        # if specified node is None, return None     
        if (source is None):
            return None
        
        # make copy head refer to a node that contains the same
        # data value a specified node's head
        copyHead = node(source.getData(), None)
        # make copy tail refer to the same node as copy head
        copyTail = copyHead

        # keep looping through specified node until
        # reach node that has null link - last node
        while (source.getLink() != None):
            # advance to next node in specified node
            source = source.getLink()
            # get data value in node and add it to the end of copy tail
            copyTail.addNodeAfter(source.getData())
            # advance to next node in copy tail
            copyTail = copyTail.getLink()

        # return reference to copy head
        return copyHead
    
    @staticmethod
    def listCopyWithTail(source):
        """Makes a copy of a specified node.

        Args:
            source (node): specified node

        Returns:
            [node]: reference to head and tail of copy
        """
        # if specified node is None, return None
        if (source is None):
            return None
        
        # make copy head refer to a node that contains the same
        # data value as specified node's head
        copyHead = node(source.getData(), None)
        # make copy tail refer to the same node as copy head
        copyTail = copyHead

        # keep looping through specified node until
        # reach node that has null link - last node
        while (source.getLink() != None):
            # advance to next node in specified node
            source = source.getLink()
            # get data value in node and add it to the end of copy tail
            copyTail.addNodeAfter(source.getData())
            # advance to next node in copy tail
            copyTail = copyTail.getLink()

        # store reference to copy head and tail in list
        answer = [copyHead, copyTail]
        # return reference to copy head and tail
        return answer
    
    @staticmethod
    def listPart(start, end):
        """Makes a copy of node starting at a specified node
        and ending at a specified node.

        Args:
            start (node): specified starting node
            end (node): specified ending node

        Raises:
            ValueError: indicates start in None
            ValueError: indicates end in None
            ValueError: indicates end not found in start

        Returns:
            [node]: reference to head and tail of copy
        """        
        try:    
            # if start or end is None, raise error       
            if (start == None):
                raise ValueError("Start is none.")
            elif (end == None):
                raise ValueError("End is none.")
        except ValueError as e:
            # display error and exit
            exit(e)
        else:   
            # make copy head refer to a node that contains the same
            # data value as start's head 
            copyHead = node(start.getData(), None)
            # make copy tail refer to the same node as copy head
            copyTail = copyHead

            # keep looping through specified node as long as
            # start's data value isn't equal to end's data value
            while (start.getData() != end.getData()):
                # advance to next node in start
                start = start.getLink()
                try:    
                    # if start is None, raise error       
                    if (start == None):
                        raise ValueError("End not found in start.")
                except ValueError as e:
                    # display error and exit
                    exit(e)
                else:
                    # get data value in node and add it to the end of copy tail
                    copyTail.addNodeAfter(start.getData())
                    # advance to next node in copy tail
                    copyTail = copyTail.getLink()

            # store reference to copy head and tail in list
            answer = [copyHead, copyTail]
            # return reference to copy head and tail
            return answer
        
    def __str__(self):
        cursor = self
        data = ""
        i = 1

        while (i <= node.listLength(self)):
            data = data + (str(cursor.getData()) + ' ')
            cursor = cursor.getLink()
            i = i + 1

        return data