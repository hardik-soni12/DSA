from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__n = 0

    def __len__(self):
        return self.__n
    
    # Insertion methods
    def insert_head(self, value):
        '''
        inserts data from the head, returns None
        '''
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            
        else:
            new_node.next = self.__head
            self.__head = new_node
        
        self.__n += 1  

    
    def append(self, value):
        '''
        insert value from the end , returns None
        '''

        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node

        else:
            curr = self.__head
            while curr.next is not None:
                curr = curr.next
            
            curr.next = new_node

        self.__n += 1
    


    # printing
    def __str__(self) -> str:
        curr = self.__head
        res= []
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        
        return ' -> '.join(res)

l = LinkedList()
l.insert_head(10)
l.insert_head(20)
l.append(5)
l.append(0)
print(l)