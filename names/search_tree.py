"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # go to right
        if value <  self.value:
            # if nothing right insert
            if not self.left:
                self.left = BSTNode(value)
            else:
                # or repeat the process at the other parent node
                self.left.insert(value)
        elif value > self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)    
        # handle duplicates
        else:
            self.right = BSTNode(value) 
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):

        if self.value == target:
            return True
        # we go right if we do not find the value
        if self.value > target:
            if self.left is not None:
                return self.left.contains(target)
        elif self.value < target:
            if self.right is not None:
                return self.right.contains(target)
        else: 
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        # start with root node and assign that to value
        curr = self
        if not self.right:
            return curr.value
        # cycle through list to see the highest value
        while curr.right:
            curr = curr.right
        return curr.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # start with root node and assign that to value
        fn(self.value)
        # cycle through list to see the highest value
        if self.right is not None:
            #  use recursion to cycle through the subtree
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)