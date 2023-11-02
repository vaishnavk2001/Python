"""file creation"""
# file1 = open('demo.txt','w')
# file1.close()

"""file read content"""

# file1 = open('demo.txt','r')
# content = file1.read()
# print(content)
# file1.close()

"""file write"""

# file = open('new_file','w')
# # file.write('hello this is new content')
# file.write('this is next')
# file.close()

"""file append"""

file = open('new_file','a')
file.write('helo this is third content')
file.close()
