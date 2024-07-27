from .Jam import Jam


class IntervalJam:
    @staticmethod
    def buildFromMid(jam: Jam):
        return IntervalJam(Jam(0, 0), jam)

    @staticmethod
    def buildInTime(jam: Jam):
        return IntervalJam(jam, jam)

    def __init__(self, start: Jam, end: Jam):
        self.start = start
        self.end = end

    def __str__(self):
        return str(self.start) + "-" + str(self.end)

    def isInRange(self, interval) -> bool:

        if self.start.inMinute() < interval.start.inMinute():
            low = interval.start.inMinute() - self.start.inMinute()
            high = self.end.inMinute() - self.start.inMinute()
        else:
            low = self.start.inMinute() - interval.start.inMinute()
            high = interval.end.inMinute() - interval.start.inMinute()

        if low < high:
            return True

        return False

        return False
