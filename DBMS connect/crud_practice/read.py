import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', db='school')
cr = x.cursor()
print('select search type \n 1. name \n 2.age \n 3.state \n 4.district ')
uip = int(input('enter you choice : '))
if uip == 1:
    """name wise search"""
    nm = input('enter the name : ')
    cr.execute('select * from employee where name = %s', nm)
    res = cr.fetchall()
    for i in res:
        print(i)

elif uip == 2:
    """age wise search"""
    age = int(input('enter the age : '))
    cr.execute('select * from employee where age = %s', age)
    res = cr.fetchall()
    for i in res:
        print(i)

elif uip == 3:
    """state wise search"""
    state = input('enter the state: ')
    cr.execute('select * from employee where state = %s', state)
    res = cr.fetchall()
    for i in res:
        print(i)

elif uip == 4:
    """district wise search"""
    dis = input('enter the district : ')
    cr.execute('select * from employee where district = %s', dis)
    res = cr.fetchall()
    for i in res:
        print(i)

x.commit()
x.close()


