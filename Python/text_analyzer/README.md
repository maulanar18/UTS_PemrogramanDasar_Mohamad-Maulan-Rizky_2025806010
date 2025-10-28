# 🧠 UTS Pemrograman Dasar (C & Python)

## 👤 Identitas
- Nama: Mohamad Maulana Rizky
- NIM: 2025806010
- Kelas: Teknologi Informasi 2
- Dosen: Rintis Mardika Sunarto
- Repository: [\[link GitHub repo\]](https://github.com/maulanar18/UTS_PemrogramanDasar_Mohamad-Maulan-Rizky_2025806010.git)

---

## 📚 Deskripsi
Proyek ini adalah Ujian Tengah Semester (UTS) Pemrograman Dasar, yang menggabungkan konsep C dan Python.  
Mahasiswa diminta membuat beberapa proyek terpisah dengan fitur logika, struktur data, file handling, dan modular programming.

---

# 📊 ANALISIS TEKS OTOMATIS (Python Advanced)

Program **Analisis Teks Otomatis** digunakan untuk menganalisis isi file teks (`.txt`) dan menghasilkan laporan statistik lengkap tentang isi teks tersebut.  
Proyek ini menerapkan konsep **File I/O**, **String Manipulation**, **Dictionary**, **Modularisasi**, dan **Grafik ASCII** di Python.

---

## 🧩 Fitur Utama

1. **Input & Output Otomatis**
   - Input dibaca dari file `input.txt`
   - Hasil analisis disimpan ke file `report.txt`

2. **Analisis yang Dilakukan**
   - Jumlah **baris**
   - Jumlah **kata**
   - **5 kata paling sering muncul**
   - Jumlah **huruf vokal** dan **konsonan**
   - Tampilkan **grafik ASCII** frekuensi kata (visual sederhana di terminal)

3. **Grafik ASCII Contoh**
    ```
    python #########
    program ######
    belajar ###
    ```


4. **Struktur Modular**
- `analyzer.py` → logika analisis teks  
- `utils.py` → fungsi pendukung (pembersihan teks, hitung vokal/konsonan, dll.)

---


---

## ⚙️ Instalasi

1. Pastikan Python 3.8+ telah terinstal.
   ```bash
   python --version
   ```
2. Pastikan file input.txt sudah ada di folder proyek.

3. Tidak memerlukan library eksternal — hanya modul bawaan Python.

## ▶️ Cara Menjalankan Program

1. Letakkan teks yang ingin dianalisis ke dalam file input.txt.
2. Jalankan perintah berikut di terminal:
```bash
python main.py
```
3. Program akan membaca file input.txt, melakukan analisis, lalu menulis hasilnya ke report.txt.
4. Grafik ASCII akan tampil di terminal seperti berikut:
======= HASIL ANALISIS TEKS =======
Jumlah Baris:  12
Jumlah Kata:   156
Huruf Vokal:   480
Huruf Konsonan: 940

====== 5 Kata Teratas ======
python     ##########
program    ######
belajar    ###
analisis   ###
teks       ##

## 🧠 Konsep yang Digunakan

    - File Handling (open, read, write)
    - String Processing (lowercase, split, strip, replace)
    - Dictionary untuk Frekuensi Kata
    - Loop dan Conditional
    - Pembuatan Grafik ASCII (menggunakan # sebagai batang visual)
    - Pemrograman Modular (fungsi & modul terpisah)