import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', database='school')
cr = x.cursor()

print('enter the values you want to insert... ')
name = input('enter the name : ')
age = int(input('enter the age : '))
state = input('enter the state : ')
district = input('enter the district : ')
sql = 'insert into employee(name, age, state, district) values(%s,%s,%s,%s)'
values = (name, age, state, district)
cr.execute(sql, values)
x.commit()
print('------OUTPUT---------')
cr.execute('select * from employee')
res = cr.fetchall()
for i in res:
    print(i)

x.close()
