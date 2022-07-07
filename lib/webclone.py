import requests
import time

import os

os.system("clear")

print("""
 ██▓ ███▄    █   █████▒▒█████    ▄████  ▄▄▄     ▄▄▄█████▓ ██░ ██ 
▓██▒ ██ ▀█   █ ▓██   ▒▒██▒  ██▒ ██▒ ▀█▒▒████▄   ▓  ██▒ ▓▒▓██░ ██▒
▒██▒▓██  ▀█ ██▒▒████ ░▒██░  ██▒▒██░▄▄▄░▒██  ▀█▄ ▒ ▓██░ ▒░▒██▀▀██░
░██░▓██▒  ▐▌██▒░▓█▒  ░▒██   ██░░▓█  ██▓░██▄▄▄▄██░ ▓██▓ ░ ░▓█ ░██ 
░██░▒██░   ▓██░░▒█░   ░ ████▓▒░░▒▓███▀▒ ▓█   ▓██▒ ▒██▒ ░ ░▓█▒░██▓
░▓  ░ ▒░   ▒ ▒  ▒ ░   ░ ▒░▒░▒░  ░▒   ▒  ▒▒   ▓▒█░ ▒ ░░    ▒ ░░▒░▒
 ▒ ░░ ░░   ░ ▒░ ░       ░ ▒ ▒░   ░   ░   ▒   ▒▒ ░   ░     ▒ ░▒░ ░
 ▒ ░   ░   ░ ░  ░ ░   ░ ░ ░ ▒  ░ ░   ░   ░   ▒    ░       ░  ░░ ░
 ░           ░            ░ ░        ░       ░  ░         ░  ░  ░
                      <Page Code Stealer>
""")

target = input("Url You Wan't To Code Steal 'https://example.com/': ")

page = requests.get(target)
print(page.content)

time.sleep(3)
print("Page Code STOLEN...")
input("Press ENTER To Go Back: ")
os.system("python3 main.py")
