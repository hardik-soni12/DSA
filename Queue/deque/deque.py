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
    


    # printing / iteration method

    def __str__(self) -> str:
        curr = self.__front
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next

        return '[ '+' ] <-> [ '.join(res)+' ]'
    

    def __iter__(self):
        curr = self.__front
        while curr:
            yield curr.data
            curr = curr.next

        
    # insertion

    def AddFront(self, value):
        '''Insert data fron the front, returns None'''

        new_node = Node(value)

        if self.isEmpty():
            self.__front = self.__rear = new_node
        
        else:
            new_node.next = self.__front
            self.__front.prev = new_node
            self.__front = new_node
        
        self.__n += 1
            
    
    def AddRear(self, value):
        '''inserts item from the rear, returns None'''
        new_node = Node(value)
        if self.isEmpty():
            self.__front = self.__rear = new_node
        
        else:
            self.__rear.next = new_node
            new_node.prev = self.__rear
            self.__rear = new_node

        self.__n += 1

d = Deque()
d.AddFront(0)
d.AddFront(1)
d.AddFront(2)
d.AddRear(-1)
d.AddRear(-2)
print(d)
print('length',len(d))
print('peek from front',d.PeekFront())
print('peek from rear',d.PeekRear())
