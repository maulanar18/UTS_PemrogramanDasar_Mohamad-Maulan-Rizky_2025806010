from analyzer import analyze_text, generate_report

def main():
    input_file = "input.txt"
    output_file = "report.txt"

    print("=== ANALISIS TEKS OTOMATIS ===")

    try:
        result = analyze_text(input_file)
        generate_report(result, output_file)

        print("\n=== HASIL ANALISIS ===")
        print(f"Jumlah Baris     : {result['lines']}")
        print(f"Jumlah Kata      : {result['words']}")
        print(f"Vokal            : {result['vowels']}")
        print(f"Konsonan         : {result['consonants']}")
        print("\n=== 5 KATA TERBANYAK ===")

        for word, count in result["top_words"].items():
            print(f"{word:<10} {'#' * count}")

        print(f"\nLaporan tersimpan di: {output_file}")

    except FileNotFoundError:
        print(f"File '{input_file}' tidak ditemukan. Pastikan file ada di folder yang sama.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
