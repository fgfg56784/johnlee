#! /opt/dj2/bin/python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd_2018/nsd1811/devweb/day6/myansible2/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'myansi2_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True, nullable=False)

class Hosts(Base):
    __tablename__ = 'myansi2_hosts'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True, nullable=False)
    ipaddr = Column(String(15), unique=True, nullable=False)
    group_id = Column(Integer, ForeignKey('myansi2_hostgroup.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(HostGroup.groupname, Hosts.ipaddr).join(Hosts)
    # print(qset.all())
    result = {}
    for group, ip in qset.all():
        if group not in result:
            result[group] = {}
            result[group]['hosts'] = []
        result[group]['hosts'].append(ip)
    print(json.dumps(result))