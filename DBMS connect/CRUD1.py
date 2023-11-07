import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', database='school')
cr = x.cursor()
"""create"""
# a = 'create table sample2(id int,name varchar(20),age int,place varchar(20),district varchar(20))'
# a = 'insert into sample2 values(3,"arun",27,"pala","kottayam")'

a = 'select * from sample2'
cr.execute(a)
res = cr.fetchall()
for i in res:
    print(i)
    
# c = cr.fetchone() # first value fetch

"""update"""
# a = 'update sample2 set age = 30 where id =3'
"""delete"""
# a = 'delete from sample2 where name = "arun" '


"""give a name and search"""

# nm = input('enter the name ')
# b = 'select * from sample2 where name = %s'
# cr.execute(b,nm)
# dt_num = cr.fetchone()
# print(dt_num)

x.commit()
x.close()
