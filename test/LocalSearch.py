    # -*- coding: utf-8 -*-

class LocalSearch:
    
    @staticmethod
    def search(cityMap, pathToTest = None):
        loop=0
        if pathToTest != None:
            path = pathToTest
        else:
            path = list(cityMap.getCityList())
        improvement = True
        while improvement:
            improvement = False
            for i in range(0, len(path)-1):  
                for j in range(i+2, len(path)-1):
                    actualPathCost = cityMap.getCostBetweenCities(path[i], path[i+1]) + cityMap.getCostBetweenCities(path[j], path[j+1]) 
                    newPathCost = cityMap.getCostBetweenCities(path[i], path[j]) + cityMap.getCostBetweenCities(path[i+1], path[j+1])
                    #actualPathCost = getCost(path[i], path[i+1], costs)
                    #newPathCost = getCost(path[i], path[j], costs)
                    if actualPathCost > newPathCost:
                        temp = path[i+1]
                        path[i+1] = path[j]
                        path[j] = temp
                        improvement = True
                    loop+=1
                    if(loop>len(path)*len(path)):
                        return path
                        
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
                
                actualPathCost = cityMap.getCostBetweenCities(path[i], path[LocalSearch._getIndex(n,i+1)]) + cityMap.getCostBetweenCities(path[LocalSearch._getIndex(n,i+2)], path[LocalSearch._getIndex(n,i+3)])
                newPathCost = cityMap.getCostBetweenCities(path[i], path[LocalSearch._getIndex(n,i+2)])  + cityMap.getCostBetweenCities(path[LocalSearch._getIndex(n,i+1)], path[LocalSearch._getIndex(n,i+3)])
                    
                if actualPathCost > newPathCost:
                    temp = path[LocalSearch._getIndex(n,i+1)]
                    path[LocalSearch._getIndex(n,i+1)] = path[LocalSearch._getIndex(n,i+2)]
                    path[LocalSearch._getIndex(n,i+2)] = temp
                    improvement = True
                        
        return path
    @staticmethod
    def searchLight(cityMap, pathToTest = None):
        if pathToTest != None:
            path = pathToTest
        else:
            path = list(cityMap.getCityList())
        improvement = True
        n=len(path)
        while improvement:
            improvement = False
            for i in range(0, len(path)-1):
                
                for j in range(i+1, len(path)):
                    
                    if(j==i+1):
                        actualPathCost = cityMap.getCostBetweenCities(path[LocalSearch._getIndex(n,i-1)], path[i]) + cityMap.getCostBetweenCities(path[j], path[LocalSearch._getIndex(n,i+2)])
                        newPathCost = cityMap.getCostBetweenCities(path[LocalSearch._getIndex(n,i-1)], path[j])  + cityMap.getCostBetweenCities(path[i], path[LocalSearch._getIndex(n,i+2)])
                    elif(j-n==i-1):
                        actualPathCost =  cityMap.getCostBetweenCities(path[j-1], path[j])+cityMap.getCostBetweenCities(path[i], path[i+1])
                        newPathCost = cityMap.getCostBetweenCities(path[j-1], path[i])  + cityMap.getCostBetweenCities(path[j], path[i+1])
                    else:
                        actualPathCost = cityMap.getCostBetweenCities(path[LocalSearch._getIndex(n,i-1)], path[i]) + cityMap.getCostBetweenCities(path[j], path[LocalSearch._getIndex(n,j+1)]) + cityMap.getCostBetweenCities(path[i], path[LocalSearch._getIndex(n,i+1)]) + cityMap.getCostBetweenCities(path[j-1], path[j])
                        newPathCost = cityMap.getCostBetweenCities(path[LocalSearch._getIndex(n,i-1)], path[j]) + cityMap.getCostBetweenCities(path[i], path[LocalSearch._getIndex(n,j+1)]) + cityMap.getCostBetweenCities(path[j], path[LocalSearch._getIndex(n,i+1)]) + cityMap.getCostBetweenCities(path[j-1], path[i])
                    #actualPathCost = getCost(path[i], path[i+1], costs)
                    #newPathCost = getCost(path[i], path[j], costs)
                    if actualPathCost > newPathCost:
                        temp = path[i]
                        path[i] = path[j]
                        path[j] = temp
                        improvement = True
                        
        return path
    def _getIndex(n,i):
        if(i<0):
            return n+i
        elif(i>=n):
            return i-n
        else:
            return i
    