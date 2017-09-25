# -*- coding: utf-8 -*-

class LocalSearch:

    @staticmethod
    def search(cityMap):
        path = list(cityMap.getCityList())
        improvement = True
        while improvement:
            improvement = False
            for i in range(0, len(path)):
                if i+1 == len(path):
                    break
                
                for j in range(0, len(path)):
                    if j == i or j == i-1 or j == i+1:
                        continue
                    if j+1 == len(path):
                        break
                    actualPathCost = cityMap.getCostBetweenCities(path[i], path[i+1]) + cityMap.getCostBetweenCities(path[j], path[j+1])
                    newPathCost = cityMap.getCostBetweenCities(path[i], path[j]) + cityMap.getCostBetweenCities(path[i+1], path[j+1])
                    #actualPathCost = getCost(path[i], path[i+1], costs)
                    #newPathCost = getCost(path[i], path[j], costs)
                    if actualPathCost > newPathCost:
                        temp = path[i+1]
                        path[i+1] = path[j]
                        path[j] = temp
                        improvement = True
        return (path, cityMap.getTotalCost(path))