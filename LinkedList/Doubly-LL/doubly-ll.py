from node import Node

class DoublyLinkedList:
    def __init__(self):
        self.__head = self.__tail = None
        self.__n = 0

    def __len__(self):
        return self.__n 
    

    # printing

    def __str__(self) :
        curr = self.__head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next

        return ' <-> '.join(res)
    

    # insertion methods

    def append(self, value):
        '''
        inserts data from the end of the LL, returns None
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            self.__tail.next = new_node
            new_node.prev = self.__tail
            self.__tail = new_node
        self.__n += 1
    

    def insert_head(self, value):
        '''
        inserts item from the start, returns None
        '''

        new_node = Node(value)

        if self.__head is None:
            self.__head = self.__tail = new_node

        else:
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        
        self.__n += 1
            
    
    def insertAfter(self, item, value):
        '''
        insert value after the present item in LL ,
        f the item isn't present in the linked list inserted value will automatically 
        gets insert at the end , returns None
        '''

        new_node = Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        
        else:
            curr = self.__head
            while curr != None and curr.data != item:
                curr = curr.next

            if curr is None:
                new_node.prev = self.__tail
                self.__tail.next = new_node
                self.__tail = new_node
            else:
                if curr.data == item:
                    new_node.prev = curr
                    new_node.next = curr.next
                    if curr.next != None:
                        curr.next.prev = new_node
                    curr.next = new_node
                
        self.__n += 1


    # deletion methods
    def pop(self, item=None):
        '''
        Removes the specified item if present else the last item if no argument is given.
        Returns the data of the removed node.
        '''

        if self.__head is None:
            raise IndexError('pop on empty linked list')
        
        # if item is None remove last element
        curr = self.__head
        if item is None:
            while curr.next != None:
                curr = curr.next
        
        else:
            # if item is given serach for it
            while curr != None and curr.data != item:
                curr = curr.next

            if curr is None:
                raise ValueError('item not found')
            
        removed_data = curr.data
        if curr == self.__head:
            self.__head = curr.next
            if self.__head:
                self.__head.prev = None

        
        else:
            curr.prev.next = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        
        if curr == self.__tail:
            self.__tail = curr.prev
            
        self.__n -= 1
        return removed_data
    

    
    def delete_head(self):
        '''
        removes the head node of a Linked list and returns the removed item
        '''

        if self.__head is None:
            raise IndexError('delete head on empty linked list')
        
        removed_item = self.__head.data
        self.__head = self.__head.next
        if self.__head:
            self.__head.prev = None
        self.__n -= 1
        return removed_item




d = DoublyLinkedList()
d.append(10)
d.append(11)
d.append(12)
d.insert_head(5)
d.append(13)
d.insertAfter(5,6)
print((d))
d.pop()
d.delete_head()

print((d))
