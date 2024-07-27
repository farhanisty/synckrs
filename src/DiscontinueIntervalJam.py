from .IntervalJam import IntervalJam


class DiscontinueIntervalJam:
    def __init__(self):
        self.intervals = list[IntervalJam]()

    def add(self, interval: IntervalJam):
        self.intervals.append(interval)

    def isInRange(self, intervalParam: IntervalJam):
        for interval in self.intervals:
            if interval.isInRange(intervalParam):
                return True

        return False
