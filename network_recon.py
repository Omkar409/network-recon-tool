#!/usr/bin/env python3
"""
Network Reconnaissance Tool for Kali Linux
Features: Port Scanning, Banner Grabbing, Service Detection
"""

import socket
import sys
import threading
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
import argparse

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

class NetworkRecon:
    def __init__(self, target, start_port=1, end_port=1024, threads=100):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.open_ports = []
        self.banner_results = {}
        self.lock = threading.Lock()
        self.ports_list = None
        
        self.common_services = {
            21: 'FTP', 22: 'SSH', 23: 'Telnet', 25: 'SMTP',
            53: 'DNS', 80: 'HTTP', 110: 'POP3', 143: 'IMAP',
            443: 'HTTPS', 3306: 'MySQL', 3389: 'RDP',
            5432: 'PostgreSQL', 8080: 'HTTP-Proxy', 8443: 'HTTPS-Alt'
        }

    def resolve_target(self):
        try:
            ip = socket.gethostbyname(self.target)
            print(f"{Colors.OKGREEN}[+] Target resolved: {self.target} -> {ip}{Colors.ENDC}")
            return ip
        except socket.gaierror:
            print(f"{Colors.FAIL}[-] Could not resolve {self.target}{Colors.ENDC}")
            sys.exit(1)

    def scan_port(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                with self.lock:
                    self.open_ports.append(port)
                    service = self.common_services.get(port, 'Unknown')
                    print(f"{Colors.OKGREEN}[+] Port {port}/tcp OPEN - {service}{Colors.ENDC}")
                    
                    banner = self.grab_banner(sock, port)
                    if banner:
                        self.banner_results[port] = banner
                        print(f"    {Colors.OKBLUE}Banner: {banner[:100]}{Colors.ENDC}")
            
            sock.close()
        except:
            pass

    def grab_banner(self, sock, port):
        try:
            if port in [80, 8080, 8443]:
                sock.send(b"HEAD / HTTP/1.1\r\nHost: " + self.target.encode() + b"\r\n\r\n")
            else:
                sock.send(b"\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            return banner if banner else None
        except:
            return None

    def run_scan(self):
        print(f"\n{Colors.HEADER}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}NETWORK RECONNAISSANCE TOOL{Colors.ENDC}")
        print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}")
        print(f"Target: {self.target}")
        
        if self.ports_list:
            ports_to_scan = self.ports_list
            print(f"Ports: {', '.join(map(str, self.ports_list))}")
        else:
            ports_to_scan = list(range(self.start_port, self.end_port + 1))
            print(f"Port Range: {self.start_port}-{self.end_port}")
            
        print(f"Threads: {self.threads}")
        print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}\n")
        
        self.target = self.resolve_target()
        start_time = time.time()
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            futures = {executor.submit(self.scan_port, port): port for port in ports_to_scan}
            
            for future in as_completed(futures):
                pass
        
        duration = time.time() - start_time
        print(f"\n{Colors.HEADER}{'='*60}{Colors.ENDC}")
        print(f"{Colors.BOLD}SCAN SUMMARY{Colors.ENDC}")
        print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}")
        print(f"Open Ports Found: {len(self.open_ports)}")
        print(f"Scan Duration: {duration:.2f} seconds")
        print(f"Scan Rate: {len(ports_to_scan) / duration:.0f} ports/sec")
        
        if self.open_ports:
            print(f"\n{Colors.OKGREEN}Open Ports:{Colors.ENDC}")
            for port in sorted(self.open_ports):
                service = self.common_services.get(port, 'Unknown')
                banner = self.banner_results.get(port, '')
                print(f"  {port}/tcp - {service} {f'({banner[:50]})' if banner else ''}")
        
        print(f"{Colors.HEADER}{'='*60}{Colors.ENDC}\n")

    def ping_sweep(self, network):
        print(f"\n{Colors.WARNING}[*] Starting Ping Sweep on {network}.0/24{Colors.ENDC}\n")
        live_hosts = []

        def ping_host(ip):
            import subprocess
            try:
                result = subprocess.run(
                    ['ping', '-c', '1', '-W', '1', ip],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                if result.returncode == 0:
                    live_hosts.append(ip)
                    print(f"{Colors.OKGREEN}[+] Host {ip} is UP{Colors.ENDC}")
            except:
                pass

        with ThreadPoolExecutor(max_workers=50) as executor:
            for i in range(1, 255):
                executor.submit(ping_host, f"{network}.{i}")

        print(f"\n{Colors.OKGREEN}[+] Found {len(live_hosts)} live hosts{Colors.ENDC}")
        return live_hosts

def main():
    parser = argparse.ArgumentParser(
        description='Network Reconnaissance Tool - Kali Linux',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 network_recon.py -t 192.168.1.1
  python3 network_recon.py -t scanme.nmap.org -p 1-65535 -T 200
  python3 network_recon.py -t target.com -p 22,80,443
  python3 network_recon.py -t 192.168.1.1 --ping-sweep 192.168.1
        """
    )

    parser.add_argument('-t', '--target', required=True, help='Target IP or hostname')
    parser.add_argument('-p', '--ports', default='1-1024', help='Port range (e.g., 1-1024 or 22,80,443)')
    parser.add_argument('-T', '--threads', type=int, default=100, help='Number of threads (default: 100)')
    parser.add_argument('--ping-sweep', metavar='NETWORK', help='Ping sweep network (e.g., 192.168.1)')

    args = parser.parse_args()

    if ',' in args.ports:
        ports_list = [int(p.strip()) for p in args.ports.split(',')]
        scanner = NetworkRecon(args.target, threads=args.threads)
        scanner.ports_list = ports_list
        scanner.run_scan()
    elif '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
        scanner = NetworkRecon(args.target, start_port, end_port, args.threads)
        scanner.run_scan()
    else:
        start_port = end_port = int(args.ports)
        scanner = NetworkRecon(args.target, start_port, end_port, args.threads)
        scanner.run_scan()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.FAIL}[-] Scan interrupted by user{Colors.ENDC}")
        sys.exit(0)
