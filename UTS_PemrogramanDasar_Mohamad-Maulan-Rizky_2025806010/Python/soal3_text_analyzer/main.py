from analyzer import analyze_text, export_json
from utils import search_word

def main():
    input_file = "input.txt"

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print("File input.txt tidak ditemukan.")
        return

    result = analyze_text(text)

    print("======= HASIL ANALISIS TEKS =======")
    print(f"Jumlah Baris              : {result['lines']}")
    print(f"Jumlah Kata               : {result['words']}")
    print(f"Jumlah Kalimat            : {result['sentences']}")
    print(f"Rata Kata / Kalimat       : {result['avg_words_per_sentence']:.2f}")
    print(f"Rata Huruf / Kata         : {result['avg_chars_per_word']:.2f}")
    print(f"Huruf Vokal               : {result['vowels']}")
    print(f"Huruf Konsonan            : {result['consonants']}\n")

    print("====== 5 Kata Teratas ======")
    for word, freq in result["top_words"].items():
        print(f"{word:<12} {'#' * freq}")

    cari = input("\nMasukkan kata untuk dicari frekuensinya: ").lower()
    freq = search_word(text, cari)
    print(f"Frekuensi '{cari}' : {freq} kali\n")

    export_json(result)
    print("Hasil disimpan ke report.json")
    print("Hasil analisis tersimpan di report.txt")

    # Save to report.txt
    with open("report.txt", "w", encoding="utf-8") as f:
        for k, v in result.items():
            f.write(f"{k}: {v}\n")

if __name__ == "__main__":
    main()

