import re

listMatkulSem = [
    "Bahasa Indonesia",
    "Struktur Data",
    "Komputer dan Masyarakat",
    "Komputasi Numerik",
    "Interaksi Manusia dan Komputer",
    "Sistem Digital",
    "Geoinformatika",
    "Pemrograman Web",
    "Praktikum Implementasi Struktur Data",
    "Praktikum Pemrograman Web",
    "Bela Negara dan Widya Mwat Yasa",
    "Riset Operasi",
]


class Jam:
    def __init__(self, jam, menit):
        self.jam = jam
        self.menit = menit

    @staticmethod
    def buildFromString(x):
        res = x.split(":")
        return Jam(res[0], res[1])


class Jadwal:
    def __init__(self, hari, awal, akhir):
        self.hari = hari
        self.awal = awal
        self.akhir = akhir

    @staticmethod
    def buildFromString(x):
        jadwal = x.split(" ")
        jam = jadwal[1].split("-")

        return Jadwal(
            jadwal[0], Jam.buildFromString(jam[0]),
            Jam.buildFromString(jam[1])
        )


class Matkul:
    def __init__(self, prodi, kode, nama, sks, kelas, jml_mahasiswa, jadwal, ruangan):
        self.prodi = prodi
        self.kode = kode
        self.nama = nama
        self.sks = sks
        self.kelas = kelas
        self.jml_mahasiswa = jml_mahasiswa
        self.jadwal = jadwal
        self.ruangan = ruangan
        self.dosen = list()


f = open("data.src")

matkuls = list()

number = 0
for x in f:
    if x == "\n":
        continue

    if not re.search("^INFORMATIKA", x):
        matkuls[-1].dosen.append(x.strip())
        continue

    matkul = re.split("\t", x)

    result = Matkul(matkul[0], matkul[1], matkul[2], matkul[3],
                    matkul[4], matkul[5],
                    Jadwal.buildFromString(matkul[6]), matkul[7])

    matkuls.append(result)

hasil = list(filter(lambda x: x.nama.strip() in listMatkulSem, matkuls))

# Jadwal.buildFromString(hasil[0].jadwal)

# id = 1
# for matkul in hasil:
#     print(f"{id}, {matkul.nama}, {matkul.jadwal}, {matkul.dosen}")
#     id += 1

f.close()
