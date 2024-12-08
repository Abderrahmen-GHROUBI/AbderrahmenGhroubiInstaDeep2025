from sqlalchemy import String,Integer,Column
from Database import Base


class TaskPriority(Base):
    __tablename__ = 'taskPriorities'
    
    
    id = Column(Integer, primary_key=True,index=True)
    
    Taskpriority= Column(String,nullable=False)
    
    
