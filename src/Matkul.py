class Matkul:
    def __init__(self, id, prodi, kode, nama, sks, kelas, jml_mahasiswa, jadwal, ruangan):
        self.id = id
        self.prodi = prodi
        self.kode = kode
        self.nama = nama
        self.sks = sks
        self.kelas = kelas
        self.jml_mahasiswa = jml_mahasiswa
        self.jadwal = jadwal
        self.ruangan = ruangan
        self.dosen = list()
