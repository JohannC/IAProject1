# -*- coding: utf-8 -*-
from CityMap import CityMap
import re

class ReadCityTest(CityMap):
    def __init__(self, filename):
        file = open(filename,'r')
        lines=file.readlines()
        file.close()
        cityList=range(0,numberOfCities)
        numberOfCities=int(re.search(r'\d+', lines[3]).group())
        costs = dict()
        i=j=0
        for l in range(7,len(lines)):
            data = lines[l].split()
            for k in range(0,len(data)):
                costs[(i, j)]=data[k]
                if(data[k]==0):
                    i=i+1
                    j=0
                else:
                    j=j+1
        
        CityMap.__init__(self, cityList, costs)