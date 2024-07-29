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
FItur render planning memerluka package prettytable.
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
git clonse https://gthub.com/farhanisty/synckrs.git
```
