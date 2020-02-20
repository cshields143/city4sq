import os, json
from tqdm import tqdm

rpath = 'cache/results/'
wpath = 'venues/'

invalids = []
empties = []

with open('citynames.json', 'r') as fp:
    cities = json.load(fp)

for fn in tqdm(os.listdir(rpath)):
    with open(rpath + fn, 'r') as fp:
        data = fp.read()
    justcity = fn.split('.')[0]
    fullcity = cities[justcity]
    if data == 'invalid city name':
        invalids.append(fullcity)
    elif data == '':
        empties.append(fullcity)
    else:
        with open(wpath + fn, 'w') as fp:
            fp.write(data)

with open('invalid_cities.txt', 'w') as fp:
    fp.write('\n'.join(sorted(invalids)))
with open('empty_cities.txt', 'w') as fp:
    fp.write('\n'.join(sorted(empties)))