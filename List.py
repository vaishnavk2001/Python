list_new = ['a','b','c',1,2,3]
list_old = [10,11,12]
print(list_old+list_new)

list_1 = ['orange','apple','mango','pinapple','jackfruit']
print('orange' in list_1)
list_1[2] = 'vegitable'

list_1.append('hello')
list_1.insert(1,'egg')
print(len(list_1))
print(list_1.index('mango'))


# print(list_1)

"""list slicing """
new_list = ['apple','orange','a','b','c',1,2,3,10,11,12]
print(new_list[1:])
print(new_list[5:10])
print(new_list[:5])
print(new_list[1:10:2])
