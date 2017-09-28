# -*- coding: utf-8 -*-

class LocalSearch:
    
    @staticmethod
    def search(cityMap, pathToTest = None):
        if pathToTest != None:
            path = pathToTest
        else:
            path = list(cityMap.getCityList())
        improvement = True
        while improvement:
            improvement = False
            for i in range(0, len(path)-1):  
                for j in range(0, len(path)-1):    
                    if j == i or j == i-1 or j == i+1:
                        continue
                    actualPathCost = cityMap.getCostBetweenCities(path[i], path[i+1]) + cityMap.getCostBetweenCities(path[j], path[j+1])
                    newPathCost = cityMap.getCostBetweenCities(path[i], path[j]) + cityMap.getCostBetweenCities(path[i+1], path[j+1])
                    #actualPathCost = getCost(path[i], path[i+1], costs)
                    #newPathCost = getCost(path[i], path[j], costs)
                    if actualPathCost > newPathCost:
                        temp = path[i+1]
                        path[i+1] = path[j]
                        path[j] = temp
                        improvement = True
                        
        return path
    @staticmethod
    def searchTrial(cityMap, pathToTest = None):
        if pathToTest != None:
            path = pathToTest
        else:
            path = list(cityMap.getCityList())
        n=len(path)
        improvement = True
        while improvement:
            
            improvement = False
            for i in range(0, n):
                
                actualPathCost = cityMap.getCostBetweenCities(path[i], path[LocalSearch._getPosition(n,i+1)]) + cityMap.getCostBetweenCities(path[LocalSearch._getPosition(n,i+2)], path[LocalSearch._getPosition(n,i+3)])
                newPathCost = cityMap.getCostBetweenCities(path[i], path[LocalSearch._getPosition(n,i+2)])  + cityMap.getCostBetweenCities(path[LocalSearch._getPosition(n,i+1)], path[LocalSearch._getPosition(n,i+3)])
                    
                if actualPathCost > newPathCost:
                    temp = path[LocalSearch._getPosition(n,i+1)]
                    path[LocalSearch._getPosition(n,i+1)] = path[LocalSearch._getPosition(n,i+2)]
                    path[LocalSearch._getPosition(n,i+2)] = temp
                    improvement = True
                        
        return path
    
    def _getPosition(n,i):
        if(i>=n):
            i=i-n
        return i
    