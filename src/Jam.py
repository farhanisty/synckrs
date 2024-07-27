class Jam:
    def __init__(self, jam: int, menit: int):
        self.jam = int(jam)
        self.menit = int(menit)

    def inMinute(self) -> int:
        return (self.jam * 60) + self.menit

    def __str__(self):
        jam = str(self.jam)
        menit = str(self.menit)

        if self.jam < 10:
            jam = "0" + jam

        if self.menit < 10:
            menit = "0" + menit

        return jam + ":" + menit

    @staticmethod
    def buildFromString(x: str):
        res = x.split(":")
        return Jam(res[0], res[1])
