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
# 🧑‍🎓 Sistem Manajemen Data Mahasiswa (Python + Linked List) — Versi Upgrade

Program ini adalah implementasi **manajemen data mahasiswa menggunakan Linked List** di Python.  
Versi ini sudah **ditingkatkan** dengan fitur tambahan seperti update data, sorting, dan ekspor ke JSON — tanpa menghapus fungsi dasar.

Program ini cocok untuk pembelajaran:

- Struktur data **Linked List**
- **CRUD** data (Create, Read, Update, Delete)
- **File handling** CSV & JSON
- Sorting dan searching data
- Validasi input

---

## ✅ Fitur Program

| Fitur | Deskripsi |
|------|-----------|
| Tambah data mahasiswa | Input nama, NIM, nilai (Tugas, UTS, UAS) |
| Hitung nilai akhir | Rumus: `0.3*Tugas + 0.3*UTS + 0.4*UAS` |
| Konversi huruf mutu | Berdasarkan nilai akhir (A – E) |
| Tampilkan seluruh data | Format tabel rapi di terminal |
| Cari mahasiswa | Berdasarkan NIM |
| Hapus data mahasiswa | Menghapus node dari linked list |
| **Update data mahasiswa** | Edit nama dan nilai |
| **Sorting data** | Berdasarkan Nama / NIM / Nilai akhir |
| Simpan ke CSV | File: `data_mahasiswa.csv` |
| **Export ke JSON** | File: `data_mahasiswa.json` |
| **Auto-load data** | Data CSV otomatis dimuat saat startup |
| Validasi input angka | Cegah error input nilai |

---

## 📂 Struktur Data dalam Linked List

Setiap node mahasiswa menyimpan:
```
Nama | NIM | Tugas | UTS | UAS | Nilai Akhir | Mutu | Pointer next
```

---

## 📥 Instalasi

Pastikan Python sudah terinstal:

```bash
python --version
```
---
## ▶️ Cara Menjalankan Program

- Simpan file sebagai sistem_data.py
- Jalankan melalui terminal/CMD:

```bash
python sistem_data.py
```
## 🧾 Menu Program

Saat dijalankan, program menampilkan:
```
===== MENU MANAJEMEN DATA MAHASISWA =====
1. Tambah Data Mahasiswa
2. Tampilkan Semua Data
3. Cari Mahasiswa berdasarkan NIM
4. Hapus Mahasiswa
5. Update Data Mahasiswa
6. Sort Data Mahasiswa
7. Simpan ke File CSV
8. Export ke JSON
0. Keluar
==========================================
```
## 📊 Contoh Output CSV 
```csv
Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu
Rina,2310001,80,85,90,85.50,A
Doni,2310002,60,55,70,61.50,C
```
## 📦 Contoh Output JSON
```json
[
  {
    "nama": "Rina",
    "nim": "2310001",
    "tugas": 80,
    "uts": 85,
    "uas": 90,
    "nilai": 85.5,
    "mutu": "A"
  }
]
```
