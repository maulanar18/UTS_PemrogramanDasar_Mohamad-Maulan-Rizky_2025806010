import json
from colorama import Fore, Style

def load_scores(filename="scores.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_score(name, score, filename="scores.json"):
    data = load_scores(filename)
    if name in data:
        data[name] = max(data[name], score)
    else:
        data[name] = score

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def show_top_scores(filename="scores.json"):
    data = load_scores(filename)
    sorted_scores = sorted(data.items(), key=lambda x: x[1], reverse=True)[:5]

    print(Fore.CYAN + "\n=== 🏆 TOP 5 SCORE ===" + Style.RESET_ALL)
    if not sorted_scores:
        print("Belum ada skor tersimpan.\n")
        return

    for i, (name, score) in enumerate(sorted_scores, 1):
        print(f"{i}. {name} – {score} pts")
    print()
