class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.array = [None]*size
        self._front = self.__rear = -1
    

    def isEmpty(self):
        '''returns True if queue is Empty'''
        return self._front == -1
    
    def isFull(self):
        '''returns True if queue is full'''
        return (self.__rear + 1) % self.size == self._front
    
    
    

c = CircularQueue(5)

print(c.isFull())
