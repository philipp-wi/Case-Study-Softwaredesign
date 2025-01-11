from tinydb import Query, TinyDB
from serializer import serializer
import os

class User:

    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')

    def __init__(self, id, name) -> None:
        """Create a new user"""
        self.name = name
        self.id = id

    def store_data(self)-> None:
        """Save the user to the database"""
        userQuery = Query()
        result = self.db_connector.search(userQuery.name == self.name)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
            print("Data updated.")
        else:
            # If the user doesn't exist, insert a new record
            self.db_connector.insert(self.__dict__)
        print("Data inserted.")
        pass

    def setOptionalData(self,alter = "", jahrgang = "", email = "") -> None:
        self.alter = alter
        self.jahrgang = jahrgang
        self.email = email

    def delete(self) -> None:
        """Delete the user from the database"""
        pass
    
    def __str__(self):
        return f"User {self.id} - {self.name}"
    
    def __repr__(self):
        return self.__str__()
    
    @staticmethod
    def find_all(cls) -> list:
        """Find all users in the database"""
        pass

    @classmethod
    def find_by_attribute(cls, by_attribute : str, attribute_value : str) -> 'User':
        """From the matches in the database, select the user with the given attribute value"""
        pass
