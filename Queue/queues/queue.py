from node import Node

class Queue:
    def __init__(self):
        self.__front = self.__rear = None
        self.__n = 0


    def __len__(self):
        return self.__n
    

    def isEmpty(self):
        '''returns True of queue is Empty else returns False'''

        if self.__front:
            return True
        return False
    

