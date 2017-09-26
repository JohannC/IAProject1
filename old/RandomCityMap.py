# -*- coding: utf-8 -*-
from CityMap import CityMap
from random import randint

class RandomCityMap(CityMap):
    
    MAX_COST  = 100
    
    def __init__(self, numberOfCities):
        cityList = RandomCityMap.__generateCityList(numberOfCities)
        costs = RandomCityMap.__generateCosts(cityList)
        CityMap.__init__(self, cityList, costs)
    
    @staticmethod
    def __generateCityList(numberOfCities):
        cityList = list()
        for i in range(0, numberOfCities):
            cityList.append(i)
        return cityList
    
    @staticmethod
    def __generateCosts(cityList):
        global MAX_COST
        costs = dict()
        for city1 in cityList:
            for city2 in cityList:
                if city1 == city2:
                    continue
                if city1 < city2:
                    if (city1, city2) not in costs:
                        costs[(city1, city2)] = randint(1, RandomCityMap.MAX_COST)
                else:
                    if (city2, city1) not in costs:
                        costs[(city2, city1)] = randint(1, RandomCityMap.MAX_COST)
        return costs
        
    