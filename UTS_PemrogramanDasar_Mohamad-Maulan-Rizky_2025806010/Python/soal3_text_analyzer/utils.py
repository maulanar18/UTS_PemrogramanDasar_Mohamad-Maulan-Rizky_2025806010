import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return text

def count_vowels_consonants(text):
    vowels = sum(1 for ch in text if ch in "aeiou")
    consonants = sum(1 for ch in text if ch.isalpha() and ch not in "aeiou")
    return vowels, consonants

def search_word(text, word):
    text = text.lower()
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    return words.count(word)

def load_stopwords():
    try:
        with open("stopwords.txt", "r", encoding="utf-8") as f:
            return {w.strip() for w in f.readlines()}
    except:
        return set()
