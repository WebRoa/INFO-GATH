import requests
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
                      <Locator>
""")

target_ip = input("Target IP: ")
api = "https://geolocation-db.com/json/"

res = requests.get(api + target_ip)

data = res.json()

print("----------------------------------")
print("IP: ", target_ip)
print("Latitude: ", data["latitude"])
print("Longitude: ", data["longitude"])
print("----------------------------------")
input("Press ENTER To Go Back... ")
os.system("python3 main.py")