class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None
    
    def __eq__(self, other):
        return isinstance(other, Node) and\
        self.item == other.item
    
    def __lt__(self, other):
        if Node != type(other):
            raise ValueError
           
        return isinstance(other, Node) and\
        self.item < other.item

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = None

    def is_empty(self):
        '''Returns True if OrderedList is empty
            MUST have O(1) performance'''
        if self.head == None:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''
        current = self.head
        compare = Node(item)
        if self.is_empty():
            self.head = compare
            return True
        
        while current != None:
            if compare < current:
                compare.next = currrent
                compare.prev = current.prev
                current.prev.next = compare
                current.prev = compare
                return True
        
            if current == compare:
                return False
            
            if current.next == None:
                current.next = compare
                compare.prev = current
                return True

            current = current.next

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was in the list) 
          returns True.  If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        if self.is_empty():
            raise IndexError
        current = self.head
        
        if self.size() == 1:
            if current.item == item:
                self.head = None
                return True
            return False
        
        while current != None:     
            if current.item == item:
                if current.prev == None:
                    current.next.prev = current.prev
                    self.head = current.next
                    return True
                
                if current.next == None: 
                    current.prev.next = None
                    current = None
                    return True
                
                else:
                    current.next.prev = current.prev        
                    current.prev.next = current.next
                    return True
            current = current.next
        return False
  
    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        index = 0
        if self.is_empty():
            raise IndexError
        
        current = self.head
        while current != None:
            if current.item == item:
                return index
            
            if current.next == None:
                return None
            
            index += 1
            current = current.next

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index > self.size():
            raise IndexError
        
        if self.is_empty():
            raise IndexError
        
        current = self.head
        i = 0
        
        while i < index:
            current = current.next
            i += 1
        item = current.item
        self.remove(item)
        return item

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        
        if self.is_empty():
            raise IndexError
        
        current = self.head
        if self.head.item == item:
            return True
        
        if self.head.next == None:
            return False
        
        self.head = self.head.next
        recur = self.search(item)
        self.head = current
        return recur

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        orderlist = []
        current = self.head
        if self.is_empty():
            return orderlist     
        
        while current != None:
            orderlist.append(current.item)
            if current.next == None:
                return orderlist
            current = current.next

    
    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        reverse = []
        current = self.head
        
        if self.is_empty():
            return []
        
        if self.head.next == None:
            return [self.head.item]
        
        reverse.append(self.head.item)
        self.head = self.head.next
        recur = self.python_list_reversed() + reverse
        self.head = current
        return recur

    
    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        if self.is_empty():
            return 0
        
        count = 0
        current = self.head
        if self.head.next == None:
            count += 1
            return count
        
        count += 1
        self.head = self.head.next
        recur = self.size() + count
        self.head = current
        return recur
