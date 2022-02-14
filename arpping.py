# Simple Scapy script to ARP ping. Usage example shown below

#! /usr/bin/env python
from scapy.all import srp,Ether,ARP,conf
# or from scapy.all import *
import sys

if len(sys.argv) != 2:
    print("Usage: arpping.py <network>")
    print("e.g.: arpping 10.10.10.0/24")
    sys.exit(1)

conf.verb=0
ans,unans= srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=sys.argv[1]),timeout=2)
for s,r in ans:
    print(r.sprintf("%Ether.src% %ARP.psrc%")) 
