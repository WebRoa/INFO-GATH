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
                      <1 Port Scanner>
""")

target_ip = input("Target IP: ")
port_scan = input("Port You Want To Scan In Host: ")

os.system("nmap -Pn -p " + port_scan + " " + target_ip)
input("Press ENTER To Go Back... ")
os.system("python3 main.py")