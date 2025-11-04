import csv, json

mahasiswa = []

with open('data_mahasiswa.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        row['nilai_akhir'] = float(row['nilai_akhir'])
        mahasiswa.append(row)

print("=== DATA MAHASISWA ===")
for m in mahasiswa:
    print(f"{m['nama']:10} | {m['nim']} | {m['nilai_akhir']:6.2f} | {m['mutu']}")

rata = sum(m['nilai_akhir'] for m in mahasiswa) / len(mahasiswa)
print(f"\nRata-rata nilai akhir: {rata:.2f}")

# Fitur Ranking
mahasiswa_sorted = sorted(mahasiswa, key=lambda x: x['nilai_akhir'], reverse=True)

print("\n=== PERINGKAT MAHASISWA ===")
for i, m in enumerate(mahasiswa_sorted, start=1):
    print(f"{i}. {m['nama']:10} | {m['nilai_akhir']:6.2f} | {m['mutu']}")

# Simpan JSON
with open('data_mahasiswa.json', 'w') as jf:
    json.dump(mahasiswa, jf, indent=2)

# Simpan CSV versi ranking
with open('data_mahasiswa_ranked.csv', 'w', newline='') as rf:
    fieldnames = ['nama', 'nim', 'nilai_akhir', 'mutu']
    writer = csv.DictWriter(rf, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(mahasiswa_sorted)
