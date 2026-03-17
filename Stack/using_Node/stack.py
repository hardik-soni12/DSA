from node import Node

class Stack:
    def __init__(self):
        self.__top = None
        self.__n = 0

    
    # size and printing

    def size(self):
        '''
        returns the size of the stack
        '''

        return self.__n
    
    def __str__(self) :
        curr = self.__top
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        return ' '.join(res)
    

    # peek and isEmpty 
    
    def isEmpty(self):
        '''returns true if stack is empty else False'''
        if self.__top:
            return False
        return True

    def peek(self):
        '''Returns the top item in the stack'''
        if self.isEmpty():
            return 'stack is empty'

        return self.__top.data
    

# insertion

    def push(self, value):
        '''insert value from the top, returns None'''

        new_node = Node(value)
        if self.isEmpty():
            self.__top = new_node
        
        else:
            new_node.next = self.__top
            self.__top = new_node
        self.__n += 1


    # deletion

    def pop(self):
        '''remove the item from the top, returns the removed item'''
        if self.isEmpty():
            raise IndexError('pop on empty stack')
        
        removed_item = self.__top.data
        self.__top = self.__top.next
        self.__n -= 1
        return removed_item
