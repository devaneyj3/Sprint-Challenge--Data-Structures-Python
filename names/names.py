

import time

from search_tree import BSTNode
start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# We need to store duplicates
duplicates = []

first_name_list = BSTNode()

# cylcle through the Binary Tree

for name in names_1:
    first_name_list.insert(name)
    
for i in names_2:
    if(first_name_list.contains(i)):
    #     check if first name list has values contained into the second name list
    #     take result of this and compare it
        duplicates.append(i)
    
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
