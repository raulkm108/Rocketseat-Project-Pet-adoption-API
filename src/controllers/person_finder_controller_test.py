#pylint: disable=unused-argument
from .person_finder_controller import PersonFinderController

class MockPerson():
    def __init__(self, first_name, last_name, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class MockPeopleRepository:
    def list_person(self, person_id: int):
        return MockPerson(
            first_name = "John",
            last_name = "Doe",
            age= 35
        )

def test_find():
    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(1)

    expected_reponse = {
        "data": {
            "type": "Person",
            "Count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "age": 35
            }
        }
    }

    assert response == expected_reponse