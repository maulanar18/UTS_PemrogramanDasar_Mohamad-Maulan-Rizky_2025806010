from colorama import init, Fore, Style
from game import start_game
from scoreboard import save_score, show_top_scores
import json

def save_game_log(data):
    try:
        logs = json.load(open("game_log.json"))
    except:
        logs = []

    logs.append(data)
    json.dump(logs, open("game_log.json", "w"), indent=2)

def main():
    init(autoreset=True)

    print(Fore.YELLOW + "===== 🎮 GAME: GUESS BATTLE =====" + Style.RESET_ALL)
    print("1. Single Player")
    print("2. Multiplayer (2 pemain)\n")

    mode = input("Pilih mode (1/2): ").strip()

    if mode == "1":
        name = input("Masukkan nama pemain: ").strip()
        if not name:
            print("Nama tidak boleh kosong!")
            return

        total_score = start_game(name)
        save_score(name, total_score)
        save_game_log({"mode": "single", "player": name, "score": total_score})

    elif mode == "2":
        p1 = input("Masukkan nama Player 1: ").strip()
        p2 = input("Masukkan nama Player 2: ").strip()

        print(Fore.CYAN + f"\n--- Giliran {p1} ---" + Style.RESET_ALL)
        s1 = start_game(p1)

        print(Fore.CYAN + f"\n--- Giliran {p2} ---" + Style.RESET_ALL)
        s2 = start_game(p2)

        if s1 > s2:
            winner = p1
        elif s2 > s1:
            winner = p2
        else:
            winner = "Draw"

        print(Fore.MAGENTA + f"\nPemenang: {winner}" + Style.RESET_ALL)

        save_score(p1, s1)
        save_score(p2, s2)

        save_game_log({
            "mode": "multiplayer",
            "player1": p1, "score1": s1,
            "player2": p2, "score2": s2,
            "winner": winner
        })

    else:
        print("Pilihan tidak valid!")
        return

    show_top_scores()
    print(Fore.GREEN + "\nTerima kasih telah bermain!\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
