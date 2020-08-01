class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []

    def append(self, item):
        # length can't be more than 5
        if len(self.data) == self.capacity:
            # insert the new elment at position 0
            self.data.insert(5, item)
            # get rid of last elment
            self.data.pop(0)
        else: 
            self.data.append(item)
        return self.data

    def get(self):
        return self.data
    

buffer = RingBuffer(5)
for i in range(50):
    buffer.append(i)

print(buffer.get()) 
