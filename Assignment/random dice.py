import random

"""generate dice randomly"""
nw_list = ['one', 'two', 'three', 'four', 'five', 'six']
new_ele = random.randint(1,5)
print(nw_list[new_ele])

"""generate random list """
n1 = []
# r = int(input('enter the range :'))
# bound = int(input('enter the boundary limit : '))
for i in range(1,7):
    new_ele = random.randint(1,100)
    n1.append(new_ele)
print(n1)

"""question paper generator"""

list_1 = []
qc = int(input("enter the total number of question : "))
for i in range(1, qc + 1):
    ques = input("enter the question :")
    list_1.append(ques)
print(list_1)

nq = int(input("enter the number of question you need : "))
if nq > qc:
    print("sorry not enough questions are here...!")
else:
    n = random.sample(range(qc), nq)
    for i in n:
        print(list_1[i])
    # r_num = random.sample(range(qc), nq)
    # print(list_1[r_num])

    # for i in range(1, nq + 1):
    #     r_num = random.sample(range(qc), nq)
    #     # r_num = random.randint(1, qc)
    #     print(list_1[r_num])
# import random
#
# n = random.sample(range(5),2)
# print(n)