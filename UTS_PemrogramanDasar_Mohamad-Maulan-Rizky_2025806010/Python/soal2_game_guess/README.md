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

# 🎮 GUESS BATTLE

**Guess Battle** adalah game **tebak angka multi-level dan multi-player** berbasis CLI menggunakan Python.  
Proyek ini menerapkan **loop, conditional, modularisasi, file handling, JSON, try-except**, serta warna terminal via **colorama**.

---

## 🧩 Fitur Utama

### ✅ Fitur 
| Fitur | Deskripsi |

- Login pemain | Nama pemain disimpan pada file JSON |
- 3 level permainan | Range angka meningkat per level |
- Sistem skor | Skor berdasarkan sisa percobaan |
- Penyimpanan skor | Disimpan otomatis ke `scores.json` |
- Leaderboard | Menampilkan Top 5 pemain |
- Efek warna | Menggunakan `colorama` |
- Mode Multiplayer | Dua pemain bermain bergiliran |
- Penentuan pemenang | Berdasarkan skor akhir |
- Log permainan | Semua sesi tersimpan ke `game_log.json` |

---

## 🧠 Level dan Aturan

| Level | Rentang Angka | Percobaan |
|---|---|---|
1 | 1–10 | 3 |
2 | 1–50 | 5 |
3 | 1–100 | 7 |

Semakin cepat benar, semakin tinggi skor.


---

## ⚙️ Instalasi

```bash
python --version
```
```bash
pip install colorama
```

---

## ▶️ Cara Menjalankan
``` bash
python main.py
```
**Menu awal:**

- Mode Single Player
- Mode Multiplayer (2 pemain)

---
## 📊 Leaderboard Contoh
```
=== TOP 5 SCORE ===
1. Rina  – 230 pts
2. Budi  – 200 pts
3. Dinda – 170 pts
4. Dimas – 150 pts
5. Tika  – 120 pts
```
---
## 📁 Contoh Data Log (game_log.json)
```json
[
  {
    "mode": "multiplayer",
    "player1": "Rina",
    "score1": 230,
    "player2": "Budi",
    "score2": 200,
    "winner": "Rina"
  }
]
```