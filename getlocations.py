import json
from urllib.request import urlopen
from urllib.error import HTTPError
from geoip import geolite2
from time import sleep

outfile = 'countries2.txt'
nextfile = open('ipsnext.txt', 'w')
iplist = []
countrydict = {}
count = 0

apikey = '6f3d4a0fa879cf800c3e37bfa8bfc2731642249a503bb8d62089488f3382bf78'

with open('distinct_total.txt', 'r') as f:
    for line in f:
        line = line.strip()
        iplist.append(line)
        
while iplist:
    sleep(1)
    line = iplist.pop(0)
    url = 'http://api.ipinfodb.com/v3/ip-country/?key='+apikey+'&ip='+line
    try:
        response = urlopen(url)
    except Exception as e:
        print(e)
        iplist.append(line)
        for ip in iplist:
            nextfile.write(ip+'\n')
        break
    
    string = response.read().decode('utf-8')
    print(string.split(';'))
   # data = json.loads(string)
   # if 'country' in data:
   #     count += 1
   #     print(count)
   #     country = data['country']
   #     if country in countrydict:
   #         countrydict[country] += 1
   #     else:
   #         countrydict[country] = 1
    #match = geolite2.lookup(line)
    #if match != None:
    #    print(match.country)
    #    outfile.writeline(match.country)

with open(outfile, 'w') as f:
    for key in countrydict.keys():
        f.write(key + ": " + str(countrydict[key])+'\n')
