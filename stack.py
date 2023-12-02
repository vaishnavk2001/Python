stack = []
def push_fun():
    ele = input('enter the element : ')
    stack.append(ele)
    print('inserted...')


def pop_fun():
    if len(stack) == 0:
        print('stack is empty...! ')
    else:
        stack.pop()


def display():
    print(stack)


while True:
    print("enter the choice : ")
    print(" 1.add \n 2.delete \n 3.exit \n 4.display")
    user_ip = int(input(":"))
    if user_ip == 1:
        push_fun()
    elif user_ip == 2:
        pop_fun()
    elif user_ip == 3:
        exit()
    elif user_ip == 4:
        display()
    else:
        print("enter the proper choice...!")
