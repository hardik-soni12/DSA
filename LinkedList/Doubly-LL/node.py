class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

    def __iter__(self):
        curr = self
        while curr:
            yield curr.data
            curr = curr.next