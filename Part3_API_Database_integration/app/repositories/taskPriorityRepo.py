from app.Part2_ApplyingSoftwareDesign1.task_priorities import TaskPriority
from sqlalchemy.orm import Session

class TaskPriorityRepo:
    def __init__(self, db:Session):
        self.db =db
        
    
    def create(self, Task_priority: TaskPriority):
      try:
        self.db.add(Task_priority)
        self.db.commit()
        return Task_priority
      except Exception as e:
          print(f"error :{e}")
    
    def update(self, Task_priority_id:int, update_data:dict):
      try:
        Task_priority = self.db.query(TaskPriority).filter(TaskPriority.id==Task_priority_id).first()
        if Task_priority:
            for key,value in update_data.items():
                setattr(TaskPriority, key, value)
            self.db.commit()
        return Task_priority
      except Exception as e:
          print(f"error: {e}")
    
    def delete (self,TaskPriority_id:int):
       try:
        Task_priority = self.db.query(TaskPriority).filter(TaskPriority.id==TaskPriority_id)
        if Task_priority:
            self.db.delete(Task_priority)
            self.db.commit()
        return Task_priority     
       except Exception as e:
           print(f"error : {e}")