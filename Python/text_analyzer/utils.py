import string

def clean_text(text):
    """Bersihkan teks dari tanda baca dan ubah menjadi huruf kecil"""
    translator = str.maketrans("", "", string.punctuation)
    return text.translate(translator).lower()

def count_vowels_consonants(text):
    """Hitung jumlah huruf vokal dan konsonan"""
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for ch in text if ch in vowels)
    consonant_count = sum(1 for ch in text if ch.isalpha() and ch not in vowels)
    return vowel_count, consonant_count
