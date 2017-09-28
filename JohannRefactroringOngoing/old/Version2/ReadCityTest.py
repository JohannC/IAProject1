# -*- coding: utf-8 -*-
from CityMap import CityMap
import re
class ReadCityTest(CityMap):
    def __init__(self, filename):
        file = open(filename,'r')
        lines=file.readlines()
        file.close()
        numberOfCities=int(re.search(r'\d+', lines[3]).group())
        cityList=range(1,numberOfCities+1)
        costs = [[0 for x in range(y+1)] for y in range(numberOfCities-1)]
        i=0
        j=0
        for l in range(7,len(lines)-1):
            data = lines[l].split()
            for k in range(0,len(data)):
                if(int(data[k])==0):
                    i=i+1
                    j=0
                else:
                    costs[i-1][j]=int(data[k])
                    j=j+1
        CityMap.__init__(self, cityList, costs)
        

