class Jam:
    def __init__(self, jam, menit):
        self.jam = jam
        self.menit = menit

    @staticmethod
    def buildFromString(x: str):
        res = x.split(":")
        return Jam(res[0], res[1])
