from scapy.all import *
import os

pcapdir = '/home/trevor/Documents/IoT_Project/project/justcamera/'


sports = {}
dports = {}
files = [f for f in os.listdir(pcapdir) if os.path.isfile(os.path.join(pcapdir, f))]

def readfiles():
    for file_ in files:
        for pkt in PcapReader(os.path.join(pcapdir, file_)):
            if IP in pkt:
                src = pkt.getlayer(IP).src
                dst = pkt.getlayer(IP).dst
                if TCP in pkt:
                    sport = pkt.getlayer(TCP).sport
                    dport = pkt.getlayer(TCP).dport
                    if src in sports:
                        if sport in sports[src]:
                            sports[src][sport] += 1
                        else:
                            sports[src][sport] = 1
                    else:
                        sports[src] = {}
                        sports[src][sport] = 1
                    if dst in dports:
                        if dport in dports[dst]:
                            dports[dst][dport] += 1
                        else:
                            dports[dst][dport] = 1
                    else:
                        dports[dst] = {}
                        dports[dst][dport] = 1

def printdict(d, outfile):
    for key in d.keys():
        outfile.write(key+":\n")
        for k in d[key].keys():
            outfile.write('\t'+str(k)+': '+str(d[key][k])+'\n')

readfiles()

with open('ports.txt', 'w') as of:
    of.write("SOURCE\n")
    printdict(sports, of)
    of.write("DST\n")
    printdict(dports, of)

