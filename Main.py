# -*- coding: utf-8 -*-

from RandomCityMap import RandomCityMap
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from ReadCityTest import ReadCityTest

cityMap1 = RandomCityMap(10)
print(LocalSearch.search(cityMap1))
print(GeneticSearch.search(cityMap1))

cityMap1 = RandomCityMap(30)
print(LocalSearch.search(cityMap1))
print(GeneticSearch.search(cityMap1))

cityMap1 = ReadCityTest("test/gr17.tsp")
print(LocalSearch.search(cityMap1))
print(GeneticSearch.search(cityMap1))
