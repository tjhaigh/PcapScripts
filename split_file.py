infile = 'distinct_total.txt'
outfile = 'ips_split'

iplist = []

with open(infile, 'r') as file_:
    for line in file_:
        line = line.strip()
        iplist.append(line)

for x in range(0, 20):
    of = outfile + str(x) + '.txt'
    with open(of, 'w') as o:
        for y in range(0, 5000):
            if not iplist: break
            o.write(iplist.pop() + '\n')

