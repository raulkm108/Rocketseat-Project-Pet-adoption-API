from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable


class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_person(self, first_name:str, last_name:str, age: int) -> None:
        with self.__db_connection as database:
            try:
                person_data = PeopleTable(first_name=first_name, last_name=last_name, age=age)
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def list_people(self) -> List:
        with self.__db_connection as database:
            try:
                people = database.session.query(PeopleTable).all()
                return people
            except NoResultFound:
                return []
            
    def delete_people(self, first_name: str) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(PeopleTable)
                        .filter(PeopleTable.first_name == first_name)
                        .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            