import re
from abc import ABC, abstractmethod
from .Matkul import Matkul
from .Jadwal import Jadwal


class MatkulScraper(ABC):
    @abstractmethod
    def generate(self, list_string: list[str]) -> list[Matkul]:
        pass

    @abstractmethod
    def getMatkulList(self):
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

            if matkul[4].upper().strip() == "IF-H":
                continue

            res = Matkul(idx, matkul[0], matkul[1], matkul[2], matkul[3],
                         matkul[4], matkul[5],
                         Jadwal.buildFromString(matkul[6]), matkul[7])

            idx += 1
            result.append(res)

        return result

    def getMatkulList(self):
        return [
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


class SistemInformasiMatkulScraper(MatkulScraper):
    def generate(self, list_string: list[str]) -> list[Matkul]:
        result = list[Matkul]()

        idx = 1
        for x in list_string:
            if x == "\n":
                continue

            if not re.search("^SISTEM INFORMASI", x):
                result[-1].dosen.append(x.strip())
                continue

            matkul = re.split("\t", x)

            res = Matkul(idx, matkul[0], matkul[1], matkul[2], matkul[3],
                         matkul[4], matkul[5],
                         Jadwal.buildFromString(matkul[6]), matkul[7])

            idx += 1
            result.append(res)

        return result

    def getMatkulList(self):
        return [
            "Perencanaan Strategis TI",
            "Rekayasa Kebutuhan Perangkat Lunak",
            "Sistem Pendukung Keputusan",
            "Keamanan Aset Informasi",
            "Desain & Manajemen Jaringan Komputer",
            "Metode Survey dan Pengolahan Data",
            "Interaksi Manusia & Komputer",
            "Kapita Selekta",
            "Sistem Informasi Manajemen Bencana",
            "Praktikum Desain & Manajemen Jaringan Komputer",
            "Praktikum Rekayasa Kebutuhan Perangkat Lunak",
            "Etika Profesi TI",
        ]
