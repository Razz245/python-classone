#!/usr/bin/env python3
# Advanced Network Scanner - Capstone Project
# This script scans a range of ports on a target IP address
# and identifies open ports along with their common services.
#Rajib Sharma  - 25 October 2025

# Advanced Network Scanner - Capstone Project
# Rajib Sharma  - 25 October 2025 (fixed colorama handling)

import socket
import threading
import sys
import time
from queue import Queue
from datetime import datetime

# Try import colorama; if not available, provide no-color fallback
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except Exception:
    class _NoColor:
        def __getattr__(self, name):
            return ''
    Fore = Style = _NoColor()

# Thread queue and state
queue = Queue()
open_ports = []
lock = threading.Lock()

# Common ports dictionary
common_ports = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP Proxy"
}

def scan_port(ip, port):
    """Scan a single port"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            service = common_ports.get(port, "Unknown Service")
            with lock:
                open_ports.append((ip, port, service))
            print(f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} {ip}:{port} → {Fore.CYAN}{service}{Style.RESET_ALL}")
    except Exception:
        # keep quiet on per-port errors
        return

def threader(ip):
    while True:
        try:
            port = queue.get_nowait()
        except Exception:
            break
        scan_port(ip, port)
        queue.task_done()

def banner():
    print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}      🔥 Advanced Network Scanner | Capstone Project 🔥{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")

def main():
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} <target_ip_or_host> <start_port> <end_port>")
        sys.exit(1)

    target_host = sys.argv[1]
    try:
        start_port = int(sys.argv[2])
        end_port = int(sys.argv[3])
    except ValueError:
        print("Start and end ports must be integers.")
        sys.exit(1)

    # resolve hostname
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"[!] Could not resolve: {target_host}")
        sys.exit(1)

    banner()
    print(f"{Fore.CYAN}Target: {Style.RESET_ALL}{target_host} ({target_ip})")
    print(f"{Fore.CYAN}Port Range: {Style.RESET_ALL}{start_port}-{end_port}")
    print(f"{Fore.CYAN}Started at: {Style.RESET_ALL}{datetime.now()}")
    print(f"{Fore.YELLOW}{'-'*60}{Style.RESET_ALL}")

    # enqueue ports
    for p in range(max(1, start_port), min(65535, end_port) + 1):
        queue.put(p)

    # start threads
    threads = []
    thread_count = 200
    t_start = time.time()
    for _ in range(thread_count):
        t = threading.Thread(target=threader, args=(target_ip,))
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        queue.join()
    except KeyboardInterrupt:
        print("\n[!] Interrupted by user. Exiting...")

    duration = round(time.time() - t_start, 2)
    print(f"{Fore.YELLOW}{'-'*60}{Style.RESET_ALL}")
    print(f"Scan complete in {duration} seconds")
    print(f"Open Ports Found: {len(open_ports)}")

    # Save results
    if open_ports:
        fname = f"scan_results_{int(time.time())}.txt"
        with open(fname, "w", encoding="utf-8") as f:
            for ip, port, service in open_ports:
                f.write(f"{ip}:{port} → {service}\n")
        print(f"{Fore.GREEN}Results saved to {fname} ✅{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}{'='*60}{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
