import requests
import pyfiglet
from termcolor import colored

def check_subdomains(base_domain, wordlist_path):
    with open(wordlist_path, 'r') as file:
        sub_list = file.read().splitlines()

    for sub in sub_list:
        sub_domain = f"http://{sub}.{base_domain}"
        try:
            response = requests.get(sub_domain, timeout=3)
            response.raise_for_status()
            print(colored("Valid domain:", "green"), colored(sub_domain, "cyan"))
        except requests.RequestException:
            pass

def check_directory(sub, directory):
    full_url = f"http://{sub}/{directory}"
    try:
        response = requests.get(full_url)
        response.raise_for_status()
        print(colored("Valid directory:", "green"), colored(full_url, "cyan"))
    except requests.exceptions.RequestException:
        pass

def print_welcome_message():
    ascii_art = pyfiglet.figlet_format("dirSubDomain tool", font="slant")
    print(colored(ascii_art, "red"))

def main():
    print_welcome_message()
    mode = input("Choose mode subdomains[s] or directories[d]: ").lower()

    if mode == "s":
        base_domain = input("Your base domain:\n")
        wordlist_path = input("Path to wordlist:\n")
        check_subdomains(base_domain, wordlist_path)
    elif mode == "d":
        url = input("Your URL:\n")
        wordlist_path = input("Path to wordlist:\n")

        try:
            with open(wordlist_path, "r") as file:
                directories = file.read().splitlines()
        except FileNotFoundError:
            print(f"Error: Wordlist file '{wordlist_path}' not found.")
            return

        for directory in directories:
            check_directory(url, directory)
    else:
        print("Invalid mode. Please choose 'subdomains' or 'directories'.")

if __name__ == "__main__":
    main()
