# PcapScripts

Collection of scripts used to parse and analyze large amounts of network traffic.






### bl-ips.py
Used to check ips against various blacklists.

### combine_locations.py
When location processing was done, the results were contained within different files. This script merged these results.

### distinct.py
This script was used to get unique IP addresses found in the pcap files

### distinct_from_file.py
The pcap files were split into 2 folders.  distinct.py was run on those two folders and then this script finds the unique IPs from within the resulting txt files.

### get_camera_traffic.py
This was used to filter the traffic down to just packets involving the IP Camera. This script can be modified to filter by any IP and MAC

### getlocations_div.py
The IPs were split into several files and this script pulled in data from one file at a time and got the locations. The data was split up so that if any issues happened during execution, not all progress would be lost.

  
