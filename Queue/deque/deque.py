from node import Node

class Deque:
    def __init__(self):
        self.__front = self.__rear = None
        self.__n = 0
    
    def __len__(self):
        return self.__n
    
    def isEmpty(self):
        '''returns True if queue is empty, else returns False'''
        if self.__front:
            return False
        return True
    
    
    # peek methods

    def PeekFront(self):
        '''returns the front item from the queue.'''

        if self.isEmpty():
            return 'Empty queue'
        
        return self.__front.data
    

    def PeekRear(self):
        '''Returns the Rear item from the queue'''

        if self.isEmpty():
            return 'Empty queue'
        
        return self.__rear.data
    

    