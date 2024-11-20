from scapy.all import sniff, IP, TCP
from collections import defaultdict
import socket
import time
import threading


# Detection thresholds
PORT_SCAN_THRESHOLD = 10  # Number of ports accessed in a short time for port scan detection
SYN_FLOOD_THRESHOLD = 100  # Number of SYN packets for SYN flood detection

# Define the port you want to monitor
MONITOR_PORT = 80  # Replace with the port you want to monitor

# Tracking dictionaries
port_access_count = defaultdict(set)
syn_packet_count = defaultdict(int)

# Suspicious IP and Port records
suspicious_ips = defaultdict(list)

# Function to fetch the current IP address dynamically

detected = False
def get_current_ip():
    try:
        # Connect to a public server to determine the current IP
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("8.8.8.8", 80))  # Google's public DNS
            return s.getsockname()[0]
    except Exception:
        return "No Network"

# Analyze each captured packet
def analyze_packet(packet):
    global detected
    while not detected:

        # Dynamically fetch the current IP address
        monitor_ip = get_current_ip()

        # Debugging: Print packet info to confirm capture
        if packet.haslayer(IP):
            print(f"Captured packet from {packet[IP].src} to {packet[IP].dst}")
        
        # Check if the packet is an IP packet with a TCP layer
        if packet.haslayer(IP) and packet.haslayer(TCP):
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            dport = packet[TCP].dport
            tcp_flags = packet[TCP].flags

            # Detect SYN packets (indicates potential SYN flood or port scan)
            if tcp_flags == "S":
                syn_packet_count[ip_src] += 1
                # Check for SYN Flood
                if syn_packet_count[ip_src] > SYN_FLOOD_THRESHOLD:

                    print(f"[ALERT] Possible SYN Flood detected from IP: {ip_src}")
                    suspicious_ips[ip_src].append("Possible SYN Flood")
                    detected = True

            
                # Track accessed ports for port scan detection
                port_access_count[ip_src].add(dport)
                if len(port_access_count[ip_src]) > PORT_SCAN_THRESHOLD:
                    print(f"[ALERT] Possible Port Scan detected from IP: {ip_src} (accessed ports: {len(port_access_count[ip_src])})")
                    suspicious_ips[ip_src].append(f"Possible Port Scan (accessed {len(port_access_count[ip_src])} ports)")

            # Check for specific IP address alert
            if ip_src == monitor_ip or ip_dst == monitor_ip:
                print(f"[ALERT] Traffic involving monitored IP {monitor_ip} detected!")

            # Check for specific port alert
            if dport == MONITOR_PORT:
                print(f"[ALERT] Traffic involving monitored port {MONITOR_PORT} detected!")

# Function to reset tracking dictionaries periodically
def reset_counts():
    global port_access_count, syn_packet_count
    while not detected:
        time.sleep(3)  # Reset every 60 seconds
        port_access_count.clear()
        syn_packet_count.clear()
        print("Counters reset")

# Function to display suspicious IPs and ports
def display_suspicious_ips():
    global detected

    
    while not detected:
        time.sleep(1)  # Display suspicious IPs every 10 seconds
        if suspicious_ips:
            print("\nSuspicious IPs and Activities Detected:")
            detected = True
            for ip, activities in suspicious_ips.items():
                print(f"IP: {ip} - Activities: {', '.join(activities)}")
            if detected:
                break

        else:
            print("No suspicious activity detected.")
        time.sleep(10)

        if detected:
            break

# Main function to start IDS
def start_ids(interface=None):
    print("Starting Intrusion Detection System...")
    # Sniff packets on the specified network interface
    sniff(iface=interface, prn=analyze_packet, store=False)

# Specify the interface you want to sniff on, e.g., 'Wi-Fi' or 'Ethernet'
network_interface = "Wi-Fi"  # Replace with your active network interface name

# Start the reset thread
reset_thread = threading.Thread(target=reset_counts, daemon=True)
reset_thread.start()

# Start the display thread for suspicious IPs
display_thread = threading.Thread(target=display_suspicious_ips, daemon=True)
display_thread.start()

# Start the IDS on the specified interface
start_ids(interface=network_interface)
