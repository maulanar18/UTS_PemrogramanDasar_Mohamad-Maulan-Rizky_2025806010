import csv
import json

def baca_csv(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row["Tugas"] = float(row["Tugas"])
            row["UTS"] = float(row["UTS"])
            row["UAS"] = float(row["UAS"])
            row["NilaiAkhir"] = float(row["NilaiAkhir"])
            data.append(row)
    return data

def hitung_rata_rata(data):
    if not data:
        return 0
    total = sum(d["NilaiAkhir"] for d in data)
    return total / len(data)

def simpan_json(data, filename):
    json_data = []
    for d in data:
        json_data.append({
            "nama": d["Nama"],
            "nim": d["NIM"],
            "nilai_akhir": d["NilaiAkhir"],
            "mutu": d["Mutu"]
        })
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(json_data, f, indent=4, ensure_ascii=False)

def tampilkan_data(data):
    print("\n=== DATA MAHASISWA ===")
    print(f"{'Nama':<10} {'NIM':<10} {'Nilai Akhir':<12} {'Mutu'}")
    print("-" * 40)
    for d in data:
        print(f"{d['Nama']:<10} {d['NIM']:<10} {d['NilaiAkhir']:<12.2f} {d['Mutu']}")
    print("-" * 40)

if __name__ == "__main__":
    csv_file = "data_mahasiswa.csv"
    json_file = "data_mahasiswa.json"

    try:
        data = baca_csv(csv_file)
        tampilkan_data(data)
        rata = hitung_rata_rata(data)
        print(f"\n📊 Rata-rata Nilai Akhir: {rata:.2f}")

        simpan_json(data, json_file)
        print(f"✅ Data berhasil dikonversi ke {json_file}")

    except FileNotFoundError:
        print("❌ File CSV tidak ditemukan. Jalankan dulu program C untuk membuat data_mahasiswa.csv.")
