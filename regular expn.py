import re

""".match find word in first of the sentence """

# patter = r"avodha"
# if re.match(patter,'avodha hello how are you '):
#     print('match')
# else:
#     print('not matched ')

""".search find the word from the whole sentence"""

# patter = r"avodha"
# if re.search(patter, 'hello how are you avodha '):
#     print('matched')
# else:
#     print('not matched')

"""findall used to find number of count"""

print(re.findall('avodha','rdfvgbavodhafcgvhbjavodhacfgvhbjavodhaertfgybhjavodha'))
