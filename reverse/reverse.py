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
        # print('\nnode passed in to add_to_head is ', node)

        if self.head is not None:
            # print(f'\nself.head: {self.head.get_value()}')
            node.set_next(self.head)
            # print(f'\nNew self.head.next: {self.head.get_next().value}\n')
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

    def reverse_list(self, node=None, prev=None):
        prev = None
        current = self.head
        print(f'self.head: {self.head}')
        while current is not None:
            next = current.get_next()
            current.set_next(prev)
            
            prev = current
            print(f'prev is: {current}')
            current = next
        self.head = prev
ll = LinkedList()

ll.add_to_head(1)
ll.add_to_head(2)
ll.add_to_head(3)
ll.add_to_head(4)
ll.add_to_head(5)

ll.reverse_list()

