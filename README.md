# IP and Port Scanner
This program scans IP addresses from a cidr address and if it's up, it  will check the ports on the address too. It will show what ports are open, but show ports that are used. Multiple ports can be inputed, but have to be seperated with a ',' and a range of ports can also be inputed when you use a '-'.

## Set up
There is not much you need to set this up. All you need is python downloaded (which you can get here: https://www.python.org/downloads/) and a program to run python like Virtual Studio Code or Pycharm

## Installation
To use this program, do the following:
1. Clone the repository into your machine
2. Run the program with the following command: "python scanner2.py -p (ports) (cidr address)" or use "python3 scanner2.py -p (ports) (cidr address)" if you're on Linux.

## Troubleshooting
I have not encountered any issues so far, but here are some pointers:

* Ensure python is installed on your machine
* Make sure there are no typos in the command line
* Make sure your address is a cidr address and not a normal IP address (it will only look at that single IP address)