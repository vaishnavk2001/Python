import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', database='school')
cr = x.cursor()
old = input('enter the person : ')
cr.execute('select * from sample2 where name=%s',old)
n_res = cr.fetchone()
print(n_res)
new = input('enter the new name : ')
cr.execute('update sample2 set district = %s where name = %s', (new, old))
x.commit()
cr.execute('select * from sample2 where name=%s',old)
res = cr.fetchone()
print(res)


x.close()
