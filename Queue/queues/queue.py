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
    

    # printing/Iteration

    def __str__(self):
        curr = self.__front
        res = []
        while curr:
            res.append(str(curr.data))
            curr += 1

        return '[ '+' ] <- '.join(res)+' ]'
    

    def __iter__(self):
        curr = self.__front
        while curr:
            yield curr.data
            curr = curr.next


    def peek(self):
        '''returns the first item from the queue'''
        if self.__front:
            return self.__front.data
        return 'empty queue'
    
    