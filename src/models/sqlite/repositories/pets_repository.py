from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_pet(self, name: str, type: str, owner_id:int | None = None) -> None:
        with self.__db_connection as database:
            try:
                pet_data = PetsTable(name=name, type=type, owner_id=owner_id)
                database.session.add(pet_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
        
    def list_pets(self) -> List:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
            
    def delete_pets(self, name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(PetsTable)
                        .filter(PetsTable.name == name)
                        .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
   # def connect_pet_to_person(self, person_first_name: str, pet_name: str) -> None:
   #     with self.__db_connection as database:
   #         try:
   #             pass
   #         except Exception as exception:
   #             database.session.rollback()
   #             raise exception