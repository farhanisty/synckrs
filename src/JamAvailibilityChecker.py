from .Matkul import Matkul
from .AvailibilityChecker import AvailibilityChecker
from .DiscontinueIntervalJam import DiscontinueIntervalJam


class JamAvailibilityChecker(AvailibilityChecker):
    def __init__(self, discontinueIntervalJam: DiscontinueIntervalJam):
        self.discontinueIntervalJam = discontinueIntervalJam
        super().__init__()

    def check(self, paramMatkul: Matkul, checkMatkul: Matkul, reason=[]):
        if self.discontinueIntervalJam.isInRange(checkMatkul.jadwal.interval):
            reason.append(
                f"Jadwal bertabrakan dengan {paramMatkul.nama} ({str(paramMatkul.jadwal)})")

        return super().check(paramMatkul, checkMatkul, reason)
