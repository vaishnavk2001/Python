import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', database='school')
cr = x.cursor()
nm = input('enter the name :')
cr.execute('select * from sample2 where name=%s', nm)
dt = cr.fetchone()
print(dt)

x.commit()
x.close()


