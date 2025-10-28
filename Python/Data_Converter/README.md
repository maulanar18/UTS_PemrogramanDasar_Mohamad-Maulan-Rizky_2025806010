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

# 🔄 Konversi Data Antar Format (C & Python)

Proyek ini menunjukkan **integrasi lintas bahasa (C dan Python)** untuk mengelola data mahasiswa dalam dua format berbeda: **CSV dan JSON**.

---

## 🧩 Fitur Utama

1. **Program C**
   - Input data mahasiswa (nama, NIM, nilai tugas, UTS, UAS)
   - Hitung nilai akhir & huruf mutu
   - Simpan ke file `data_mahasiswa.csv`

2. **Program Python**
   - Membaca `data_mahasiswa.csv`
   - Menampilkan data dengan rapi di terminal
   - Menghitung rata-rata nilai akhir
   - Mengonversi data ke `data_mahasiswa.json`

---

## ⚙️ Teknologi yang Digunakan

- **C Language** → untuk membuat data awal (file CSV)
- **Python 3** → untuk analisis dan konversi ke JSON
- **CSV & JSON Handling**
- **Integrasi Lintas Bahasa**

---

## ▶️ Cara Menjalankan

### **Langkah 1 — Jalankan Program C**
```bash
gcc data_converter.c -o data_converter
./data_converter
```
Masukkan data mahasiswa sesuai instruksi.
Setelah selesai, akan terbentuk file data_mahasiswa.csv.

### **Langkah 2 — Jalankan Program Python**
```bash
python converter.py
```
Program akan:

    - Membaca CSV
    - Menampilkan data dan rata-rata nilai
    - Menyimpan file data_mahasiswa.json

## 📊 Contoh Hasil JSON
```
[
  {"nama": "Rina", "nim": "2310001", "nilai_akhir": 85.5, "mutu": "A"},
  {"nama": "Doni", "nim": "2310002", "nilai_akhir": 61.5, "mutu": "C"}
]
```