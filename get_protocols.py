from scapy.all import *
import os

pcapdir = '/home/trevor/Documents/IoT_Project/PcapData/pcap-total/'

protocols = {}
files = [f for f in os.listdir(pcapdir) if os.path.isfile(os.path.join(pcapdir, f))]

def readfiles():
    for file_ in files:
        try:
            for pkt in PcapReader(os.path.join(pcapdir, file_)):
                l = list(expand(pkt))
                p = ":".join(l)
                if p in protocols:
                    protocols[p] += 1
                else:
                    protocols[p] = 1
        except Exception as e:
            print(e)

def expand(x):
    yield x.name
    while x.payload:
        x = x.payload
        yield x.name


readfiles()

with open("protocols-total.txt", 'w') as outfile:
    for key in protocols.keys():
        outfile.write(key + ':     ' + str(protocols[key]) + '\n')
