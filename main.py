from src.FileOperation import FileOperation
from src.MatkulScraper import InformatikaMatkulScraper
from src.MatkulScraper import SistemInformasiMatkulScraper
from src.ScheduleCreator import ScheduleCreator
from src.sorter.DosenSorter import DosenSorter
from src.sorter.MatkulNameSorter import MatkulNameSorter
from src.sorter.IdMatkulSorter import IdMatkulSorter

list_matkul = FileOperation.read("data.src")

matkul_scrapper = InformatikaMatkulScraper()  # prodi Informatika

parsed_matkul = matkul_scrapper.generate(list_matkul)

filter_matkul = matkul_scrapper.union(
    matkul_scrapper.getMatkulList(), parsed_matkul)

schedule_creator = ScheduleCreator(filter_matkul)

schedule_creator.choose(70)
schedule_creator.choose(84)

schedule_creator.showChoosen()

schedule_creator.getRenderInvoker().sort(MatkulNameSorter())
schedule_creator.showAvailable()

schedule_creator.getRenderInvoker().sort(DosenSorter()).changeMode("DESC")
schedule_creator.showUnavailable()
