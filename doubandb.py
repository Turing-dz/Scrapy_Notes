from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建基类
Base = declarative_base()

# 创建引擎
engine = create_engine('mysql+pymysql://root:PASSWORD@127.0.0.1:3306/test?charset=utf8', echo=True)

# 定义 Book 类
class Book(Base):
    __tablename__ = 'book'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String(20))
    info = Column('info', String(30))
    star = Column('star', String(10))
    pl = Column('pl', String(10))
    introduce = Column('introduce', Text())

# 创建表结构
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
sess = Session()