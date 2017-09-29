    # -*- coding: utf-8 -*-

class LocalSearch:
    
    def __init__(self, cityMap):
        self.cityMap = cityMap
    
    def search(self, pathToTest = None):
        loop=0
        if pathToTest != None:
            path = pathToTest
        else:
            path = list(self.cityMap.getCityList())
        improvement = True
        while improvement:
            improvement = False
            for i in range(0, len(path)-1):  
                for j in range(i+2, len(path)-1):
                    actualPathCost = self.cityMap.getCostBetweenCities(path[i], path[i+1]) + self.cityMap.getCostBetweenCities(path[j], path[j+1]) 
                    newPathCost = self.cityMap.getCostBetweenCities(path[i], path[j]) + self.cityMap.getCostBetweenCities(path[i+1], path[j+1])
                    if actualPathCost > newPathCost:
                        temp = path[i+1]
                        path[i+1] = path[j]
                        path[j] = temp
                        improvement = True
                    loop+=1
                    if(loop>len(path)*len(path)):
                        return path
        return path