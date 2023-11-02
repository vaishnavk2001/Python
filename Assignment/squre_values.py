def Squre(limit):
    for i in range(1, limit+1):
        sqre = i * i
        print('squre value of ', i, 'is', sqre)


limit = int(input('enter the limit : '))
print(Squre(limit))
