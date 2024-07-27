from src.FileOperation import FileOperation
from src.MatkulScraper import InformatikaMatkulScraper
from src.ScheduleCreator import ScheduleCreator
from src.Jam import Jam
from src.IntervalJam import IntervalJam
from src.DiscontinueIntervalJam import DiscontinueIntervalJam

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

# satu = IntervalJam(Jam(7, 30), Jam(10, 0))
# print(satu.isInRange(IntervalJam(Jam(10, 0), Jam(11, 45))))
scrapper = InformatikaMatkulScraper()
hasil = scrapper.union(listMatkulSem, scrapper.generate(
    FileOperation.read("data.src"))
)

scheduleCreator = ScheduleCreator(hasil)

scheduleCreator.choose(20)
scheduleCreator.choose(165)

scheduleCreator.showChoosed()
scheduleCreator.showAvailable()
scheduleCreator.showUnavailable()
