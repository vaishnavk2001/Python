"""normal exception handling"""

def Handling_sum(a, b):
    try:
        c = a // b
        print('sum is :', c)
    except:
        print("zero can't divide so change the second value..!")
    finally:
        print('ok great....')


a = int(input('enter the number: '))
b = int(input('enter the second number: '))
print(Handling_sum(a, b))

"""list exception handling"""


def list(inp):
    try:
        list1 = ['apple', 1, 'orange', 'pinapple', 3, 5, 8]
        print(list1[inp])
    except:
        print("can't find this...!")
    finally:
        print('it is finally block...!')


inp = int(input('enter the number:'))
print(list(inp))
