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

    
    # printing and traverse

    def __str__(self) -> str:
        res = []
        for data in self.__items:
            if data:
                res.append(str(data))
        
        return ' '.join(res)
    

    def traverse(self):
        if self.__items:
            for i in range(len(self.__items)-1,-1, -1):
                if self.__items[i]:
                    print(self.__items[i])
            


s = Stack(5)
# s.push(10)
# s.push(20)
print(s)
s.traverse()