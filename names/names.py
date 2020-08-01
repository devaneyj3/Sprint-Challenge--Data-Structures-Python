

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

# HOW DO I INSERT STRINGS INTO A BSTNode


# send list number 1 and start out at index 0
first_name_list = BSTNode(names_1)

# for list 2 compare
# compare list 1 with list 2 with the contains method on the BSTNode Class
second_name_list = BSTNode(names_2)


for i in range(1, len(names_1)):
    # take each name from this list and insert into the tree
    first_name_list.insert((names_1[i]).value)
    # take result of this and compare it
for i in range(1, len(names_2)):
    second_name_list.insert((names_2[i]).value)
    
print(first_name_list)
print(second_name_list)
    
end_time = time.time()
# print (f"{len(stack)} duplicates:\n\n{', '.join(stack)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
