import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', database='school')
cr = x.cursor()

nm = input('enter the name : ')
cr.execute('select * from sample2 where name=%s', nm)
o_res = cr.fetchone()
print(o_res)

cr.execute('delete from sample2 where name=%s',nm)
x.commit()

print('-----output-----')
cr.execute('select * from sample2')
n_res = cr.fetchall()
for i in n_res:
    print(i)

x.close()

