import pymysql

x = pymysql.connect(host='localhost', user='root', password='1234', database='school')
cr = x.cursor()

print('-----update happen by id base -----')
print("")
clname = input('enter the column you need to update :')
value = input('enter the new value: ')
n_id = int(input('enter the id : '))

print('before update')
print("")
cr.execute('select * from employee')
res = cr.fetchall()
for i in res:
    print(i)

print("updating....!")
print("")
sql = f'UPDATE employee SET {clname} = %s WHERE emp_id = %s'
values = (value, n_id)
cr.execute(sql, values)
x.commit()

print('---output---')
print("")
cr.execute('select * from employee')
new_res = cr.fetchall()
for i in new_res:
    print(i)

x.close()
