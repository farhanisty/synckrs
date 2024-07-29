# SYNCKRS
Aplikasi untuk mempermudah perencanaan krs.
## Fitur-Fitur
- Baca jadwal otomatis dari BIMA
- Auto menyembunyikan jadwal jika suatu matkul sudah diambil atau jadwal bertabrakan dengan jadwal lain yang telah diambil
- Multiplanning
- Sort jadwal
- Render planning berbasis cli
## Requirement
- Python versi 3 ke atas
- Pip
- Git
## Installasi
### PIP
#### WIndows
Pada sistem operasi windows, pip akan otomatis terinstall jika sudah menginstall python.
#### Linux
Berbeda denan windows, untuk sistem operasi berbasis linux python versi 3 menggunakan pip3. Di beberapa distro linux tidak mengincludekan pip3 sebagai package bawaan.
```shell
sudo apt install python3-pip
```
### Prettytable
FItur render plan memerlukan package prettytable.
#### Windows
```shell
pip install prettytable
```
#### Linux
```shell
pip3 install prettytable
```
### SYNCKRS
Clone repository SYNCKRS.
```shell
git clone https://github.com/farhanisty/synckrs.git
```
## Run
### Windows
```shell
python main.py
```
### Linux
```shell
python3 main.py
```
## Dokumentasi
- ### FileOperation
  Objek ini digunakan untuk membaca file *.src lalu dirubah menjadi python list dengan menggunakan _read_ method. Method tersebut bersifat static yang artinya tidak perlu melakukan instansiasi terlebih dahulu.
  ```python
  # import FileOperation class
  from src.FileOperation import FileOperation

  # method ini memerlukan sebuah parameter nama file yang akan dibaca
  list_matkul = FileOperation.read("bello.src")
  ```
- ### MatkulScrapper
  Objek ini bertanggung jawab untuk parsing hasil list_matkul.
  ```python
  from src.FileOperation import FileOperation
  from src.MatkulScraper import InformatikaMatkulScraper # untuk prodi Informatika
  from src.MatkulScraper import SistemInformasiMatkulScraper # Untuk prodi Sistem Informasi

  list_matkul = FileOperation.read("bello.src")

  # Instaniasi MatkulScrapper, gunakan salah satu saja
  matkul_scrapper = InformatikaMatkulScraper() # prodi Informatika
  matkul_scrapper = SistemInformasiMatkulScraper() # prodi Sistem Informasi

  # Parsing list_matkul
  parsed_matkul = matkul_scrapper.generate(list_matkul)

  # Digunakan untuk filter matkul semester 3
  filter_matkul = matkul_scrapper.union(matkul_scrapper.getMatkulList(), parsed_matkul)
  ```
- ### ScheduleCreator
  Objek ini yang menjadi interface untuk menggunakan SYNCKRS.
  ```python
  from src.FileOperation import FileOperation
  from src.MatkulScraper import InformatikaMatkulScraper
  from src.MatkulScraper import SistemInformasiMatkulScraper
  from src.ScheduleCreator import ScheduleCreator # import ScheduleCreator

  list_matkul = FileOperation.read("bello.src")
  
  matkul_scrapper = InformatikaMatkulScraper() # prodi Informatika
  matkul_scrapper = SistemInformasiMatkulScraper() # prodi Sistem Informasi
  
  parsed_matkul = matkul_scrapper.generate(list_matkul)

  filter_matkul = matkul_scrapper.union(matkul_scrapper.getMatkulList(), parsed_matkul)

  # Instansiasi ScheduleCreator
  schedule_creator = ScheduleCreator(filter_matkul)
  ```

### Menampilkan Jadwal
Terdapat tiga opsi untuk menampilkan jadwal:
- Jadwal yang bisa diambil
  ```python
  ...
  
  schedule_creator.showAvailable()
  ```
- Jadwal yang tidak bisa diambil
  ```python
  ...

  schedule_creator.showUnavailable()
  ```
- Jadwal yang sudah dipilih
  ```python
  ...

  schedule_creator.showChoosen()
  ```

### Memilih Jadwal
Untuk memilih suatu jadwal pastikan sudah mengetahui id jadwal yang akan dipilih. Id jadwal bisa dilihat dengan menampilkan jadwal yang bisa diambil.
```python
...

# Ganti angka 1 dengan id matkul yang akan diambil
schedule_creator.choose(1)
```
Setelah mengambil suatu jadwal, secara otomatis akan mengeliminasi jadwal-jadwal yang bertabrakan ataupun matkul yang telah dipilih. Untuk melihat jadwal-jadwal yang tereliminasi bisa menggunakan schedule_creator.showUnavailable().

### Sort
```python
...

from src.sorter.DosenSorter import DosenSorter # sort berdasarkan nama dosen
from src.sorter.MatkulNameSorter import MatkulNameSorter # sort berdasarkan nama matkul
from src.sorter.IdMatkulSorter import IdMatkulSorter # sort berdasarkan id matkul/hari

...

# tuliskan sebelum menampilkan jadwal
schedule_creator.getRenderInvoker().sort(DosenSorter()) # DosenSorter bisa diganti dengan ketiga objek sorter di atas
schedule_creator.showAvailable()
```

#### Mode
Terdapat dua buah mode sort, yaitu ASC dan DESC. Secara otomatis, perintah di atas akan mensortir dengan mode ASC(dari kecil ke besar). Untuk merubah menjadi mode DESC:
```python
...

schedule_creator.getRenderInvoker().sort(MatkulNameSorter()).changeMode("DESC")

...
```

### Contoh

```python
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

```
