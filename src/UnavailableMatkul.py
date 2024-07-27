from .Matkul import Matkul


class UnavailableMatkul(Matkul):
    @staticmethod
    def cast(matkul: Matkul):
        newObj = UnavailableMatkul(
            matkul.id,
            matkul.prodi,
            matkul.kode,
            matkul.nama,
            matkul.sks,
            matkul.kelas,
            matkul.jml_mahasiswa,
            matkul.jadwal,
            matkul.ruangan
        )

        newObj.dosen = matkul.dosen

        return newObj

    def __init__(self, id, prodi, kode, nama, sks, kelas, jml_mahasiswa, jadwal, ruangan):
        super().__init__(id, prodi, kode, nama, sks, kelas, jml_mahasiswa, jadwal, ruangan)
        self.reason = list[str]()

    def addReason(self, reason: str):
        self.reason.add(reason)

    def formatReason(self):
        return ", ".join(self.reason)
