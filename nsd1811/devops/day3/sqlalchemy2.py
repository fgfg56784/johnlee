from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:1234@127.0.0.1/testdb?charset=utf8',
    encoding='utf8',
    # echo=True
)

Base = declarative_base()
Session = sessionmaker(bind=engine)

class  Departments(Base):
    __tablename__ = 'departments'
    dep_id = Column(Integer, primary_key = True)
    dep_name = Column(String(20))

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key = True)
    emp_name = Column(String(15))
    email = Column(String(20))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key = True)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    date = Column(Date)
    baisc = Column(Float(8,2))
    awards = Column(Float(8,2))

if __name__ == "__main__":
    Base.metadata.create_all(engine)