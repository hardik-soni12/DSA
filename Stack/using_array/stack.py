class Stack:
    def __init__(self, size) :
        self.size = size
        self.__items = [None]* self.size
        self.top = -1


    def __len__(self):
        return self.top + 1

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
        '''traverse from the top'''
        if self.__items:
            for i in range(len(self.__items)-1,-1, -1):
                if self.__items[i]:
                    print(self.__items[i])

    
    # peek and isEmpty

    def isEmpty(self):
        '''returns True if stack is empty else False'''
        if self.top == -1:
            return True
        return False

    def peek(self):
        '''returns the top item from th stack if not empty'''
        if self.isEmpty():
            return 'empty stack'
        return self.__items[self.top]
    

    # deletion

    def pop(self):
        '''removes item from the top and returns removed item'''

        if self.isEmpty():
            raise IndexError('pop on empty stack')
        
        removed_item = self.__items[self.top]
        self.__items[self.top] = None
        self.top -= 1
        return removed_item

s = Stack(5)
s.push(10)
s.push(20)
s.push(22)
s.pop()
print(s)
# s.traverse()
print(len(s))
