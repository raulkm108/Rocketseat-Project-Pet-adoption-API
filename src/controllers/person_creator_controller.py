from typing import Dict
import re
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface

class PersonCreatorController:
    def __init__(self,people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age)
        formated_response = self.__format_response(person_info)
        return formated_response

    def __validate_first_and_last_name(self, first_name: str, last_name:str) -> None:
        # Regular expression for characters that are not letters
        non_valid_characters = re.compile(r'[^a-zA-Z]')

        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise Exception("Invalid person name")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int) -> None:
        self.__people_repository.insert_person(first_name, last_name, age)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }
