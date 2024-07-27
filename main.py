from src.FileOperation import FileOperation
from src.MatkulScraper import InformatikaMatkulScraper
from src.ScheduleCreator import ScheduleCreator
from src.sorter.DosenSorter import DosenSorter
from src.sorter.MatkulNameSorter import MatkulNameSorter
from src.sorter.IdMatkulSorter import IdMatkulSorter
from src.cluster.DosenMatkulCluster import DosenMatkulCluster

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


scheduleCreator = ScheduleCreator(hasil)

scheduleCreator.choose(23)
scheduleCreator.choose(34)
scheduleCreator.choose(111)

scheduleCreator.getRenderInvoker().sort(IdMatkulSorter())
scheduleCreator.showChoosen()

scheduleCreator.showUnavailable()
# scheduleCreator.getRenderInvoker().sort(DosenSorter()).changeMode("DESC")
# scheduleCreator.showAvailable()
#
# scheduleCreator.getRenderInvoker().sort(IdMatkulSorter()).changeMode("ASC")
# scheduleCreator.showAvailable()
