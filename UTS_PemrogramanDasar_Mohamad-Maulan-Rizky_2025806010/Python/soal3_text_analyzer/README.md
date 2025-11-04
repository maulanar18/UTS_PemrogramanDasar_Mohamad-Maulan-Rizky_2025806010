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

# 📊 ANALISIS TEKS OTOMATIS — Versi Upgrade

Program **Analisis Teks Otomatis** digunakan untuk menganalisis isi file `.txt` dan menghasilkan laporan statistik lengkap.  
Versi ini telah **ditingkatkan** dengan fitur pencarian kata, analisis kalimat, dan ekspor hasil ke file JSON, tanpa menghilangkan fitur sebelumnya.

---

## 🧩 Fitur Awal

| Fitur | Deskripsi |
|------|-----------|
Input otomatis | Membaca text dari `input.txt`
Output otomatis | Menulis hasil analisis ke `report.txt`
Hitung baris | Menghitung total baris teks
Hitung kata | Menghitung total kata
5 kata paling sering | Menampilkan lima kata dengan frekuensi tertinggi
Analisis huruf | Menghitung jumlah vokal dan konsonan
Grafik ASCII | Menampilkan grafik frekuensi kata
Modular | File `analyzer.py` dan `utils.py`
Cari kata dalam teks | User dapat memasukkan kata untuk dicek frekuensinya
Hitung jumlah kalimat | Menampilkan total kalimat dalam teks
Panjang rata-rata kata | Menghitung rata-rata jumlah huruf per kata
Panjang rata-rata kalimat | Menghitung rata-rata jumlah kata per kalimat
Ekspor JSON | Menyimpan hasil analisis ke `report.json`
Ignore stopwords* | Mengabaikan kata umum seperti "dan", "yang", "di" (opsional)

> *Stopwords disimpan di file terpisah `stopwords.txt` dan dapat dimodifikasi.


---

## 🧾 Contoh Output Terminal

```
======= HASIL ANALISIS TEKS =======
Jumlah Baris : 12
Jumlah Kata : 156
Jumlah Kalimat : 18
Rata Kata / Kalimat : 8.7
Rata Huruf / Kata : 5.1
Huruf Vokal : 480
Huruf Konsonan : 940

====== 5 Kata Teratas ======
python ##########
program ######
belajar ###
analisis ###
teks ##

Cari kata: python
Frekuensi: 5 kali
```

---

## 📦 Contoh Output JSON

```json
{
  "lines": 12,
  "words": 156,
  "sentences": 18,
  "avg_words_per_sentence": 8.7,
  "avg_chars_per_word": 5.1,
  "vowels": 480,
  "consonants": 940,
  "top_words": {
    "python": 10,
    "program": 6
  }
}
```
---
## ⚙️ Cara Menjalankan Program
```bash
python main.py
```