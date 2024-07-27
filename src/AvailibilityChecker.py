from .Matkul import Matkul


class AvailibilityChecker:
    def __init__(self):
        self.nextChecker = None

    def setNext(self, nextChecker):
        self.nextChecker = nextChecker

    def check(self, paramMatkul: Matkul, checkMatkul: Matkul, reason=[]):
        if self.nextChecker:
            return self.nextChecker.check(paramMatkul, checkMatkul, reason)
        return reason
