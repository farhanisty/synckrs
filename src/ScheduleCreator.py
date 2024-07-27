from .Matkul import Matkul
from .DiscontinueIntervalJam import DiscontinueIntervalJam
from prettytable import PrettyTable


class ScheduleCreator:
    def __init__(self, matkuls: list[Matkul]):
        self.matkuls = matkuls
        self.unavailable_matkuls = list()
        self.matkuls_id = list(map(lambda x: x.id, matkuls))
        self.choosed = list[Matkul]()
        self.days = list[DiscontinueIntervalJam]()

        for x in range(0, 6):
            self.days.append(DiscontinueIntervalJam())

    def choose(self, id: int):
        index = self.matkuls_id.index(id)
        matkul = self.matkuls[index]
        self.choosed.append(self.matkuls[index])

        self.removeFromMatkuls(index)

        self.days[self.dayToInt(matkul.jadwal.hari)].add(
            matkul.jadwal.interval
        )

        id = 0
        pop_ids = list[int]()

        for mt in self.matkuls:
            if mt.nama == matkul.nama:
                self.unavailable_matkuls.append(mt)
                pop_ids.append(id)

            if self.days[self.dayToInt(mt.jadwal.hari)].isInRange(mt.jadwal.interval):
                self.unavailable_matkuls.append(mt)
                pop_ids.append(id)

            id += 1

        no = 0
        for pop_id in pop_ids:
            self.removeFromMatkuls(pop_id - no)
            no += 1

    def showAvailable(self):
        self.printTable(self.matkuls)

    def showChoosed(self):
        self.printTable(self.choosed)

    def showUnavailable(self):
        self.printTable(self.unavailable_matkuls)

    def printTable(self, matkuls: list[Matkul]):
        table = PrettyTable(["id", "Matkul", "SKS", "Jadwal", "Dosen"])

        for matkul in matkuls:
            table.add_row([matkul.id, matkul.nama, matkul.sks,
                          matkul.jadwal, matkul.dosen[0]])

        print(table)

    def removeFromMatkuls(self, index):
        self.matkuls.pop(index)
        self.matkuls_id.pop(index)

    def dayToInt(self, day: str) -> int:
        if day == "senin":
            return 0
        elif day == "selasa":
            return 1
        elif day == "rabu":
            return 2
        elif day == "kamis":
            return 3
        elif day == "jumat":
            return 4
        else:
            return 5
