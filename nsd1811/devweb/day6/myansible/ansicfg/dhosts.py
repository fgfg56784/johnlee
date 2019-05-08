#!/opt/djenv/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1811/devweb/day6/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), nullable=False, unique=True)

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(100), nullable=False, unique=True)
    ipaddr = Column(String(15), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Host.ipaddr).join(Host)
    # print(qset.all())  #出来的格式为列表套元组的格式
    result = {}
    for group, ip in qset.all():
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)               #把原格式变为字典套字典套列表的格式 {{[]}} 例如: {'dbserver': {'hosts': ['192.168.1.1', '192.168.1.2']}}

    print(json.dumps(result)) #最后把字典转换为ansible能读取的json字符串格式

