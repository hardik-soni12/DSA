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
        if not self.isEmpty():
            return 'stack is empty'

        return self.__top.data
    
    