@'
#!/usr/bin/env python3
import argparse
from modules import scan, report, ai_helper, wifi

def main():
    parser = argparse.ArgumentParser(prog="AeroHound",
                                     description="AeroHound Community Edition - Recon & WiFi Testing Tool")

    parser.add_argument("--scan", help="Scan a target IP or range (example: 192.168.1.0/24)")
    parser.add_argument("--report", help="Generate a report file", action="store_true")
    parser.add_argument("--ai", help="Get AI suggestions from scan results", action="store_true")
    parser.add_argument("--wifi-scan", help="Scan WiFi networks (Linux only)", action="store_true")
    parser.add_argument("--wifi-deauth", help="Deauth a target client (Linux only, requires monitor mode). Usage: <BSSID> <client_mac>", nargs=2)

    args = parser.parse_args()

    if args.scan:
        results = scan.run_scan(args.scan)
        print("[+] Scan completed")
        if args.ai:
            ai_helper.suggest(results)
        if args.report:
            report.generate(results)

    if args.wifi_scan:
        wifi.scan_networks()

    if args.wifi_deauth:
        bssid, client = args.wifi_deauth
        wifi.deauth(bssid, client)

if __name__ == "__main__":
    main()
'@ | Set-Content aerohound.py