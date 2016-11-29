from urllib.request import urlopen
from urllib.error import HTTPError
from time import sleep
import threading

apikey = '<my api key>'

outbase = 'locations_part'
inbase = 'ips_split'

def get_locations(ips):
    countrydict = {}
    count = 0
    while ips:
        #sleep(.75)
        ip = ips.pop()
        url = 'http://api.ipinfodb.com/v3/ip-country/?key='+apikey+'&ip='+ip
        try:
            response = urlopen(url)
        except Exception as e:
            #print(e)
            ips.append(ip)
            continue
        string = response.read().decode('utf-8')
        data = string.split(';')
        country = data[-1]
        if country in countrydict:
            countrydict[country] += 1
        else:
            countrydict[country] = 1
        count += 1
        print(count)
    return countrydict

def write_to_file(countries, x):
    if countries:
        of = outbase + x + '.txt'
        print(of)
        with open(of, 'w') as o:
            for key in countries.keys():
                o.write(key + ': ' + str(countries[key]) + '\n')

for x in range(10, 20):
    infile = inbase + str(x) + '.txt'
    ips = []
    print(infile)
    with open(infile, 'r') as i:
        for line in i:
            line = line.strip()
            ips.append(line)
    write_to_file(get_locations(ips), str(x))
