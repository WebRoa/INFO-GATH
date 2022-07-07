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
                      <Multiple Port Scanner>
""")

target_ip = input("Target IP: ")
port_1 = input("Port 1: ")
port_2 = input("Port 2: ")
port_3 = input("Port 3: ")

os.system("sudo nmap " + target_ip + " -p " + port_1 + " " + port_2 + " " + port_3)
input("Press ENTER To Go Back... ")
os.system("python3 main.py")