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