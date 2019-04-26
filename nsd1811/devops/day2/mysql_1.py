import pymysql

#创建到数据库的连接
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='1234',
    db='nsd1811',
    charset='utf8'
)

cursor = conn.cursor() # 创建游标
create_dep= '''create table 部门表(部门ID int, 
部门名 char(10), primary key(部门ID)
)'''  # sql语句
cursor.execute(create_dep)  
conn.commit()
cursor.close()

cursor = conn.cursor() # 创建游标
create_dep= '''
create table 员工表(员工编号 int, 
姓名 char(15), 
性别 varchar(5),                         
出生日期 date, 
电话 int, 
家庭住址 char(50), 
email char(50), 
部门ID int, 
 primary key(员工编号),
foreign key(部门ID) references 部门表(部门ID)
)'''  # sql语句   
cursor.execute(create_dep)   # 执行sql语句
conn.commit()  # 提交改动
cursor.close()   # 关闭游标

cursor = conn.cursor() # 创建游标
create_dep= '''
create table 工资表(auto_id int, 
员工编号 int, 
工资日 date, 
基本工资 int, 
奖金 int, 
primary key(auto_id), 
foreign key(员工编号) references 员工表(员工编号)
)'''  # sql语句
cursor.execute(create_dep)
conn.commit()
cursor.close()
conn.close()