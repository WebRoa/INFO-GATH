import os
import time
import socket
import colorama
from colorama import Fore
colorama.init()

os.system("clear")

re = Fore.RED
gr = Fore.GREEN
bl = Fore.BLUE
ma = Fore.MAGENTA
cy = Fore.CYAN
ye = Fore.YELLOW

print(gr)

os.system("clear")

print(gr + "[!] Welcome: " + socket.gethostname() + " ✔")

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

	    Tools:
                   - iptrack        | Gathering Information About IP
                   - iplocate       | Locating IP Address
                   - creditcv       | Validate If Credit Card Is Real
                   - popularpscan   | Scanning Popular Ports
                   - 1portscan      | Scanning 1 Port
                   - multiplescan   | Scanning Multiple Ports
	  	   - ping           | Pinging Host
                   - webtoip        | Convert Website To IP
                   - paping         | Ping Host With Different Ports
		   - packetsniff    | Capture Packets On Your Network
		   - webcodesteal   | Steal Website's Html Code
		   - pagelinkscrape | Scrapes All Links In Website
""")

ragaca = input("[!] - CHOOSE ONE: ")

if ragaca == "iptrack":
	os.system("python3 lib/location_tracker.py")
if ragaca == "iplocate":
        os.system("python3 lib/locator.py")
if ragaca == "creditcv":
       os.system("python3 lib/credit_card_valid.py")
if ragaca == "popularpscan":
        os.system("python3 lib/popular_ports-scan.py")
if ragaca == "1portscan":
        os.system("python3 lib/1_nmap_port.py")
if ragaca == "multiplescan":
	os.system("python3 lib/multiple_nmap_port_scan.py")
if ragaca == "ping":
	os.system("python3 lib/ping.py")
if ragaca == "webtoip":
	os.system("python3 lib/website_to_ip.py")
if ragaca == "paping":
	os.system("python3 lib/paping.py")
if ragaca == "packetsniff":
	os.system("sudo wireshark")
if ragaca == "webcodesteal":
	os.system("python3 lib/webclone.py")
if ragaca == "pagelinkscrape":
	os.system("python3 lib/linkscrape.py")
else:
	print("Command: " + ragaca + " Not Found")
	time.sleep(1)
	os.system("python3 main.py")
