from typing import Dict
from src.models.sqlite.interfaces.people_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable
from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface

class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self,people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        response = self.__format_reponse(person)
        return response

    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self.__people_repository.list_person(person_id)
        if not person:
            raise Exception("Person not found")

        return person

    def __format_reponse(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "Count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "age": person.age,
                    "pets": [
                        {
                        "name": pet.name,
                        "type": pet.type
                        }
                        for pet in person.pets
                
                    ]
                }
            }
        }