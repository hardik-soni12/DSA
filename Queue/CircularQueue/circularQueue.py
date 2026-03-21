class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.array = [None]*size
        self._front = self.__rear = -1
    
    
