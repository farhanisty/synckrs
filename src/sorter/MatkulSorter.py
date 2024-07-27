from abc import ABC, abstractmethod
from src.Matkul import Matkul


class MatkulSorter(ABC):
    @abstractmethod
    def execute(self, matkuls: list[Matkul], mode="ASC"):
        pass
