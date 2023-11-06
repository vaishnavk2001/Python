set1 = {'a',1,'apple','orange'}
set1.add('new ele')  #add
set1.update(['grapes','mango','pinapple'])
print(len(set1))
set1.remove('pinapple')
set1.discard('apple')
set1.pop()
set1.clear()
print(set1)

"""set operations"""
"""union"""

set_1 = {'apple','orange','mango','pineapple'}
set_2 = {1,2,3,4}

set_3 = set_1.union(set_2)
set_3 = set_1|set_2 #another for union
set_1.update(set_2) # another for union
print(set_1)

"""set(-)"""
#
set_2 = {1,2,3,4}
set_3 = {2,3,4,5}
set_4 = set_2-set_3
print(set_4)

"""avoid duplication"""
lis = [1,1,2,4,4,3,5,5]
print(set(lis))
