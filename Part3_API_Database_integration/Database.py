from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
import os
from dotenv import load_dotenv

try:

     load_dotenv()
     
     
     username=os.getenv('DB_USERNAME')
     password=os.getenv('DB_PASSWORD')
     server=os.getenv('DB_SERVER')
     database=os.getenv('DB_NAME')
     driver=os.getenv('DB_DRIVER')
     
     
     connection_url=(f"mssql+pyodbc://{username}:{password}@"f"{server}/{database}?driver={driver}")
     
     
     engine= create_engine(connection_url)
     sessionLocal= sessionmaker(autocommit = False,autoflush=False,bind =engine)
     Base = declarative_base()
     
     print("Suc")
except Exception as e:
    print(f"Error in Database connection: {e}")