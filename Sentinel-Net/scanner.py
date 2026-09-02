import socket

target = "127.0.0.1"

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