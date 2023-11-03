dict_1 = {
    1: 'apple',
    2: 'orange',
    3: 'mango',
    4: 'pinapple'
}
"""take key using value"""

item = input('enter the item you need : ')
for key, value in dict.items():
    if value == item:
        print(key)


"""we can give key and take value and if it is not presemted then it show error message"""

key = int(input('enter key'))
print(dict.get(key, 'item not present'))

"""length of dict"""
print(len(dict))

'''add new item'''
dict[4] = 'grapes'
print(dict)

"""remove item"""
dict.pop(1) # used to delete perticular item
del dict[1] # used to delete perticular item
dict.popitem() # used to delete last item
print(dict)

"""copy dict """
dict2 = dict.copy() #used to copy
dict_2 = dict(dict_1) # used to copy
print(dict_2)

"""dict constructor"""
new = dict(a='car',b='bike',c='lorry')
print(new)

