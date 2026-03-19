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
            curr = curr.next

        return '[ '+' ] <- [ '.join(res)+' ]'
    

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
    
    
    # Insertion

    def enqueue(self, value):
        '''inserts item from the rear, returns None'''
        new_node = Node(value)
        if self.__front is None:
            self.__front = self.__rear = new_node
        else:
            self.__rear.next = new_node
            self.__rear = new_node

        self.__n += 1


    


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q)