import time
import requests
import random
import os
import signal
from colorama import Fore, Style, Back, init
import urllib3

# Inisialisasi colorama
init(autoreset=True)

# Nonaktifkan peringatan InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def signal_handler(sig, frame):
    print("\nProses dihentikan oleh pengguna.")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

def get_proxies():
    clear_screen()
#    pastebin_url = input(f"{Back.RED}{Fore.WHITE} Masukkan URL Proxy.txt {Back.RESET}{Fore.RESET}  ")
    pastebin_url = 'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt'
    response = requests.get(pastebin_url)
    return response.text.strip().split('\n')

def get_user_inputs():
    clear_screen()
    url_web = input(f"{Back.RED}{Fore.WHITE} URL Website {Back.RESET}{Fore.RESET}  ")
    clear_screen()
    total = int(input(f"{Back.RED}{Fore.WHITE} Mau Berapa {Back.RESET}{Fore.RESET}  "))
    return url_web, total

# User agent random
user_agents = [
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.52 Safari/536.5',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/5.0 (iPad; U; CPU OS 3_2 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B334b Safari/531.21.102011-10-16 20:23:50',
    'Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 3_0 like Mac OS X; en-us) AppleWebKit/528.18 (KHTML, like Gecko) Version/4.0 Mobile/7A341 Safari/528.16',
    'iTunes/9.1 (Macintosh; U; PPC Mac OS X 10.2',
    'Mozilla/5.0 (Linux; U; Android 2.1; en-us; Nexus One Build/ERD62) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Mobile Safari/530.17',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11',
    'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 8.0',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.7) Gecko/20070914 Firefox/2.0.0.7'
]

def curl(url_web, proxies):
    ip_proxy = random.choice(proxies).strip()

    #Jika tidak ada port pada proxy maka
    if ':' not in ip_proxy:
        print(f"{Fore.RED}Proxy salah : {ip_proxy}")
        return

    user_agent = random.choice(user_agents)

    proxy_dict = {
        "http": f"http://{ip_proxy}",
        "https": f"http://{ip_proxy}",
    }

    headers = {
        'User-Agent': user_agent,
        'Referer': 'https://www.google.co.id'
    }

    try:
        response = requests.get(url_web, headers=headers, proxies=proxy_dict, verify=False, timeout=10)

        print(f"{Fore.WHITE}[ {Fore.GREEN}✓ {Fore.WHITE}] Menambah Visitor{Fore.WHITE}")
    except requests.RequestException as e:
        print(f"{Fore.WHITE}[ {Fore.RED}x {Fore.WHITE}] Menambah Visitor{Fore.WHITE}")

proxies = get_proxies()
url_web, total = get_user_inputs()

for _ in range(total):
    curl(url_web, proxies)

