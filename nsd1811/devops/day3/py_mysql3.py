from sqlacmy1  import  Departments, Employees, Salary, Session

session = Session()
hr = Departments(dep_id=1, dep_name='人事部')
ops = Departments(dep_id=2, dep_name='运维部')
dev = Departments(dep_id=3, dep_name='开发部')
qa = Departments(dep_id=4, dep_name='测试部')
finance = Departments(dep_id=5, dep_name='财务部')
ui = Departments(dep_id=6, dep_name='设计部')

# session.add(hr)
# session.add_all([hr, ops, dev, qa, finance, ui])

zf = Employees(emp_id=1,emp_name='张飞', email='zf@123.com',dep_id=5)
gy = Employees(emp_id=2,emp_name='关羽',email='gy@666.com',dep_id=3)
an = Employees(emp_id=3,emp_name='安妮',email='an$but.com',dep_id=1)

# session.add_all([zf, gy, an])

zfgz = Salary(date=20190410, emp_id=1, baisc=12021, awards=2301)
gygz = Salary(date=20190410, emp_id=2, baisc=11021, awards=3776)
angz = Salary(date=20190410, emp_id=3, baisc=14021, awards=6776)

# session.add_all([zfgz, gygz, angz])
############################################
query1 = session.query(Departments)
# print(query1)  #query1 是sql 语句
# deps = query1.all()  #取出查询的全部结果
# print(deps)  # deps是由数据库表每行记录  生成的实例  构成的列表
# print('部门ID  部门名')
# for dep in query1:
#     print('     ' + str(dep.dep_id) +'  '+ dep.dep_name)
# print()
#######################################################
# query2 = session.query(Employees)
# for emp in query2:
#     print(emp.emp_id, emp.emp_name, emp.email, emp.dep_id)
# print()
#######################################################
# query3 = session.query(Salary.date, Salary.baisc+Salary.awards)
# for date,tiltle in query3:
#     print(date, tiltle)
# print()
#######################################################
# query4 = session.query(Employees).order_by(Employees.emp_id)
# print('员工编号  员工姓名          email   所属部门ID')
# for emp in query4:
#     print('      ' + str(emp.emp_id)+ '       '+ emp.emp_name + '    ' +  emp.email+ '             ' +str(emp.dep_id))
# print()
#######################################################
# query5 = session.query(Departments).order_by(Departments.dep_id)[2:5]  #排序后,切片
# for dep in query5:
#     print('     ' + str(dep.dep_id) +'  '+ dep.dep_name)
# print()
#######################################################
# query6 = session.query(Departments).filter(Departments.dep_id <= 3)
# print(query6)
# for dep in query6:
#     print(dep.dep_id, dep.dep_name)
#######################################################
# query7 = session.query(Employees).filter(Employees.email.like('%123%'))
# print(query7)
# for emp in query7:
#     print(emp.emp_id, emp.emp_name,emp.email, emp.dep_id)
#######################################################
# query8 = session.query(Employees).filter(Employees.dep_id.in_([1,3]))
# print(query8)
# for emp in query8:
#      print(emp.emp_id, emp.emp_name,emp.email, emp.dep_id)
############################################################
# query9 = session.query(Employees).filter(~Employees.dep_id.in_([1,3]))
# print(query9)
# for emp in query9:
#      print(emp.emp_id, emp.emp_name,emp.email, emp.dep_id)
###########################################################
from sqlalchemy import and_, or_
# query10 = session.query(Departments).filter(and_(Departments.dep_id >= 2, Departments.dep_id <= 6))
# for dep in query10:
#     print(dep.dep_id, dep.dep_name)
############################################################
# query11 = session.query(Departments).\
# filter(or_(Departments.dep_id <= 2, Departments.dep_id >= 5)).order_by(Departments.dep_id)
# for dep in query11:
#     print(dep.dep_id, dep.dep_name)
###################################################################
# query12 = session.query(Departments).count()
# print(query12)  #统计departments表的行数
#######################################################
# query13 = session.query(Employees.emp_name, Departments.dep_name).join(Departments)  #.order_by(Employees.emp_name)
# for emp_name, dep_name in query13:
#     print(emp_name, dep_name)
#######################################################
# query14 = session.query(Departments.dep_name, Employees.emp_name).join(Employees)  #.order_by(Employees.emp_name)
# for dep_name, emp_name in query14:
#     print(dep_name, emp_name)
#######################################################
# query15 = session.query(Departments).filter(Departments.dep_name == '人事部')
# hr = query15.one()
# hr.dep_name = '人力资源部'
#######################################################
query15 = session.query(Departments).filter(Departments.dep_id == 6)
ui = query15.one()
session.delete(ui)
#######################################################
session.commit()
session.close()