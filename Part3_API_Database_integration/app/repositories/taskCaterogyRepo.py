from app.Part2_ApplyingSoftwareDesign1.task_category import TaskCategory
from sqlalchemy.orm import Session

class TaskCategoryRepo:
    def __init__(self, db:Session):
        self.db =db
        
    
    def create(self, Task_category: TaskCategory):
      try:
        self.db.add(Task_category)
        self.db.commit()
        return Task_category
      except Exception as e:
          print(f"error :{e}")
    
    def update(self, taskCategory_id:int, update_data:dict):
      try:
        Task_Category = self.db.query(TaskCategory).filter(TaskCategory.id==taskCategory_id).first()
        if Task_Category:
            for key,value in update_data.items():
                setattr(Task_Category, key, value)
            self.db.commit()
        return Task_Category
      except Exception as e:
          print(f"error: {e}")
    
    def delete (self,taskCategory_id:int):
       try:
        transaction = self.db.query(TaskCategory).filter(TaskCategory.id==taskCategory_id)
        if transaction:
            self.db.delete(transaction)
            self.db.commit()
        return transaction     
       except Exception as e:
           print(f"error : {e}")