from .Jam import Jam


class Jadwal:
    def __init__(self, hari, awal, akhir):
        self.hari = hari
        self.awal = awal
        self.akhir = akhir

    @staticmethod
    def buildFromString(x: str):
        jadwal = x.split(" ")
        jam = jadwal[1].split("-")

        return Jadwal(
            jadwal[0], Jam.buildFromString(jam[0]),
            Jam.buildFromString(jam[1])
        )
