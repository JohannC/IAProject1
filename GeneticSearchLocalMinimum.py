# -*- coding: utf-8 -*-
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from Path import Path


class GeneticSearchLocalMinimum(GeneticSearch):
    
    MAX_NUMBER_OF_SIBLINGS = 16
    MIN_NUMBER_OF_SIBLINGS = 4
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 3
    MAX_NUMBER_OF_MUTATION = 1
    
    @classmethod
    def search(cls, cityMap):
        noImprovement = 0
        population = cls._generatePolulation(cityMap.getCityList(), cls.MAX_NUMBER_OF_SIBLINGS, cityMap)
        actualBestElement = super(GeneticSearchLocalMinimum, cls)._bestElement(population)
        for i in range(0,len(population)):
            print(population[i].pathcost)
        print()
        print()
        while noImprovement < cls.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            loopNumber = int((cls.MAX_NUMBER_OF_SIBLINGS - cls.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = super(GeneticSearchLocalMinimum, cls)._selectParent(population)
                parent2 = super(GeneticSearchLocalMinimum, cls)._selectParent(population)
                (kid1, kid2) = super(GeneticSearchLocalMinimum, cls)._makeLove(parent1, parent2)
                kid1Improved = LocalSearch.search(cityMap, kid1)
                kid2Improved = LocalSearch.search(cityMap, kid2)
                population.append(Path(kid1Improved,cityMap))
                population.append(Path(kid2Improved,cityMap))
            population = super(GeneticSearchLocalMinimum, cls)._keepBestElements(population, cls.MIN_NUMBER_OF_SIBLINGS)
            for i in range(0,len(population)):
                print(population[i].pathcost)
            print()
            print()
            print()
            newBestElement = population[0]
            if newBestElement.pathcost >= actualBestElement.pathcost:
                noImprovement +=1
            else:
                noImprovement =0
                actualBestElement = newBestElement
        result = actualBestElement.path
        return result
    
    @classmethod
    def _generatePolulation(cls, cityList, numberOfElement, cityMap):
        population = list()
        for i in range(0, numberOfElement):
            member = super(GeneticSearchLocalMinimum, cls)._generateRandomSolution(cityList)
            memberImproved= LocalSearch.search(cityMap, member)
            population.append(Path(memberImproved,cityMap))
        return population
    
            
