#Project: Port Scanner with Multithreading
# Rajib Sharma (sharma.com)
"""
class16_scanner.py
Simple multithreaded port scanner (educational).
Usage:
    python3 class16_scanner.py <target> [start_port] [end_port] [max_threads]

Example:
    python3 class16_scanner.py example.com 1 1024 100
"""
import sys
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

# small service name map for common ports
SERVICE_MAP = {
    20: "FTP-data", 21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP", 80: "HTTP", 110: "POP3", 123: "NTP",
    143: "IMAP", 161: "SNMP", 194: "IRC", 443: "HTTPS", 587: "SMTP-submission",
    993: "IMAPS", 995: "POP3S", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    8080: "HTTP-alt"
}

def scan_port(target_ip: str, port: int, timeout: float = 1.0) -> (int, bool):
    """
    Try to connect to (target_ip, port). Return tuple (port, is_open).
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((target_ip, port))
            return port, (result == 0)
    except Exception:
        return port, False

def parse_args():
    """
    Parse command line arguments and return (target, start_port, end_port, max_threads).
    """
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    target = sys.argv[1]
    start_port = int(sys.argv[2]) if len(sys.argv) >= 3 else 1
    end_port = int(sys.argv[3]) if len(sys.argv) >= 4 else 1024
    max_threads = int(sys.argv[4]) if len(sys.argv) >= 5 else 100

    # sanitize values
    if start_port < 1:
        start_port = 1
    if end_port > 65535:
        end_port = 65535
    if start_port > end_port:
        start_port, end_port = end_port, start_port
    if max_threads < 1:
        max_threads = 10

    return target, start_port, end_port, max_threads

def main():
    target, start_port, end_port, max_threads = parse_args()

    # Resolve target
    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"[!] Error: could not resolve hostname: {target}")
        sys.exit(1)

    print("="*60)
    print(f"Target: {target} ({target_ip})")
    print(f"Port range: {start_port} - {end_port}")
    print(f"Max threads: {max_threads}")
    print(f"Start time: {datetime.now()}")
    print("="*60)

    open_ports = []

    ports = range(start_port, end_port + 1)

    try:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            future_to_port = {executor.submit(scan_port, target_ip, port): port for port in ports}
            for future in as_completed(future_to_port):
                port = future_to_port[future]
                try:
                    port, is_open = future.result()
                    if is_open:
                        service = SERVICE_MAP.get(port, "unknown")
                        print(f"[+] Port {port} is OPEN\tService: {service}")
                        open_ports.append((port, service))
                except Exception:
                    # ignore individual scan errors
                    pass

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"[!] Error during scanning: {e}")
        sys.exit(1)

    print("\n" + "="*60)
    print(f"Scan completed at: {datetime.now()}")
    print(f"Open ports found: {len(open_ports)}")
    for port, service in sorted(open_ports):
        print(f"    - {port}/tcp  ({service})")
    print("="*60)

if __name__ == "__main__":
    main()

