#importing the abstractmethod from abc module
from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass
    
    @abstractmethod
    def update(self, data):
        pass
    
    @abstractmethod
    def delete(self, data):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into SQL database")
    
    def update(self, data):
        print(f"Updating {data} in SQL database")
    
    def delete(self, data):
        print(f"Deleting {data} from SQL database")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into NoSQL database")
    
    def update(self, data):
        print(f"Updating {data} in NoSQL database")
    
    def delete(self, data):
        print(f"Deleting {data} from NoSQL database")

db_type = input("Enter database type (SQL, NoSQL): ")
data = input("Enter data: ")

if db_type == "SQL":
    db = SQLDatabase()
elif db_type == "NoSQL":
    db = NoSQLDatabase()
else:
    print("Invalid database type")
    exit()

db.insert(data)
db.update(data)
db.delete(data)
