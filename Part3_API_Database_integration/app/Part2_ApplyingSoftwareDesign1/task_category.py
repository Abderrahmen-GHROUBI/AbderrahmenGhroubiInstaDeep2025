from sqlalchemy import String,Integer,Column
from Database import Base


class TaskCategory(Base):
    __tablename__ = 'taskCategories'
    
    
    id = Column(Integer, primary_key=True,index=True)
    categoryDescription= Column(String,nullable=False)
    
    

