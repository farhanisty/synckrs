from src.FileOperation import FileOperation
from src.MatkulScraper import InformatikaMatkulScraper
from src.ScheduleCreator import ScheduleCreator
from src.render.RenderInvoker import RenderInvoker
from src.render.PrettyTableRenderEngine import PrettyTableRenderEngine


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

renderInvoker = RenderInvoker(PrettyTableRenderEngine())

scheduleCreator = ScheduleCreator(hasil)

scheduleCreator.choose(20)
scheduleCreator.choose(165)

renderInvoker.render(scheduleCreator.getAvailable())
