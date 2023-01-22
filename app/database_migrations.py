from sqlmodel import SQLModel
from .models import database #importing the database models allow SQLModel to automatically generate the database
from .database import engine

def create_db_and_tables():  # 
    SQLModel.metadata.create_all(engine)  # 


    
if __name__ == "__main__":  # 
    create_db_and_tables()  # 
