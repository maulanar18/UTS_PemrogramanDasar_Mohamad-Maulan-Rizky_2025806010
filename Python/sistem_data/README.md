# 🧠 UTS Pemrograman Dasar (C & Python)

## 👤 Identitas
- Nama: Mohamad Maulana Rizky
- NIM: 2025806010
- Kelas: Teknologi Informasi 2
- Dosen: Rintis Mardika Sunarto
- Repository: [link GitHub repo]

---

## 📚 Deskripsi
Proyek ini adalah Ujian Tengah Semester (UTS) Pemrograman Dasar, yang menggabungkan konsep C dan Python.  
Mahasiswa diminta membuat beberapa proyek terpisah dengan fitur logika, struktur data, file handling, dan modular programming.

---
# 🧑‍🎓 Program Manajemen Data Mahasiswa (Linked List Python)

Program ini merupakan implementasi **Manajemen Data Mahasiswa** menggunakan **Linked List Dinamis** di Python.  
Fitur ini dirancang untuk mengelola data mahasiswa dengan operasi **CRUD sederhana** (Create, Read, Delete), menghitung nilai akhir, huruf mutu, serta menyimpan hasilnya ke file CSV.

---

## ⚙️ Fitur Program

| No | Fitur | Deskripsi |
|----|--------|------------|
| 1 | **Tambah Data Mahasiswa** | Memasukkan data baru (nama, NIM, nilai tugas, UTS, UAS) ke dalam linked list. |
| 2 | **Hitung Nilai Akhir** | Nilai akhir dihitung otomatis: `0.3*Tugas + 0.3*UTS + 0.4*UAS`. |
| 3 | **Konversi Huruf Mutu** | Menentukan huruf mutu berdasarkan nilai akhir: A–E. |
| 4 | **Tampilkan Semua Data** | Menampilkan tabel seluruh data mahasiswa di terminal. |
| 5 | **Cari Mahasiswa** | Mencari mahasiswa berdasarkan NIM. |
| 6 | **Hapus Mahasiswa** | Menghapus data mahasiswa dari linked list dan membebaskan node. |
| 7 | **Simpan ke File CSV** | Menyimpan seluruh data ke file `data_mahasiswa.csv` secara otomatis. |

---

## 📄 Contoh Format File CSV

File `data_mahasiswa.csv` akan tersimpan secara otomatis setelah kamu menyimpan atau keluar dari program.

```csv
Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu
Rina,2310001,80,85,90,85.50,A
Doni,2310002,60,55,70,61.50,C
```

# 🖥️ Cara Menjalankan Program
## 1️⃣ Instalasi Python

Pastikan Python sudah terinstal di sistem kamu.
Cek dengan:
```bash
python --version
```
Jika belum, unduh dari python.org/downloads

Saat instalasi, centang opsi “Add Python to PATH”.

## 2️⃣ Jalankan Program

Masuk ke folder tempat file disimpan, lalu jalankan di terminal:
```bash
python sistem_data.py
```
## 3️⃣ Gunakan Menu Utama

Setelah dijalankan, program akan menampilkan menu seperti berikut:
```
===== MENU MANAJEMEN DATA MAHASISWA =====
1. Tambah Data Mahasiswa
2. Tampilkan Semua Data
3. Cari Mahasiswa (berdasarkan NIM)
4. Hapus Mahasiswa (berdasarkan NIM)
5. Simpan ke File CSV
0. Keluar
==========================================
```
## 4️⃣ File Output

Setelah memilih opsi 5 atau keluar (0), data akan otomatis disimpan ke file:
```bash
data_mahasiswa.csv
```
# 🧰 Teknologi yang Digunakan

Bahasa: Python 3

Struktur data: Linked List (Node & Pointer)

File handling: CSV (Comma-Separated Values)
