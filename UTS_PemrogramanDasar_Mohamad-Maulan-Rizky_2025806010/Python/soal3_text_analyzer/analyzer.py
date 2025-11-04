from collections import Counter
from utils import clean_text, count_vowels_consonants, load_stopwords

def analyze_text(text):
    stopwords = load_stopwords()
    
    lines = text.count("\n") + 1
    cleaned = clean_text(text)

    words = cleaned.split()
    words_filtered = [w for w in words if w not in stopwords]

    word_count = len(words_filtered)
    sentences = text.count(".") + text.count("!") + text.count("?")

    vowels, consonants = count_vowels_consonants(cleaned)

    top_words = dict(Counter(words_filtered).most_common(5))

    avg_words_sentence = word_count / sentences if sentences else 0
    avg_chars_word = sum(len(w) for w in words_filtered) / word_count if word_count else 0

    return {
        "lines": lines,
        "words": word_count,
        "sentences": sentences,
        "avg_words_per_sentence": avg_words_sentence,
        "avg_chars_per_word": avg_chars_word,
        "vowels": vowels,
        "consonants": consonants,
        "top_words": top_words
    }


def export_json(data):
    import json
    with open("report.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
