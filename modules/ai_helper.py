def suggest(results):
    print("[*] AI Assistant Suggestions:")
    if 22 in results["open_ports"]:
        print(" - SSH detected: Try brute-force or weak key attacks (Pro feature).")
    if 80 in results["open_ports"] or 443 in results["open_ports"]:
        print(" - Web service found: Recommend web vulnerability scanning.")
    if not results["open_ports"]:
        print(" - No open ports, consider WiFi-based attacks (Linux module available).")
