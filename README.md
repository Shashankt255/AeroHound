# 🐺 AeroHound  

[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg?logo=python)](https://www.python.org/)  
[![OS](https://img.shields.io/badge/OS-Linux%20%7C%20Windows-lightgrey?logo=linux)](https://github.com/Shashankt255/AeroHound)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-success.svg)](https://github.com/Shashankt255/AeroHound)  

**AeroHound** – Lightweight Red Team & Wi-Fi penetration testing toolkit.  
Capture, crack, and report like a pro.  

---

    ▄█▀▀▀▄      ▄▀▀█▄  
   █▀      █   █      █  
   █      ▄▀   ▀▄     █  
   ▀▄   ▄▀       ▀▄  █  
     ▀▀▀           ▀▀  
 🐺 AeroHound – Hunt Networks Like a Wolf


---

## ✨ Features
- 🔹 Network recon & port scanning
- 🔹 WPA2/WPA3 handshake capture
- 🔹 802.1X (EAP/PEAP/MSCHAPv2) attacks
- 🔹 AI-assisted wordlist & attack generation
- 🔹 Automated reporting
- 🔹 Wi-Fi deauth (Linux, Alfa card required)
- 🔹 Modular plugin system

---

## 🚀 Getting Started
```bash
git clone https://github.com/Shashankt255/AeroHound.git
cd AeroHound
pip install -r requirements.txt

## 📌 Usage
python aerohound.py --scan 192.168.1.0/24 --report --ai

## 🔍 Network Scan
python aerohound.py --scan 192.168.1.0/24 --report --ai

## 📡 Wi-Fi Deauth (Linux only)
sudo python aerohound.py --wifi wlan0 --deauth

## 📝 Generate Report
python aerohound.py --scan 10.0.0.0/24 --report

## 📢 Credits

Developed & maintained by Shashankt255

🐺 AeroHound © 2025