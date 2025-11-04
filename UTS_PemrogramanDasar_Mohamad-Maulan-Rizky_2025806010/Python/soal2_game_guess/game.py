import random
from colorama import Fore, Style

def play_level(level, name):
    # Tentukan batas angka dan jumlah percobaan
    if level == 1:
        limit, attempts = 10, 3
    elif level == 2:
        limit, attempts = 50, 5
    else:
        limit, attempts = 100, 7

    secret = random.randint(1, limit)
    print(f"\n{Fore.CYAN}=== Level {level} ==={Style.RESET_ALL}")
    print(f"Tebak angka antara 1 - {limit}. Kamu punya {attempts} percobaan.\n")

    for i in range(1, attempts + 1):
        try:
            guess = int(input(f"Percobaan {i}: Masukkan tebakanmu: "))
        except ValueError:
            print(Fore.RED + "⚠️ Masukkan angka yang valid!" + Style.RESET_ALL)
            continue

        if guess == secret:
            sisa = attempts - i
            score = (sisa + 1) * (level * 50)
            print(Fore.GREEN + f"🎉 Benar! Angka rahasia adalah {secret}." + Style.RESET_ALL)
            print(Fore.YELLOW + f"Kamu mendapat {score} poin!\n" + Style.RESET_ALL)
            return score
        elif guess < secret:
            print(Fore.BLUE + "Terlalu kecil!" + Style.RESET_ALL)
        else:
            print(Fore.MAGENTA + "Terlalu besar!" + Style.RESET_ALL)

    print(Fore.RED + f"😢 Gagal! Angka yang benar adalah {secret}.\n" + Style.RESET_ALL)
    return 0


def start_game(name):
    print(Fore.YELLOW + f"\nSelamat datang, {name}! Mari kita mulai GUESS BATTLE!\n" + Style.RESET_ALL)
    total_score = 0

    for level in range(1, 4):
        score = play_level(level, name)
        total_score += score
        if score == 0:
            print(Fore.RED + "Kamu kalah di level ini. Game over!\n" + Style.RESET_ALL)
            break

    print(Fore.CYAN + f"Total skor kamu: {total_score}\n" + Style.RESET_ALL)
    return total_score
