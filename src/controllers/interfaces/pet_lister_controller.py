from abc import ABC, abstractmethod
from typing import Dict


class PetListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass