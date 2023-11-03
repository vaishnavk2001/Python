tup = ('apple', 'orange', 'mango', 'pineapple')
print(tup)
print(tup[2])
print(tup[-1])  # negative index

"""convert a tuple to list """

new_tuple = list(tup)  # converted
new_tuple.append('new item1')
tup = tuple(new_tuple)  # converted
print(tup)

"""tuple looping"""

if 'orange' in tup:
    print(True)

"""length"""
print(len(tup))

"""concatinate"""

tup_2 = (1,'siraj',2,'kiran')
print(tup+tup_2)

tup_3 = (1, 2, 4, 8, 6, 7, 5, 9, 2, 3, 4)
print(tup_3.count(4))  # for find repeate value
print(min(tup_3))
print(max(tup_3))
