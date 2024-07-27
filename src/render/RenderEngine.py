from abc import ABC, abstractmethod
from src.Matkul import Matkul


class RenderEngine(ABC):
    @abstractmethod
    def render(self, matkuls: list[Matkul]):
        pass
