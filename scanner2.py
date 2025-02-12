import ipaddress
import sys
import subprocess
import re
import os
import argparse
import socket

# Takes the cidr from the command line
parser = argparse.ArgumentParser(description='IP and port scanner')
parser.add_argument('--port', '-p', type=str, help='List of ports to scan, default scans first 1000 ports')
parser.add_argument('cidr', type=str, help='CIDR notation for IP range to scan')
args = parser.parse_args()

# Verifies your os type
OS_TYPE = os.name

# Sets the count modifier to the os type
COUNT = '-n' if OS_TYPE == 'nt' else '-c'

# Empty list to store ip addresses
ip_list = []

# Creates a network object
netIpv4Address = ipaddress.ip_network(args.cidr)

# Iterates through the network object and appends the ip addresses to the list
for i in netIpv4Address:
    ip_list.append(str(i))

# Function to parse port ranges and specific ports
def parse_ports(port_str):
    ports = set()
    for part in port_str.split(','):
        if '-' in part:
            start, end = part.split('-')
            ports.update(range(int(start), int(end) + 1))
        else:
            ports.add(int(part))
    return sorted(ports)

# Get the list of ports to scan
if args.port:
    ports = parse_ports(args.port)
else:
    ports = range(1, 1001)

# Function to check if a port is open
def is_port_open(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        return result == 0

# Iterates through the list of ip addresses and pings each one and checks ports
for ip in ip_list:
    try:
        result = subprocess.run(['ping', COUNT, '1', ip], capture_output=True, text=True)
        response = result.stdout
        if "Received = 1" in response and "Approximate" in response:
            print(f"{ip} (UP)")
            for port in ports:
                if is_port_open(ip, port):
                    print(f"  - Port {port} (OPEN)")
        else:
            print(f"{ip} (DOWN)")
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
