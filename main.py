from src.FileOperation import FileOperation
from src.MatkulScraper import InformatikaMatkulScraper
from src.MatkulScraper import SistemInformasiMatkulScraper
from src.ScheduleCreator import ScheduleCreator
from src.sorter.DosenSorter import DosenSorter
from src.sorter.MatkulNameSorter import MatkulNameSorter
from src.sorter.IdMatkulSorter import IdMatkulSorter


scrapper = SistemInformasiMatkulScraper()
hasil = scrapper.union(scrapper.getMatkulList(), scrapper.generate(
    FileOperation.read("matkulsi.src"))
)

scheduleCreator = ScheduleCreator(hasil)

scheduleCreator.showAvailable()

# scheduleCreator.choose(70)
# scheduleCreator.choose(47)
# scheduleCreator.choose(34)
# scheduleCreator.choose(84)
# scheduleCreator.choose(104)
# scheduleCreator.choose(156)
# scheduleCreator.choose(126)
# scheduleCreator.choose(141)
# scheduleCreator.choose(111)
# scheduleCreator.choose(124)
# scheduleCreator.choose(173)
# scheduleCreator.choose(147)
# # scheduleCreator.choose(23)
# # scheduleCreator.choose(48)
#
# scheduleCreator.getRenderInvoker().sort(IdMatkulSorter())
# scheduleCreator.showChoosen()
#
# # scheduleCreator.showUnavailable()
# # scheduleCreator.getRenderInvoker().sort(MatkulNameSorter())
# # scheduleCreator.showAvailable()
#
# scheduleCreator.getRenderInvoker().sort(MatkulNameSorter())
# scheduleCreator.showUnavailable()
# #
# # scheduleCreator.getRenderInvoker().sort(IdMatkulSorter()).changeMode("ASC")
# # scheduleCreator.showAvailable()
