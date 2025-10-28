#include <stdio.h>
#include <stdlib.h>

struct Mahasiswa {
    char nama[50];
    char nim[20];
    float tugas, uts, uas, nilai_akhir;
    char mutu;
};

char getMutu(float nilai) {
    if (nilai >= 85) return 'A';
    else if (nilai >= 70) return 'B';
    else if (nilai >= 60) return 'C';
    else if (nilai >= 50) return 'D';
    else return 'E';
}

int main() {
    FILE *fp;
    int n, i;
    struct Mahasiswa mhs;

    fp = fopen("data_mahasiswa.csv", "w");
    if (!fp) {
        printf("Gagal membuat file!\n");
        return 1;
    }

    fprintf(fp, "Nama,NIM,Tugas,UTS,UAS,NilaiAkhir,Mutu\n");

    printf("Masukkan jumlah mahasiswa: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        printf("\nData mahasiswa ke-%d\n", i + 1);
        printf("Nama: "); scanf("%s", mhs.nama);
        printf("NIM: "); scanf("%s", mhs.nim);
        printf("Nilai Tugas: "); scanf("%f", &mhs.tugas);
        printf("Nilai UTS: "); scanf("%f", &mhs.uts);
        printf("Nilai UAS: "); scanf("%f", &mhs.uas);

        mhs.nilai_akhir = (mhs.tugas * 0.3) + (mhs.uts * 0.3) + (mhs.uas * 0.4);
        mhs.mutu = getMutu(mhs.nilai_akhir);

        fprintf(fp, "%s,%s,%.2f,%.2f,%.2f,%.2f,%c\n",
                mhs.nama, mhs.nim, mhs.tugas, mhs.uts, mhs.uas, mhs.nilai_akhir, mhs.mutu);
    }

    fclose(fp);
    printf("\n✅ Data berhasil disimpan ke data_mahasiswa.csv\n");
    return 0;
}
