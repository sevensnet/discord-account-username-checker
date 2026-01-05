import requests
import time
import random
import itertools
import string
import os
import sys

# --- CONFIGURATION & FILES ---
CHECKED_FILE = "checked_names.txt"
AVAILABLE_FILE = "available_names.txt"
PROXY_FILE = "proxies.txt"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_proxies():
    if not os.path.exists(PROXY_FILE):
        with open(PROXY_FILE, "w") as f: pass # Create empty file
        return []
    with open(PROXY_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def get_config():
    clear_screen()
    print("=== DISCORD ULTIMATE SCANNER CONFIG ===")
    
    length = int(input("Username Length (e.g. 3): ") or 3)
    
    use_letters = input("Include Letters (a-z)? (y/n): ").lower() == 'y'
    use_numbers = input("Include Numbers (0-9)? (y/n): ").lower() == 'y'
    use_dots = input("Include Dots (.)? (y/n): ").lower() == 'y'
    
    chars = ""
    if use_letters: chars += string.ascii_lowercase
    if use_numbers: chars += string.digits
    if use_dots:    chars += "."
    
    if not chars:
        print("!! Error: No characters selected.")
        sys.exit()

    min_d = float(input("Min Delay (sec) [0 if using many proxies]: ") or 0)
    max_d = float(input("Max Delay (sec): ") or 0.1)
    
    return chars, length, (min_d, max_d)

def check_discord(username, proxies=None):
    # Rule validation: Discord doesn't allow double dots or dots at start/end
    if ".." in username or username.startswith(".") or username.endswith("."):
        return "Invalid"
        
    url = f"https://discord.com/api/v9/users/{username}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/121.0.0.0"}
    
    proxy_dict = None
    if proxies:
        p = random.choice(proxies)
        proxy_dict = {"http": p, "https": p}

    try:
        response = requests.get(url, headers=headers, proxies=proxy_dict, timeout=5)
        if response.status_code == 404:
            return "Available"
        elif response.status_code == 429:
            return "RateLimit"
        else:
            return "Taken"
    except:
        return "ProxyError"

def main():
    chars, length, delay_range = get_config()
    proxies = load_proxies()
    
    if not proxies:
        print("\n[!] No proxies found in proxies.txt. Using local IP (High risk of rate limit).")
    else:
        print(f"\n[!] Loaded {len(proxies)} proxies.")

    # Generate and filter
    all_combos = [''.join(i) for i in itertools.product(chars, repeat=length)]
    
    # Pre-filter history
    if os.path.exists(CHECKED_FILE):
        with open(CHECKED_FILE, "r") as f:
            done = set(line.strip() for line in f)
        to_check = [c for c in all_combos if c not in done]
    else:
        to_check = all_combos

    total = len(to_check)
    print(f"[!] Starting scan for {total} names...")
    time.sleep(2)

    with open(AVAILABLE_FILE, "a") as af, open(CHECKED_FILE, "a") as cf:
        for i, name in enumerate(to_check, 1):
            res = check_discord(name, proxies)
            
            if res == "RateLimit":
                print(f"[{i}/{total}] !! RATE LIMITED. Change VPN/Proxies or wait.")
                time.sleep(30)
                continue
            
            if res == "ProxyError":
                print(f"[{i}/{total}] !! Proxy failed. Skipping...")
                continue

            if res != "Invalid":
                cf.write(name + "\n")
                cf.flush()

            if res == "Available":
                print(f"[{i}/{total}] [+] FOUND: {name}")
                af.write(name + "\n")
                af.flush()
            elif res == "Taken":
                print(f"[{i}/{total}] [-] {name}")

            if delay_range[1] > 0:
                time.sleep(random.uniform(*delay_range))

if __name__ == "__main__":
    main()
