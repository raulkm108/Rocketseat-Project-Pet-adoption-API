from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController
from src.models.sqlite.entities.people import PeopleTable #pylint: disable=unused-import


class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(name= "Fluffy", type = "Cat"),
            PetsTable(name= "Buddy", type = "Dog")
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "Pets",
            "count": 2,
            "attributes": [
                { "name": "Fluffy", "type": "Cat"},
                { "name": "Buddy", "type": "Dog"}
            ]
        }
    }

    assert response == expected_response