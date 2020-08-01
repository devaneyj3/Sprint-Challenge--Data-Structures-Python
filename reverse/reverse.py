class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)
        self.head = node


    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # print(self.head.next.value)
        # we need a pointer to the next node after self.head
        self.head = node
        node.set_next(prev)
        
        while current:
            print(f'self.head is, {current}')
            if current.get_next() is None:
                # put this node in front 
                targetNode = current
                print(f'this node does not have a next, {targetNode}')
                self.add_to_head(targetNode)
            current = current.get_next()
        # while current:
        #     nxt = current.next
        #     current.next = prev
            
        #     prev = current
        #     current = nxt
        # self.head = prev
        
ll = LinkedList()

ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.add_to_head(4)
ll.add_to_head(5)

ll.reverse_list(5, 1)

