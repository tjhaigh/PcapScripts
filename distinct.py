from scapy.all import *
import os

pcapdir = "/home/trevor/Documents/IoT_Project/PcapData/pcap-total/"
pcapdir2 = "/home/trevor/Documents/IoT_Project/PcapData/pcap/"
testpcapdir = "/home/trevor/Documents/IoT_Project/project/testpcap/"
errorpkts = open("packeterrors_total.txt", "w")
errorfiles = open("fileerrors_total.txt", "w")
ipfile = open("distincttotal_from_packets.txt", "w")
# Get list of all files in directory
files = [f for f in os.listdir(pcapdir) if os.path.isfile(os.path.join(pcapdir, f))]
files2 = [f for f in os.listdir(pcapdir2) if os.path.isfile(os.path.join(pcapdir2, f))]
testfiles = [f for f in os.listdir(testpcapdir) if os.path.isfile(os.path.join(testpcapdir, f))]
iplist = []
errorlist = []

def read_files(files):
    for _file in files:
        try:
            pkts = rdpcap(os.path.join(pcapdir, _file))
        except Exception as e:
            print(e)
            errorlist.append(_file)
            errorfiles.write(_file+"\n")
            continue
        for pkt in pkts:
            if IP not in pkt: 
                errorpkts.write(_file+"\n")
                continue
            src = pkt.getlayer(IP).src
            dst = pkt.getlayer(IP).dst
            if src not in iplist:
                iplist.append(src)
            if dst not in iplist:
                iplist.append(dst)

read_files(pcapdir)

for ip in iplist:
    ipfile.write(ip+"\n")

ipfile.close()
