

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

# Replace the nested for loops below with your improvements


# list comprehension?

    # for name_2 in names_2:
    #     if name_1 == name_2:
    #         stack.push(name_1)

# send list number 1 and start out at index 0
first_name_list = BSTNode(names_1[0])
print(first_name_list.value)
for i in range(1, len(names_1)):
    # take each name from this list and insert into the tree
    print(i)
    # take result of this and compare it
    
# for list 2 compare
# compare list 1 with list 2 with the contains method on the BSTNode Class

second_name_list = BSTNode(names_2[0])

end_time = time.time()
# print (f"{len(stack)} duplicates:\n\n{', '.join(stack)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
