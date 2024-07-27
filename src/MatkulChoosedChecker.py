from .AvailibilityChecker import AvailibilityChecker
from .Matkul import Matkul


class MatkulChoosedChecker(AvailibilityChecker):
    def __init__(self):
        super().__init__()

    def check(self, paramMatkul: Matkul, checkMatkul: Matkul, reason=[]):
        if paramMatkul.nama == checkMatkul.nama:
            reason.append(
                f"Matkul {paramMatkul.nama} sudah diambil(ID {paramMatkul.id})")
        return super().check(paramMatkul, checkMatkul, reason)
