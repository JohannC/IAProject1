# -*- coding: utf-8 -*-
from CityMap import CityMap
from random import randint

class RandomMap(map):
    
    MAX_COST  = 100
    
    def __init__(self, numberOfCities):
        cityList = RandomMap.__generateCityList(numberOfCities)
        costs = RandomMap.__generateCosts(cityList)
        map.__init__(self, cityList, costs)
    
    @staticmethod
    def __generateCityList(numberOfCities):
        cityList=list()
        for i in range(1,numberOfCities+1):
            cityList.append(i)
        return cityList
    
    @staticmethod
    def __generateCosts(cityList):
        global MAX_COST
        costs=[[0 for x in range(y+1)] for y in range(len(cityList)-1)] 
        for i in range(0,len(cityList)-1):
            for j in range(0,i+1):
                costs[i][j]=randint(1, RandomMap.MAX_COST)
        return costs
        
    