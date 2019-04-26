import pymysql
conn =  pymysql.connect(
    host= '127.0.0.1',
    port= 3306,
    user= 'root',
    passwd= '1234',
    db= 'nsd1811',
    charset= 'utf8'
)

cursor = conn.cursor()

insert_dep1 = 'insert into 部门表 values (%s, %s)'
dep = [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '市场部')] 
# cursor.executemany(insert_dep1, dep)

dep2 = [(5, '测试部')]
# cursor.executemany(insert_dep1, dep2)

dep3 = [(6, '财务部'), (7, '运营部')]
# cursor.executemany(insert_dep1, dep3)

update_hr = 'update 部门表 set 部门名=%s where 部门名=%s'
hr = ('人力资源部', '人事部')
# cursor.execute(update_hr, hr)

del_yy = 'delete from 部门表 where 部门名=%s'
yy = ('运营部',)
# cursor.executemany(del_yy, yy)

# select1 = 'select * from 部门表 order by 部门ID'
# cursor.execute(select1)
# result1 = cursor.fetchone()  #取一行记录
# result2 = cursor.fetchmany(2) # 取多行记录
# result3 = cursor.fetchall() #  取剩下的全部记录
# print(result1)
# print(result2)
# print(result3)

select2 = 'select * from 部门表'
cursor.execute(select2)
result = cursor.fetchmany(4)

cursor.scroll(-3)

cursor.scroll(1, mode='absolute')
# cursor.scroll(2, mode='ralative')
result4 = cursor.fetchone()
result5 = cursor.fetchmany(3)

print(result)
print(result4)
print(result5)

conn.commit()
cursor.close()

# insert_dpl1 = 'insert into 员工表 values (%s, %s)'
# dpl = [(1, '人事部'), (2, '运维部'), (3, '开发部'), (4, '市场部')] 
# cursor.executemany(insert_dpl1, dpl)
# conn.commit()
# cursor.close()

# insert_gzb = 'insert into 工资表 values (%s, %s)'
# gzb = '[(1, 1, 2019-4-10)]'


conn.close()
