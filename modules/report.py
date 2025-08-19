def generate(results):
    print("[*] Generating report...")
    with open("report.txt", "w") as f:
        f.write("AeroHound Scan Report\n")
        f.write("====================\n")
        f.write(f"Target: {results['target']}\n")
        f.write(f"Open Ports: {results['open_ports']}\n")
    print("[+] Report saved as report.txt")
