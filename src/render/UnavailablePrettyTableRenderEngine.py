from .RenderEngine import RenderEngine
from src.Matkul import Matkul
from prettytable import PrettyTable


class UnavailablePrettyTableRenderEngine(RenderEngine):
    def render(self, matkuls: list[Matkul]):
        table = PrettyTable(
            ["id", "Matkul", "SKS", "Jadwal", "Dosen", "Alasan"])

        for matkul in matkuls:
            table.add_row([matkul.id, matkul.nama, matkul.sks,
                          matkul.jadwal, matkul.dosen[0],
                           matkul.formatReason()])

        print(table)
