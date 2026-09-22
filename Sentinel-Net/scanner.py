import socket

target = "127.0.0.1"

hostname_to_check = "google.com"
try:
    resolved_ip = socket.gethostbyname(hostname_to_check)
    print(f"DNS Lookup: {hostname_to_check} = {resolved_ip}")
except socket.gaierror:
    print(f"DNS Lookup failed for {hostname_to_check}")

found = False

for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((target, port))
        if result == 0:
                print(f"Port {port}: OPEN")
                found = True
        sock.close()

if not found:
        print("No open ports found.")