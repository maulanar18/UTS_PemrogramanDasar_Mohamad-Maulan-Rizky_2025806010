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

Proyek ini menunjukkan integrasi antara bahasa **C** dan **Python** untuk pengolahan data mahasiswa dalam format **CSV** dan **JSON**, serta penambahan fitur **ranking mahasiswa** berdasarkan nilai akhir.

---

## 📌 Fitur Utama

| Fitur | Bahasa | Status |
|---|---|---|
- Input data mahasiswa & simpan ke CSV 
- Hitung nilai akhir & huruf mutu 
- Baca CSV & tampilkan data 
- Hitung rata-rata nilai akhir 
- Konversi ke JSON 
- Urutkan data (ranking)
- Simpan CSV versi ranking
---

## ▶️ Cara Menjalankan

### 1️. Menjalankan Program C
```bash
gcc data_converter.c -o data_converter
./data_converter
```
Output: data_mahasiswa.csv terbentuk
### 2️. Menjalankan Program Python
```bash
python converter.py
```
**Program Python akan:**

- Membaca file CSV
- Menampilkan data mahasiswa
- Menampilkan nilai rata-rata
- Menampilkan peringkat mahasiswa
- Membuat data_mahasiswa.json
- Membuat data_mahasiswa_ranked.csv

## 📊 Contoh Output Ranking
```
=== PERINGKAT MAHASISWA ===
1. Rina       | 85.50 | A
2. Doni       | 61.50 | C
```

```json
[
  { "nama": "Rina", "nim": "2310001", "nilai_akhir": 85.5, "mutu": "A" },
  { "nama": "Doni", "nim": "2310002", "nilai_akhir": 61.5, "mutu": "C" }
]
```
