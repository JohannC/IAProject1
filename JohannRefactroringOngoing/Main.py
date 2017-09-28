# -*- coding: utf-8 -*-

import datetime
from RandomCityMap import RandomCityMap
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from GeneticSearchLocalMinimum import GeneticSearchLocalMinimum
from ReadCityTest import ReadCityTest
from GeneticSearchLocalMinimumCrazy import GeneticSearchLocalMinimumCrazy
'''
cityMap1 = RandomCityMap(10)
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search 10 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search 10 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum 10 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))


cityMap1 = RandomCityMap(30)
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search 30 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search 30 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum 30 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

cityMap1 = ReadCityTest("test/gr17.tsp")
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search test/gr17.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search test/gr17.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/gr17.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

cityMap1 = ReadCityTest("test/gr21.tsp")
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search test/gr21.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search test/gr21.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/gr21.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

cityMap1 = ReadCityTest("test/gr24.tsp")
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search test/gr24.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search test/gr24.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/gr24.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

'''
cityMap1 = ReadCityTest("test/hk48.tsp")

startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search test/hk48.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

startTime = datetime.datetime.now()
path = LocalSearch.searchTrial(cityMap1)
endTime = datetime.datetime.now()
print('Local Search Trial  test/hk48.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search test/hk48.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

startTime = datetime.datetime.now()
#path = GeneticSearchLocalMinimum(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum test/hk48.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))

startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimumCrazy(cityMap1).search()
endTime = datetime.datetime.now()
print('GeneticSearchMinimumCrazy test/hk48.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))


cityMap1 = ReadCityTest("test/si175.tsp")

startTime = datetime.datetime.now()
path = LocalSearch.searchTrial(cityMap1)
endTime = datetime.datetime.now()
print('Local Search trial test/si175.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search test/si175.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimumCrazy(cityMap1).search()
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum crazy test/si175.tsp : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
