import sqlite3
from classes import Soldier

class DatabaseManageri:
    def __init__(self, db_name="soldier.db"):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS table_of_soldier (
                id INTEGER PRIMARY KEY UNIQUE,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                gender TEXT NOT NULL,                       
                city INTEGER NOT NULL,
                Distance_from_base INTEGER NOT NULL
            )
        """)
        self.connection.commit()

    def insert_soldier(self, soldieri):
     self.cursor.execute(
        "INSERT INTO table_of_soldier (id, first_name, last_name, gender, city, Distance_from_base) VALUES (?, ?, ?, ?, ?, ?)", (soldieri.id, soldieri.first_name, soldieri.last_name, soldieri.gender, soldieri.city, soldieri.Distance_from_base))
     
     self.connection.commit()



  
    


