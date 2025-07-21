import socket

# Create raw socket to capture packets
sniffer = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

print("Starting packet sniffer... Press Ctrl+C to stop.\n")

try:
    while True:
        raw_data, addr = sniffer.recvfrom(65536)
        print(f"Packet from {addr}: {raw_data[:32]}")
except KeyboardInterrupt:
    print("\nSniffer stopped.")
