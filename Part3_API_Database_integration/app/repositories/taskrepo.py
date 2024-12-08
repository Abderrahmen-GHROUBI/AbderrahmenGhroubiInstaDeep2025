from app.Part2_ApplyingSoftwareDesign1.task import Task
from sqlalchemy.orm import Session


class TaskRepo:
    def __init__(self,db:Session):
        self.db = db
        
        
    def create(self, Task_: Task):
      try:
        self.db.add(Task_)
        self.db.commit()
        return Task_
      except Exception as e:
          print(f"error :{e}")
    
    def update(self, Task_id:int, update_data:dict):
      try:
        Task_ = self.db.query(Task).filter(Task.id==Task_id).first()
        if Task_:
            for key,value in update_data.items():
                setattr(Task_, key, value)
            self.db.commit()
        return Task_
      except Exception as e:
          print(f"error: {e}")
    
    def delete (self,Task_id:int):
       try:
        Task_ = self.db.query(Task).filter(Task.id==Task_id)
        if Task_:
            self.db.delete(Task_)
            self.db.commit()
        return Task_     
       except Exception as e:
           print(f"error : {e}")