import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository


db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Interation with the db")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print()
    print(response)

@pytest.mark.skip(reason="Interation with the db")
def test_delete_pet():
    name = "belinha"
    repo = PetsRepository(db_connection_handler)
    repo.delete_pets(name)
    
@pytest.mark.skip(reason="Interation with the db")
def test_insert_person():
    first_name = "test first name"
    last_name = "test last name" 
    age = 77

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age)