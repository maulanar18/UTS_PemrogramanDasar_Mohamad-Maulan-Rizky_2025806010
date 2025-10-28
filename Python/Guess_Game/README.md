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

# 🎮 GUESS BATTLE

Game **“Guess Battle”** adalah permainan **tebak angka multi-level dan multi-player** berbasis CLI (Command Line Interface) yang dibuat dengan bahasa **Python**.  
Proyek ini menerapkan konsep **loop, conditional, modularisasi, file handling, JSON**, dan penggunaan warna terminal dengan **colorama**.

---

## 🧩 Fitur Utama

1. **Login Pemain**
   - Pemain dapat masuk menggunakan **nama pengguna**.
   - Skor akan disimpan dan dimuat dari file `scores.json`.

2. **Tiga Level Permainan**
   | Level | Rentang Angka | Percobaan Maksimal |
   |--------|----------------|--------------------|
   | 1 | 1–10 | 3 percobaan |
   | 2 | 1–50 | 5 percobaan |
   | 3 | 1–100 | 7 percobaan |

3. **Sistem Skor**
   - Skor dihitung berdasarkan jumlah percobaan yang tersisa.
   - Semakin cepat pemain menebak, semakin tinggi poinnya.

4. **Penyimpanan Data**
   - Hasil permainan disimpan secara otomatis ke file `scores.json`.

5. **Leaderboard**
   - Menampilkan **Top 5 pemain terbaik** berdasarkan skor tertinggi.

6. **Efek Visual**
   - Menggunakan **colorama** untuk memberi warna pada teks terminal:
     - 🟢 Hijau = sukses
     - 🔴 Merah = salah
     - 🟡 Kuning = informasi

---

---

## ⚙️ Instalasi

1. Pastikan Python versi 3.8 atau lebih baru sudah terpasang.  
   Cek dengan:
   ```bash
   python --version
   ```
2. Install library colorama:
    ```bash
    pip install colorama
    ```
3. Unduh semua file (main.py, game.py, scoreboard.py) ke dalam satu folder.

## ▶️ Cara Menjalankan Program

    1. Buka terminal atau CMD di folder proyek.
    2. Jalankan perintah berikut:
```bash
python main.py
```
    3. Masukkan nama pemain untuk login.
    4. Pilih level permainan (1, 2, atau 3).
    5. Tebak angka yang muncul — kamu punya jumlah percobaan tertentu di setiap level.
    6. Setelah permainan selesai, lihat skor kamu dan Top 5 pemain terbaik!

## 📊 Contoh Tampilan Hasil
=== TOP 5 SCORE ===
1. Rina  – 230 pts
2. Budi  – 200 pts
3. Dinda – 170 pts
4. Dimas – 150 pts
5. Tika  – 120 pts

## 💡 Studi Kasus

Proyek ini mensimulasikan sistem game turnamen sederhana berbasis CLI,
mengajarkan:

Penggunaan loop & conditional

Handling error dengan try-except

File I/O dan JSON

Pemrograman modular dengan beberapa file .py

Penggunaan warna terminal interaktif