import subprocess
from scapy.all import *

def get_interfaces():
    result = subprocess.run(["netsh", "interface", "show", "interface"],
    capture_output=True, text=True)
    output_lines = result.stdout.splitlines()[3:]
    interfaces = [line.split() [3] for line in output_lines if len(line.split
    ()) >= 4]
    return interfaces

def packet_handler(packet):
    if packet.haslayer (Raw):
        print("Captured Packet:")
        print(str(packet))

# Get list of network interfaces
interfaces = get_interfaces()

# Print a list of network interfaces for the user to choose from
print("List of network interfaces:")
for i, iface in enumerate (interfaces, start=1):
    print(f"{i}. {iface}")

# User select network interface
choice = int(input("Select a network interface (enter a number): "))
selected_iface = interfaces [choice - 1]

# Capture packets on selected network interface
sniff(iface=selected_iface, prn=packet_handler, filter="tcp")