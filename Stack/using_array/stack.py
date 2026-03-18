class Stack:
    def __init__(self, size) :
        self.size = size
        self.__items = [None]* self.size
        self.top = -1


    # insertion

    def push(self, value):
        '''inserts item from the top returns None'''
        if self.top == self.size-1:
            return 'stack Overflow'
        self.top+=1
        self.__items[self.top] = value


s = Stack(5)
s.push(10)
s.push(20)

