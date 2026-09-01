from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.entities.people import PeopleTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface


class PetsRepository(PetsRepositoryInterface):
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
    def connect_pet_to_person(self, owner_id: int, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                person = (
                    database.session
                    .query(PeopleTable)
                    .filter(PeopleTable.id == owner_id)
                    .first()
                )

                pet = (
                    database.session
                    .query(PetsTable)
                    .filter(PetsTable.id == pet_id)
                    .first()
                )

                if person is None or pet is None:
                    raise ValueError("Person or Pet not found")

                pet.owner = person

                database.session.commit()

            except Exception:
                database.session.rollback()
                raise
    
   # def connect_pet_to_person(self, person_first_name: str, pet_name: str) -> None:
   #     with self.__db_connection as database:
   #         try:
   #             pass
   #         except Exception as exception:
   #             database.session.rollback()
   #             raise exception