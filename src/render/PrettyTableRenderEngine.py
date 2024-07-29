from .RenderEngine import RenderEngine
from src.Matkul import Matkul
from prettytable import PrettyTable


class PrettyTableRenderEngine(RenderEngine):
    def render(self, matkuls: list[Matkul]):
        table = PrettyTable(
            ["id", "Kode Matkul", "Matkul", "SKS", "Kelas", "Jadwal", "Dosen"])

        for matkul in matkuls:
            table.add_row([matkul.id, matkul.kode, matkul.nama, matkul.sks,
                           matkul.kelas, matkul.jadwal, matkul.dosen[0]])

        print(table)
