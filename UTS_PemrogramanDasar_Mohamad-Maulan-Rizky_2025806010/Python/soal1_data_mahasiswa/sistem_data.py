import csv
import json
import os

class Mahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = tugas
        self.uts = uts
        self.uas = uas
        self.nilai_akhir = self.hitung_nilai()
        self.mutu = self.get_mutu()
        self.next = None  

    def hitung_nilai(self):
        return 0.3 * self.tugas + 0.3 * self.uts + 0.4 * self.uas

    def get_mutu(self):
        n = self.nilai_akhir
        if n >= 85:
            return "A"
        elif n >= 70:
            return "B"
        elif n >= 60:
            return "C"
        elif n >= 50:
            return "D"
        else:
            return "E"


def load_data(filename="data_mahasiswa.csv"):
    if not os.path.exists(filename):
        return None

    head = None
    with open(filename, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            baru = Mahasiswa(row["Nama"], row["NIM"], float(row["Tugas"]), float(row["UTS"]), float(row["UAS"]))
            head = insert_last(head, baru)
    print("📂 Data sebelumnya berhasil dimuat.\n")
    return head


def insert_last(head, node):
    if head is None:
        return node
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = node
    return head


def tambah_data(head):
    try:
        nama = input("Masukkan Nama: ")
        nim = input("Masukkan NIM: ")
        tugas = float(input("Masukkan Nilai Tugas: "))
        uts = float(input("Masukkan Nilai UTS: "))
        uas = float(input("Masukkan Nilai UAS: "))
    except:
        print("❌ Input nilai harus angka!\n")
        return head

    baru = Mahasiswa(nama, nim, tugas, uts, uas)
    head = insert_last(head, baru)

    print(f"✅ Data mahasiswa '{nama}' berhasil ditambahkan.\n")
    return head


def tampilkan_data(head):
    if head is None:
        print("Belum ada data mahasiswa.\n")
        return

    print(f"{'Nama':<15}{'NIM':<12}{'Tugas':<8}{'UTS':<8}{'UAS':<8}{'Nilai Akhir':<13}{'Mutu':<5}")
    print("-" * 70)
    temp = head
    while temp:
        print(f"{temp.nama:<15}{temp.nim:<12}{temp.tugas:<8.1f}{temp.uts:<8.1f}{temp.uas:<8.1f}{temp.nilai_akhir:<13.2f}{temp.mutu:<5}")
        temp = temp.next
    print()


def simpan_ke_file(head, filename="data_mahasiswa.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "NIM", "Tugas", "UTS", "UAS", "NilaiAkhir", "Mutu"])

        temp = head
        while temp:
            writer.writerow([temp.nama, temp.nim, temp.tugas, temp.uts, temp.uas, f"{temp.nilai_akhir:.2f}", temp.mutu])
            temp = temp.next

    print(f"📁 Data berhasil disimpan ke file '{filename}'.\n")


def export_json(head, filename="data_mahasiswa.json"):
    data = []
    temp = head
    while temp:
        data.append({
            "nama": temp.nama,
            "nim": temp.nim,
            "tugas": temp.tugas,
            "uts": temp.uts,
            "uas": temp.uas,
            "nilai": temp.nilai_akhir,
            "mutu": temp.mutu
        })
        temp = temp.next

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"📦 Data berhasil diexport ke '{filename}'.\n")


def cari_mahasiswa(head, nim):
    temp = head
    while temp:
        if temp.nim == nim:
            print(f"✅ Ditemukan: {temp.nama} ({temp.nim}) | Nilai Akhir: {temp.nilai_akhir:.2f}, Mutu: {temp.mutu}\n")
            return temp
        temp = temp.next
    print(f"❌ Mahasiswa dengan NIM {nim} tidak ditemukan.\n")
    return None


def hapus_mahasiswa(head, nim):
    if head is None:
        print("Data masih kosong!\n")
        return head

    if head.nim == nim:
        print(f"🗑️ Data mahasiswa {head.nama} ({head.nim}) dihapus.\n")
        return head.next 

    prev = head
    curr = head.next
    while curr:
        if curr.nim == nim:
            print(f"🗑️ Data mahasiswa {curr.nama} ({curr.nim}) dihapus.\n")
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next

    print(f"❌ Data dengan NIM {nim} tidak ditemukan.\n")
    return head


def update_mahasiswa(head, nim):
    temp = head
    while temp:
        if temp.nim == nim:
            try:
                print("Masukkan data baru:")
                temp.nama = input("Nama baru: ")
                temp.tugas = float(input("Nilai tugas baru: "))
                temp.uts = float(input("Nilai UTS baru: "))
                temp.uas = float(input("Nilai UAS baru: "))
            except:
                print("❌ Input nilai harus angka!\n")
                return head

            temp.nilai_akhir = temp.hitung_nilai()
            temp.mutu = temp.get_mutu()
            print("✅ Data berhasil diperbarui!\n")
            return head
        temp = temp.next

    print("❌ Data tidak ditemukan.\n")
    return head


def sort_mahasiswa(head, key):
    if head is None:
        print("Belum ada data untuk disort.\n")
        return head

    data = []
    temp = head
    while temp:
        data.append(temp)
        temp = temp.next

    if key == "nama":
        data.sort(key=lambda x: x.nama)
    elif key == "nim":
        data.sort(key=lambda x: x.nim)
    elif key == "nilai":
        data.sort(key=lambda x: x.nilai_akhir, reverse=True)

    head = None
    for d in data:
        head = insert_last(head, d)

    print("✅ Data berhasil diurutkan.\n")
    return head


def main():
    head = load_data()

    while True:
        print("===== MENU MANAJEMEN DATA MAHASISWA =====")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Data")
        print("3. Cari Mahasiswa berdasarkan NIM")
        print("4. Hapus Mahasiswa")
        print("5. Update Data Mahasiswa")
        print("6. Sort Data Mahasiswa")
        print("7. Simpan ke File CSV")
        print("8. Export ke JSON")
        print("0. Keluar")
        print("==========================================")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            head = tambah_data(head)
        elif pilihan == "2":
            tampilkan_data(head)
        elif pilihan == "3":
            nim = input("Masukkan NIM yang dicari: ")
            cari_mahasiswa(head, nim)
        elif pilihan == "4":
            nim = input("Masukkan NIM yang akan dihapus: ")
            head = hapus_mahasiswa(head, nim)
        elif pilihan == "5":
            nim = input("Masukkan NIM yang akan diperbarui: ")
            head = update_mahasiswa(head, nim)
        elif pilihan == "6":
            print("Sort berdasarkan:")
            print("1. Nama")
            print("2. NIM")
            print("3. Nilai Akhir (Descending)")
            k = input("Pilih: ")
            if k == "1":
                head = sort_mahasiswa(head, "nama")
            elif k == "2":
                head = sort_mahasiswa(head, "nim")
            elif k == "3":
                head = sort_mahasiswa(head, "nilai")
        elif pilihan == "7":
            simpan_ke_file(head)
        elif pilihan == "8":
            export_json(head)
        elif pilihan == "0":
            simpan_ke_file(head)
            print("Program selesai. Semua data telah disimpan.\n")
            break
        else:
            print("Pilihan tidak valid!\n")


if __name__ == "__main__":
    main()
