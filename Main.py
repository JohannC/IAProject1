# -*- coding: utf-8 -*-

import datetime
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from GeneticSearchLocalMinimum import GeneticSearchLocalMinimum
from ReadCityMapFromFile import ReadCityMapFromFile

seed = 10


cityMap1 = ReadCityMapFromFile.read("test/gr17.tsp")
startTime = datetime.datetime.now()
path = LocalSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Local Search test/gr17.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search test/gr17.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/gr17.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

cityMap1 = ReadCityMapFromFile.read("test/gr21.tsp")
startTime = datetime.datetime.now()
path = LocalSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Local Search test/gr21.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search test/gr21.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/gr21.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

cityMap1 = ReadCityMapFromFile.read("test/gr24.tsp")
startTime = datetime.datetime.now()
path = LocalSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Local Search test/gr24.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search test/gr24.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/gr24.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))


cityMap1 = ReadCityMapFromFile.read("test/hk48.tsp")

startTime = datetime.datetime.now()
path = LocalSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Local Search - hk48.tsp : '+str(cityMap1.getTotalCost(path))+' - '+str(endTime - startTime))

startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search - hk48.tsp : '+str(cityMap1.getTotalCost(path))+' - '+str(endTime - startTime))

startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum - hk48.tsp : '+str(cityMap1.getTotalCost(path))+' - '+str(endTime - startTime))

cityMap1 = ReadCityMapFromFile.read("test/si175.tsp")

startTime = datetime.datetime.now()
path = LocalSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Local Search test/si175.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search test/si175.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1, seed).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/si175.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

