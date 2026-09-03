from abc import ABC, abstractmethod
from src.models.sqlite.entities.people import PeopleTable
from typing import List

class PeopleRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, first_name:str, last_name:str, age: int) -> None:
        pass

    @abstractmethod
    def list_person(self, first_name:str) -> PeopleTable:
        pass

    @abstractmethod
    def list_people(self) -> List:
        pass

    @abstractmethod
    def delete_person(self, first_name: str) -> None:
        pass