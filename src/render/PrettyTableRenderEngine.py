from .RenderEngine import RenderEngine
from src.Matkul import Matkul
from prettytable import PrettyTable


class PrettyTableRenderEngine(RenderEngine):
    def render(self, matkuls: list[Matkul]):
        table = PrettyTable(
            ["id", "Matkul", "SKS", "Kelas", "Jadwal", "Dosen"])

        for matkul in matkuls:
            table.add_row([matkul.id, matkul.nama, matkul.sks,
                           matkul.kelas, matkul.jadwal, matkul.dosen[0]])

        print(table)
