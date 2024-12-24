from sqlalchemy import create_engine,MetaData,Table
from sqlalchemy import Column,String,Integer,select,ForeignKey
engine=create_engine(
    "mysql+pymysql://root:PASSWORD@127.0.0.1:3306/test",
    max_overflow=5,#超过连接池大小外最多可以创建的连接数
    pool_size=10,#链接池大小
    echo=True#调试信息展示
)
metadata=MetaData()#取得元数据，介绍数据库
#定义表
user=Table("user",metadata,
           Column("id",Integer,primary_key=True,autoincrement=True),
           Column("name",String(10)))
# metadata.create_all(engine)#参加数据表
# engine.execute("insert into user (name) value ('zoe')")#1.原生sql语句增删改查
# conn=engine.connect()#2.利用（表对象）方法进行增删改查
# conn.execute(user.insert(),{"name":"jodie"})
# conn.close()
#3.集成orm类操作数据库
from sqlalchemy.orm import sessionmaker,relationship,scope_session#代替conn，执行数据库语句，同一个线程公用一个session，不同线程不同session，使用scope_session()函数维护线程sessio安全
from sqlalchemy.ext.declarative import declarative_base#创建数据库表类的基类
base=declarative_base()#创建基类
# class Host(base):
#     __tablename__="hosts"
#     id=Column(Integer,primary_key=True,autoincrement=True)
#     hostname=Column(String(64),unique=True,nullable=False)
#     ip_addr=Column(String(128),unique=True,nullable=False)
#     port=Column(Integer,default=8080)
# # base.metadata.create_all(engine) #创建表
# if __name__=="__main__":
#     session=sessionmaker(bind=engine)
#     sess=session()#创建实例
#     h=Host(hostname="test1",ip_addr="127.0.0.3")
#     sess.add(h)#多条add_all([1,2,3])
#     sess.commit()
#关联表一对多
class User(base):
    __tablename__ = 'user1'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    gender = Column(String(10), nullable=True, default="保密")
    town = Column(String(125))
    language = relationship('Language', backref='user1',cascade="all,delete")#1对多的1

class Language(base):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    advantage = Column(String(125), nullable=True)
    disadvantage = Column(String(125), nullable=True)
    user_id = Column(Integer, ForeignKey('user1.id'))#1对多的多
base.metadata.create_all(engine) #创建表
#关联表多对多（多了一个A2B中间关系表）
BASE = declarative_base()

User2Lan = Table('user_2_language', BASE.metadata,
                 Column('user_id', ForeignKey('user.id'), primary_key=True),
                 Column('language_id', ForeignKey('language.id'), primary_key=True))

class User(BASE):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    gender = Column(String(10), nullable=True, default='保密')
    town = Column(String(125))
    language = relationship('Language', secondary=User2Lan, backref='user', cascade="all, delete")

class Language(BASE):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(125), nullable=True)
    advantage = Column(String(125), nullable=True)
    disadvantage = Column(String(125), nullable=True)