"""word finder"""
import re

word = input('enter the particular word :  ')
para = input('enter the paragraph : ')

if re.findall(word,para):
    print('matched')
    print(re.findall(word,para))
else:
    print('not matched')