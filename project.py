from scapy.all import *

class comm:
    count = 1

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

pkts = rdpcap("test.pcap")

packets = []
for pkt in pkts:
    src = pkt.getlayer(IP).src
    dst = pkt.getlayer(IP).dst
    print(pkt[Ether].dst)
    if not packets: 
        packets.append(comm(src, dst))
    else:
        matched = False
        for p in packets:
            if src == p.src and dst == p.dst:
                p.count += 1
                matched = True
                break
        if not matched:
            packets.append(comm(src, dst))

for p in packets:
    print(p.src, "   ", p.dst, "   Count:", p.count)
