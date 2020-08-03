from ll import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        self.curr = 0
        
    def append(self, item):
        if len(self.data) == self.capacity:
            self.data[self.curr] = item
            # set enumerator to how many spaces ar left
            self.curr = (self.curr + 1) % self.capacity
        else:
            self.data.append(item)

    def get(self):

        return self.data
    

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f'