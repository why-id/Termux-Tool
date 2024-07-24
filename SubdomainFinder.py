import requests
import os
import signal
import sys

# Fungsi untuk menangani sinyal penghentian (CTRL + C)
def signal_handler(sig, frame):
    print("\nProses dihentikan.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Fungsi untuk membersihkan layar di Termux
def clear_screen():
    os.system('clear')

# Fungsi untuk mendapatkan wordlist dari URL
def get_wordlist_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

# Fungsi utama untuk menemukan subdomain
def find_subdomains(domain, wordlist):
    clear_screen()  # Membersihkan layar sebelum memulai

    for subdomain in wordlist:
        url = f'http://{subdomain}.{domain}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"\033[92m[✓] Ditemukan: {url}\033[0m")
                with open(f'{domain}.txt', 'a', encoding='utf8') as out_file:
                    out_file.write(url + '\n')
        except requests.ConnectionError:
            pass

if __name__ == '__main__':
    clear_screen()
    print("Pilih wordlist subdomain:")
    print("1. 10,000 wordlist")
    print("2. 50,000 wordlist")
    
    choice = input("Masukkan pilihan (1/2): ").strip()

    if choice == '1':
        wordlist_url = 'https://raw.githubusercontent.com/Symbolexe/Xorn/main/subdomains.txt'
    elif choice == '2':
        wordlist_url = 'https://raw.githubusercontent.com/security007/subdolist/master/list.txt'
    else:
        print("Pilihan tidak valid.")
        sys.exit(1)

    print(f"Mengambil wordlist dari {wordlist_url}...")
    wordlist = get_wordlist_from_url(wordlist_url)
    print("Wordlist berhasil diambil.")

    domain = input("Masukkan domain (contoh: dexskieee.com): ").strip()
    find_subdomains(domain, wordlist)
