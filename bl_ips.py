import subprocess
import os
import dns.resolver
from concurrent.futures import ThreadPoolExecutor
import threading
import time

ipfile = 'distinct_total.txt'

cmdtxt = '/home/trevor/Documents/IoT_Project/project/blcheck/blcheck -qp '

blacklists = []
counts = {}
lock = threading.Lock()
threadcount = 0

def check_ip(ip, ipReversed):
    badcount = 0
    for bl in blacklists:
        try:
            resolver = dns.resolver.Resolver()
            query = ipReversed + '.' + bl
            r = resolver.query(query, 'A')
            badcount += 1
        except Exception as e:
            pass
    
    lock.acquire()
    global counts
    counts[ip] = badcount
    global threadcount
    threadcount -= 1
    lock.release()
    return badcount

def test(msg, msg2):
    time.sleep(1)
    print(msg, msg2)
    lock.acquire()
    global threadcount
    threadcount -= 1
    lock.release()

with open('bl.txt', 'r') as blfile:
    for line in blfile:
        line = line.strip()
        blacklists.append(line)

with open('distinct_total.txt', 'r') as infile:
    pool = ThreadPoolExecutor(100)
    count = 1
    for line in infile:
        line = line.strip()
        ip = line.split('.')
        ip.reverse()
        ip = '.'.join(ip)
        while 1:
            if threadcount < 99:
                print(count)
                future = pool.submit(check_ip, line, ip)
                threadcount += 1
                count += 1
                break
    

with open('blacklisted.txt', 'w') as outfile:
    for key in counts.keys():
        outfile.write(key + ': ' + str(counts[key]))
