import os

file1 = "distinctip.txt"
file2 = "distinctready.txt"
outfile = "distinct_total.txt"
iplist = set()

with open(file1, "r") as file_:
    for line in file_:
        line = line.strip()
        iplist.add(line)

with open(file2, "r") as file_:
    for line in file_:
        line = line.strip()
        iplist.add(line)

with open(outfile, "w") as out:
    for ip in iplist:
        out.write(ip + "\n")
