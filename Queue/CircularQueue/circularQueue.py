class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.__queue = [None]*size
        self.__front = self.__rear = -1
    

    def isEmpty(self):
        '''returns True if queue is Empty'''
        return self.__front == -1
    
    def isFull(self):
        '''returns True if queue is full'''
        return (self.__rear + 1) % self.size == self.__front
    
    def __str__(self) -> str:
        res = [item for item in self.__queue if item is not None]
        return str(res)
    

    # insertion
    def enqueue(self, value):
        '''inserts data , returns None'''
        if self.isFull():
            return 'Queue is full'
        
        if self.isEmpty():
            self.__front = 0
        
        self.__rear = (self.__rear + 1) % self.size
        self.__queue[self.__rear] = value

    
    

c = CircularQueue(5)

c.enqueue(10)
c.enqueue(20)
c.enqueue(30)
c.enqueue(40)
c.enqueue(50)
print(c.isEmpty())
print(c.isFull())
print(c)
