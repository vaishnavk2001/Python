"""list comprehensive"""
li = [i * i for i in range(1, 11)]
print(li)

""" cut and add in list"""

new_list = []
for i in "avodha":
    new_list.append(i)

print(new_list)

"""change the above program into list comprehensive"""

li = [i for i in 'avodha']
print(li)

"""find even number normal"""
eve = []
for i in range(21):
    if i % 2 == 0:
        eve.append(i)

print(eve)

"""change to list comprehensive"""

new_lst = [i for i in range(0,20) if i % 2 == 0]
print(new_lst)

"""input from user letter,word & find the number of letter repeat"""
word = input('enter the word :')
letter = input('enter the letter you need to find count :')
count = 0
for i in word:
    if i == letter:
        count += 1

print("count = ",count)

"""power of number"""
list = [1,2,3,4,5]
new_list = [i**2 for i in  list]
print(new_list)
