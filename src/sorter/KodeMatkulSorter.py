from .MatkulSorter import MatkulSorter
from src.Matkul import Matkul


class KodeMatkulSorter(MatkulSorter):
    def execute(self, matkuls: list[Matkul], mode="ASC"):
        if mode == "DESC":
            param = True
        else:
            param = False

        matkuls.sort(reverse=param, key=lambda x: x.kode)
