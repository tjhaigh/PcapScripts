# combine the locations
import operator

locationdict = {}
total = 0
for x in range(0, 20):
    with open('locations_part' + str(x) + '.txt', 'r') as file_:
        for line in file_:
            line = line.strip()
            parts = line.split(':')
            country = parts[0]
            count = int(parts[1])
            total += count
            if country in locationdict:
                locationdict[country] += count
            else:
                locationdict[country] = count

locationdict['total'] = total
sorteddict = sorted(locationdict.items(), key=operator.itemgetter(1), reverse=True)
with open('locations_total.txt', 'w') as file_:
    for item in sorteddict:
        country = item[0]
        count = item[1]
        file_.write(country+': '+str(count)+'\n')
