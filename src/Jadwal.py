from .Jam import Jam
from .IntervalJam import IntervalJam


class Jadwal:
    def __init__(self, hari: str, interval: IntervalJam):
        self.hari = hari.lower().strip()
        self.interval = interval

    def __str__(self):
        return self.hari + " " + str(self.interval)

    @staticmethod
    def buildFromString(x: str):
        jadwal = x.split(" ")
        jam = jadwal[1].split("-")

        return Jadwal(
            jadwal[0], IntervalJam(Jam.buildFromString(
                jam[0]), Jam.buildFromString(jam[1]))
        )
