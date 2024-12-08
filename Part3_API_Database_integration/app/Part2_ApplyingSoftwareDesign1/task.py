from sqlalchemy import String,Integer,Column,ForeignKey
from Database import Base
from sqlalchemy.orm import relationship 



class Task(Base):
    __tablename__ = 'tasks'
    
    
    id = Column(Integer, primary_key=True,index=True)
    category_id=(Integer, ForeignKey("taskPriorities.id"))
    priority_id=(Integer,ForeignKey("taskCategories.id"))
    description= Column(String,nullable=False)
    dueDate=Column()
    TaskPriority = relationship("taskPriorities")
    TaskCaterory = relationship("TaskCategory")
    
    


