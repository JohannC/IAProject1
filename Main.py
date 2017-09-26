# -*- coding: utf-8 -*-

import datetime
from RandomCityMap import RandomCityMap
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from GeneticSearchLocalMinimum import GeneticSearchLocalMinimum


cityMap1 = RandomCityMap(10)
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search 10 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Genetic Search 10 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearchLocalMinimum.search(cityMap1)
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum 10 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))


cityMap1 = RandomCityMap(30)
startTime = datetime.datetime.now()
path = LocalSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Local Search 30 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
path = GeneticSearch.search(cityMap1)
endTime = datetime.datetime.now()
print('Genetic Search 30 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))
startTime = datetime.datetime.now()
#path = GeneticSearchLocalMinimum.search(cityMap1)
endTime = datetime.datetime.now()
print('Genetic Search with Local minimum 30 cities : '+str(cityMap1.getTotalCost(path))+' in '+str(endTime - startTime))



