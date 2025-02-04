import ipaddress
import sys
import os
import re
import argparse

# Takes the cidr from the command line
cidr = sys.argv[1]

parser = argparse.ArgumentParser(description='Simple TCP Port Scanner using Scapy')
parser.add_argument('--port', '-p', type=str, help='List of ports to scan (e.g., 22,80-100), default scans first 1000 ports')

# Verifies your os type
OS_TYPE = os.name

# Sets the count modifier to the os type
COUNT = '-n' if OS_TYPE == 'nt' else '-c'

# Empty list to store ip addresses
ip_list = []

# Creates a network object
netIpv4Address = ipaddress.ip_network(cidr)

# Iterates through the network object and appends the ip addresses to the list
for i in netIpv4Address:
    ip_list.append(str(i))

# Iterates through the list of ip addresses and pings each one and gets the time it takes to respond. try and except block to catch any errors
for ip in ip_list:
    try:
        response = os.popen(f"ping {ip} {COUNT} 1").read()
        if "Received = 1" in response and "Approximate" in response:
            match = re.search(r'time[=<]\s*(\d+ms)', response)
            print(f"{ip} - UP ({match.group(1)})")
        else:
            print(f"{ip} - DOWN (No Response)")
    except Exception as e:
        print(f"Error pinging {ip}: {e}")
