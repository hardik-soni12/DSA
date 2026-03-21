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
    
    def __str__(self) -> str:
        res = [item for item in self.array if item is not None]
        return str(res)
    
    
    
    

c = CircularQueue(5)

print(c.isFull())
print(c)
