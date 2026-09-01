from abc import ABC, abstractmethod
from typing import List
from src.models.sqlite.entities.pets import PetsTable

class PetsRepositoryInterface(ABC):

    @abstractmethod
    def create_pet(self, name: str, type: str, owner_id:int | None = None) -> None:
        pass

    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def delete_pets(self, name: str) -> None:
        pass