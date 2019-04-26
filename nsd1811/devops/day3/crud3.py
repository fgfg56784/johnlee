from sqlacmy1 import Departments, Employees, Salary, Session

session = Session()

# hr = Departments(dep_id=1, dep_name='人事部')
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# cs = Departments(dep_id=4, dep_name='测试部')
# ui = Departments(dep_id=5, dep_name='设计部')
# fin = Departments(dep_id=6, dep_name='财务部')

zf = Employees(emp_id=2,emp_name='张飞', email='zf@12.com',dep_id=2)
gy = Employees(emp_id=3,emp_name='关羽',email='gy@66.com',dep_id=5)
an = Employees(emp_id=4,emp_name='安妮',email='an$bu.com',dep_id=3)

# zfgz = Salary(date=20190410, emp_id=1, baisc=12021, awards=2301)
# gygz = Salary(date=20190410, emp_id=2, baisc=11021, awards=3776)
# angz = Salary(date=20190410, emp_id=3, baisc=14021, awards=6776)

# session.add(zf)
# session.add_all([hr,ops,dev,cs,ui,fin])
session.add_all([zf, gy, an])
# session.add_all([zfgz,gygz,angz])
