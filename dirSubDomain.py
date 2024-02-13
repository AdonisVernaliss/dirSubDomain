import requests
import pyfiglet
from termcolor import colored

def check_mode(base_domain, wordlist_path, is_subdomain):
    with open(wordlist_path, 'r') as file:
        urls = file.read().splitlines()

    for url in urls:
        full_url = f"http://{url}.{base_domain}" if is_subdomain else f"http://{base_domain}/{url}"
        try:
            response = requests.get(full_url, timeout=3)
            if response.ok:
                print(colored("Valid domain:" if is_subdomain else "Valid directory:", "green"), colored(full_url, "cyan"))
        except requests.RequestException:
            pass

def welcome_message():
    msg = pyfiglet.figlet_format("dirSubDomain tool", font="slant")
    print(colored(msg, "red"))

def main():
    welcome_message()
    mode = input("Choose mode subdomains[s] or directories[d]: ").lower()

    if mode == "s":
        base_domain = input("Your base domain:\n")
        wordlist_path = input("Path to wordlist:\n")
        check_mode(base_domain, wordlist_path, True)
    elif mode == "d":
        base_domain = input("Your domain:\n")
        wordlist_path = input("Path to wordlist:\n")
        check_mode(base_domain, wordlist_path, False)
    else:
        print("Invalid mode. Please choose 'subdomains' or 'directories'.")

if __name__ == "__main__":
    main()
