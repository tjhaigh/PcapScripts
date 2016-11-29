countrydict = {}
totalcount = 0

for x in range(0,10):
    inputfile = 'locations_part' + x + '.txt'
    with open(inputfile, 'r') as file_:
        for line in file_:
            line = line.strip()
            country = 
