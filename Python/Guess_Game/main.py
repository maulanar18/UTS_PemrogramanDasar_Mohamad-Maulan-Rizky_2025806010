from colorama import init, Fore, Style
from game import start_game
from scoreboard import save_score, show_top_scores

def main():
    init(autoreset=True)

    print(Fore.YELLOW + "===== 🎮 GAME: GUESS BATTLE =====" + Style.RESET_ALL)
    name = input("Masukkan nama pemain: ").strip()
    if not name:
        print("Nama tidak boleh kosong!")
        return

    total_score = start_game(name)
    save_score(name, total_score)
    show_top_scores()

    print(Fore.GREEN + "Terima kasih telah bermain!\n" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
