from collections import Counter
from utils import clean_text, count_vowels_consonants

def analyze_text(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    total_lines = len(lines)
    text = " ".join(lines)
    words = clean_text(text).split()

    total_words = len(words)
    vowel_count, consonant_count = count_vowels_consonants(text)

    word_freq = Counter(words)
    top_words = dict(word_freq.most_common(5))

    return {
        "lines": total_lines,
        "words": total_words,
        "vowels": vowel_count,
        "consonants": consonant_count,
        "top_words": top_words
    }

def generate_report(result, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=== LAPORAN ANALISIS TEKS ===\n")
        f.write(f"Jumlah Baris     : {result['lines']}\n")
        f.write(f"Jumlah Kata      : {result['words']}\n")
        f.write(f"Vokal            : {result['vowels']}\n")
        f.write(f"Konsonan         : {result['consonants']}\n")
        f.write("\n=== 5 KATA TERBANYAK ===\n")

        for word, count in result["top_words"].items():
            f.write(f"{word:<10} {'#' * count}\n")
