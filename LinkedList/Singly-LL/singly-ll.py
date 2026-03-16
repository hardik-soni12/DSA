from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__n = 0

    def __len__(self):
        return self.__n
    
    # Insertion methods
    def insert_head(self, value):
        '''
        inserts data from the head, returns None
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            
        else:
            new_node.next = self.__head
            self.__head = new_node
        
        self.__n += 1  

    
    def append(self, value):
        '''
        insert value from the end , returns None
        '''

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node

        else:
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            
            curr.next = new_node

        self.__n += 1

    

    def insert_after(self, item, value):
        '''
        insert data after the item given, returns None
        '''
        new_node = Node(value)
        curr = self.__head
        while curr is not None and curr.data != item:
            curr = curr.next

        if curr != None:
            new_node.next = curr.next
            curr.next = new_node
            self.__n += 1
        else:
            raise ValueError('Item not found!')
        

    # deletion methods

    def clear(self):
        ''' clear all the data from the Linked List,
        returns None'''
        self.__head = None
        self.__n = 0

    
    def delete_head(self):
        '''
        removes item from the head, returns the removed item.
        '''
        if self.__head is None:
            raise IndexError('Remove head on empty linked List')
        
        removed_item = self.__head.data
        self.__head = self.__head.next
        self.__n -= 1
        return removed_item
    

    def pop(self):
        '''removes item from the end and returns the remove item'''
        if self.__head is None:
            raise IndexError('Pop on empty linked list')
        
        if self.__head.next is None:
            removed_item = self.__head
            self.__head = None
        else:
            curr = self.__head
            while curr.next.next != None:
                curr = curr.next

            removed_item = curr.next.data
            curr.next = None
        
        self.__n -= 1
        return removed_item
    

    def remove(self, item):
        '''
        removes the item given if present in linked list
        '''
        
        if self.__head is None:
            raise IndexError('remove on empty linked list')
        
        if self.__head.data == item:
            self.__head = self.__head.next
        
        else:
            curr = self.__head
            while curr.next != None:
                if curr.next.data == item:
                    break
                curr = curr.next

            if curr.next is None:
                raise ValueError('item not found')
            else:
                curr.next = curr.next.next

        self.__n -= 1




    # printing
    def __str__(self) -> str:
        curr = self.__head
        res= []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        
        return ' -> '.join(res)

l = LinkedList()
l.insert_head(10)
l.insert_head(20)
l.append(5)
l.append(0)
l.insert_after(20, 15)
print(l)

print((l))