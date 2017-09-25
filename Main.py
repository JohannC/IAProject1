# -*- coding: utf-8 -*-

from RandomCityMap import RandomCityMap
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch

cityMap1 = RandomCityMap(10)
print(LocalSearch.search(cityMap1))
print(GeneticSearch.search(cityMap1))

cityMap1 = RandomCityMap(30)
print(LocalSearch.search(cityMap1))
print(GeneticSearch.search(cityMap1))


