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
  from src.FileOperatin import FileOperation
  from src.MatkulScrapper import InformatikaMatkulScrapper # untuk prodi Informatika
  from src.MatkulScrapper import SistemInformasiMatkulScrapper # Untuk prodi Sistem Informasi

  list_matkul = FileOperation.read("bello.src")

  # Instaniasi MatkulScrapper, gunakan salah satu saja
  matkul_scrapper = InformatikaMatkulScrapper() # prodi Informatika
  matkul_scrapper = SistemInformasiMatkulScrapper() # prodi Sistem Informasi

  # Parsing list_matkul
  parsed_matkul = matkul_scrapper.generate(list_matkul)

  # Digunakan untuk filter matkul semester 3
  filter_matkul = matkul_scrapper.union(matkul_scrapper.getMatkulList(), parsed_matkul)
  ```
- ### ScheduleCreator
  Objek ini yang menjadi interface untuk menggunakan SYNCKRS.
  ```python
  from src.FileOperatin import FileOperation
  from src.MatkulScrapper import InformatikaMatkulScrapper
  from src.MatkulScrapper import SistemInformasiMatkulScrapper
  from src.ScheduleCreator import ScheduleCreator # import ScheduleCreator

  list_matkul = FileOperation.read("bello.src")
  
  matkul_scrapper = InformatikaMatkulScrapper() # prodi Informatika
  matkul_scrapper = SistemInformasiMatkulScrapper() # prodi Sistem Informasi
  
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

  schedule_creator.showChoosed()
  ```

### Memilih Jadwal
Untuk memilih suatu jadwal pastikan sudah mengetahui id jadwal yang akan dipilih. Id jadwal bisa dilihat dengan menampilkan jadwal yang bisa diambil.
```python
...

# Ganti angka 1 dengan id matkul yang akan diambil
schedule_creator(1)
```
Setelah mengambil suatu jadwal, secara otomatis akan mengeliminasi jadwal-jadwal yang bertabrakan ataupun matkul yang telah dipilih. Untuk melihat jadwal-jadwal yang tereliminasi bisa menggunakan schedule_creator.showUnavailable().

