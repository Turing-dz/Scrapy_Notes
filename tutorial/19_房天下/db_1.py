from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Text
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()#1.创建表对象的基类Base
class House(Base):#2.根据基类创建表对象
    __tablename__="house"
    id=Column(Integer,primary_key=True,autoincrement=True)
    block=Column(String(125))
    title=Column(String(125))
    rent=Column(String(125))
    data=Column(Text())
    
    
    
    
    
engine=create_engine(#3.创建数据库引擎，定义数据库连接参数。
    "mysql+pymysql://root:PASSWORD@127.0.0.1:3306/test?charset=utf8",
    pool_size=100,
    max_overflow=500,
    echo=True,
)





Base.metadata.create_all(engine)#4.引擎与类建立联系，在数据库中创建所有基于 Base 定义的表。





Session=sessionmaker(engine)#绑定数据库引擎 engine，用于创建数据库会话
sess=scoped_session(Session)#创建一个作用域会话 sess，它是线程安全的，可以在多线程环境中使用