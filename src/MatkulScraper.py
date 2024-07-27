import re
from abc import ABC, abstractmethod
from .Matkul import Matkul
from .Jadwal import Jadwal


class MatkulScraper(ABC):
    @abstractmethod
    def generate(self, list_string: list[str]) -> list[Matkul]:
        pass

    def union(self, list_in: list[str], list_matkuls: list[Matkul]) -> list[Matkul]:
        return list(filter(lambda x: x.nama.strip()
                           in list_in, list_matkuls))


class InformatikaMatkulScraper(MatkulScraper):
    def generate(self, list_string: list[str]) -> list[Matkul]:
        result = list[Matkul]()

        idx = 1
        for x in list_string:
            if x == "\n":
                continue

            if not re.search("^INFORMATIKA", x):
                result[-1].dosen.append(x.strip())
                continue

            matkul = re.split("\t", x)

            res = Matkul(idx, matkul[0], matkul[1], matkul[2], matkul[3],
                         matkul[4], matkul[5],
                         Jadwal.buildFromString(matkul[6]), matkul[7])

            idx += 1
            result.append(res)

        return result
