from .Matkul import Matkul
from prettytable import PrettyTable


class ScheduleCreator:
    def __init__(self, matkuls: list[Matkul]):
        self.matkuls = matkuls
        self.matkuls_id = list(map(lambda x: x.id, matkuls))
        self.choosed = list[Matkul]()

    def choose(self, id: int):
        index = self.matkuls_id.index(id)
        self.choosed.append(self.matkuls[index])
        self.matkuls.pop(index)

    def showAvailable(self):
        table = PrettyTable(["id", "Matkul", "SKS", "Jadwal", "Dosen"])

        for matkul in self.matkuls:
            table.add_row([matkul.id, matkul.nama, matkul.sks,
                          matkul.jadwal, matkul.dosen[0]])

        print(table)
