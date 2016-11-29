from scapy.all import *
import os

pcapdir = '/home/trevor/Documents/IoT_Project/PcapData/pcap-total/'

files = [f for f in os.listdir(pcapdir) if os.path.isfile(os.path.join(pcapdir, f))]

errorfiles = open('error_files.txt', 'w')

filterip = '192.168.186.46'
filtermac = '00:16:8c:de:ad:32'
pktlist = []

outfile = 'camerapcap'
x = 0

for file_ in files:
    print(file_)
    try:
        for pkt in PcapReader(os.path.join(pcapdir, file_)):
            keep = False
            if IP in pkt:
                src = pkt.getlayer(IP).src
                dst = pkt.getlayer(IP).dst
                if src == filterip or dst == filterip:
                    keep = True
            if Ether in pkt:
                src = pkt.getlayer(Ether).src
                dst = pkt.getlayer(Ether).dst
                if src == filtermac or dst == filtermac:
                    keep = True
            if keep:
                pktlist.append(pkt)
                if len(pktlist) > 100000:
                    wrpcap(outfile+str(x)+'.pcap', pktlist)
                    x += 1
                    pktlist = []
    except Exception as e:
        print('Error',e,file_)

wrpcap(outfile+str(x)+'.pcap', pktlist)



errorfiles.close()
