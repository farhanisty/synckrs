class FileOperation:
    @staticmethod
    def read(nama_file: str) -> list[str]:
        nama_file = nama_file

        result = list()

        f = open(nama_file)

        for x in f:
            result.append(x)

        f.close()

        return result
