# -*- coding: utf-8 -*-

class CityMap:
    
    
    def __init__(self, cityList, costs):
        self.__cityList = cityList
        self.__costs = costs
        self.__numberOfCities = len(cityList)
    
    def getCityList(self):
        return self.__cityList
    
    def getCosts(self):
        return self.__costs
    
    def getNumberOfCities(self):
        return self.__numberOfCities
    
    def getTotalCost(self, path):
        cost = 0
        for i in range(0, len(path)):
            if i+1 == len(path):
                j = 0
            else:
                j = i+1
            cost += self.getCostBetweenCities(path[i], path[j])
        return cost

    def getCostBetweenCities(self, point1, point2):
        if point1 < point2:
            return self.__costs[point2-2][point1-1]
        else:
            return self.__costs[point1-2][point2-1] 

