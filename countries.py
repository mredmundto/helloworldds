import collections
from __future__ import division

population_dict2010 = collections.defaultdict(int)
population_dict2100 = collections.defaultdict(int)
with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
            population_dict2010[line[0]] += line[5]
        if line[1] == 'Total National Population':
            population_dict2100[line[0]] += line[6]

print(population_dict2010)
print(population_dict2100)

print(float(population_dict2100['Europe']/population_dict2010['Europe'] - 1 ))
print(float(population_dict2100['Oceania']/population_dict2010['Oceania'] - 1 ))
print(float(population_dict2100['Africa']/population_dict2010['Africa'] - 1 ))
print(float(population_dict2100['Asia']/population_dict2010['Asia'] - 1 ))
print(float(population_dict2100['North America']/population_dict2010['North America'] - 1 ))
print(float(population_dict2100['South America']/population_dict2010['South America'] - 1 ))