from LinkedList import DoublyLinkedList
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        # add item to list
        ll = DoublyLinkedList(None)
        ll.add_to_head(item)
        print(ll)
        # length can't be more than 5
        if len(ll) > self.capacity:
            print('here')
            # get rid of last elment
            lastEl = self.data.pop(0)
            print(lastEl)
            # insert the new elment at position 0
            self.data.insert(0, item)
        
        return self.data

    def get(self):
        
        return ll
    

buffer = RingBuffer(5)

buffer.append('a')
buffer.append('a')
buffer.append('a')
buffer.append('a')

print(buffer.get()) 
