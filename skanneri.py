import socket
import threading
import sys

if len(sys.argv) != 2:
    print("Usage: python skanneri.py <ip>")
    sys.exit(1)

target = sys.argv[1]
open_ports = []

def scan_port(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    try:
        conn = sock.connect((target, port))
        open_ports.append(port)
    except:
        pass

for port in range(80, 444):
    thread = threading.Thread(target=scan_port, args=(port,))
    thread.start()

for thread in threading.enumerate():
    if thread is not threading.currentThread():
        thread.join()

print(f"Open ports on {target}: {open_ports}")