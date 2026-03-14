import ctypes

class DynamicArray:
    def __init__(self):
        self.__size = 1
        self.__n = 0
        # create a c type array with size = self.__size
        self.A = self.__create_array(self.__size)

    def __create_array(self, capacity):
        '''# creates a ctype array(static, referential) with size capacity'''
        return (capacity*ctypes.py_object)()
    
    def __len__(self):
        return self.__n
    

    # Resize Array
    def __resize(self, new_capacity):
        # Create new array with new capacity
        B = self.__create_array(new_capacity)
        self.__size = new_capacity

        # copy content of A in B
        for i in range(self.__n):
            B[i] = self.A[i]

        # Reassign
        self.A = B

    
    # printing
    def __str__(self):
        res = []
        for i in range(self.__n):
            res.append(str(self.A[i]))
    
        return '['+', '.join(res)+']'


    # insertion methods

    def append(self, value):
        '''inserts items at the end, returns None'''

        # check whether the array have space for adding new item or not,
        #  if not than resize the size of array
        if self.__size == self.__n:
            self.__resize(self.__size+10)

        self.A[self.__n] = value
        self.__n += 1

    
    def insert(self, index, value):
        '''Inserts item to the index given, returns None'''
        if self.__size == self.__n:
            self.__resize(self.__size+10)
        elif index > self.__n:
            raise IndexError('index out of range')
        for i in range(self.__n, index, -1):
            self.A[i] = self.A[i-1]

        self.A[index] = value
        self.__n += 1


    # deletion methods

    def pop(self):
        '''
        remove items from the end,
        and returns the removed item.
        '''

        if self.__n == 0:
            raise IndexError('pop on empty list')
        removed_item = self.A[self.__n -1]
        self.__n -= 1
        return removed_item
    
    
    def clear(self):
        '''clear all data in the array, returns empty array'''
        self.__size = 1
        self.__n = 0
        return self
    
    def __delitem__(self, index):
        if 0<= index < self.__n:
            for i in range(index, self.__n-1):
                self.A[i] = self.A[i+1]
            self.__n -= 1
        else:
            raise IndexError('Index out of range')

    def remove(self, item):
        '''removes the item given as parameter'''
        if self.__n == 0:
            raise IndexError('remove on empty array ')
        
        pos= None
        for i in range(self.__n):
            if self.A[i] == item:
                pos = i
                break
        
        if pos:
            removed_item = self.A[pos]
            del self[pos]
            return removed_item
        raise ValueError(f'item {item} not found')
    
    # Indexing

    def __getitem__(self, index):
        if 0<= index < self.__n:
            return self.A[index]
        if index < 0 and ((self.__n + index) >= 0):
            return self.A[self.__n + index]
        
        raise IndexError('index out of range')
    

    # searching

    def index(self, item):
        '''returns index position if item in array, else returns -1 if not found '''
        for i in range(self.__n):
            if self.A[i] == item:
                return i
            
        return -1

        

d = DynamicArray()
d.append(30)
d.append(40)
d.insert(0,10)
d.insert(1,20)
d.append(11)
d.remove(410)
print(d)