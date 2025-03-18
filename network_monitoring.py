from scapy.all import *

def monitor_traffic(packet):
    """
    Monitors network traffic and prints alerts for suspicious SYN packets (indicating potential DDoS).
    """
    if packet.haslayer(TCP):
        if packet[TCP].flags == "S":  # SYN packet, part of potential DDoS attack
            print(f"Suspicious SYN packet detected: {packet[IP].src} -> {packet[IP].dst}")

# Start sniffing network traffic
sniff(prn=monitor_traffic, store=0)
