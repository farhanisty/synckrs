from src.FileOperation import FileOperation
from src.MatkulScraper import InformatikaMatkulScraper

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

scrapper = InformatikaMatkulScraper()
hasil = scrapper.union(listMatkulSem, scrapper.generate(
    FileOperation.read("data.src"))
)


# Jadwal.buildFromString(hasil[0].jadwal)

# id = 1
# for matkul in hasil:
#     print(f"{id}, {matkul.nama}, {matkul.jadwal}, {matkul.dosen}")
#     id += 1
