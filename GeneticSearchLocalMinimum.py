# -*- coding: utf-8 -*-
from random import randint
from random import shuffle
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch



class GeneticSearchLocalMinimum(GeneticSearch):
    
    MAX_NUMBER_OF_SIBLINGS = 30
    MIN_NUMBER_OF_SIBLINGS = 10
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 3
    MAX_NUMBER_OF_MUTATION = 1
    
    @classmethod
    def search(cls, cityMap):
        noImprovement = 0
        population = cls._generatePolulation(cityMap.getCityList(), cls.MAX_NUMBER_OF_SIBLINGS, cityMap)
        while noImprovement < cls.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            actualBestElement = super(GeneticSearchLocalMinimum, cls)._bestElement(population, cityMap)
            loopNumber = int((cls.MAX_NUMBER_OF_SIBLINGS - cls.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = super(GeneticSearchLocalMinimum, cls)._selectParent(population, cityMap)
                parent2 = super(GeneticSearchLocalMinimum, cls)._selectParent(population, cityMap)
                (kid1, kid2) = super(GeneticSearchLocalMinimum, cls)._makeLove(parent1, parent2)
                kid1Improved = LocalSearch.search(cityMap, kid1)
                kid2Improved = LocalSearch.search(cityMap, kid2)
                population.append(kid1Improved)
                population.append(kid2Improved)
            population = super(GeneticSearchLocalMinimum, cls)._keepBestElements(population, cityMap, cls.MIN_NUMBER_OF_SIBLINGS)
            newBestElement = super(GeneticSearchLocalMinimum, cls)._bestElement(population, cityMap)
            if cityMap.getTotalCost(newBestElement) >= cityMap.getTotalCost(actualBestElement):
                noImprovement +=1
            else:
                noImprovement =0
        result = super(GeneticSearchLocalMinimum, cls)._bestElement(population, cityMap)
        return result
    
    @classmethod
    def _generatePolulation(cls, cityList, numberOfElement, cityMap):
        population = list()
        for i in range(0, numberOfElement):
            member = super(GeneticSearchLocalMinimum, cls)._generateRandomSolution(cityList)
            memberImproved= LocalSearch.search(cityMap, member)
            population.append(memberImproved)
        return population
    
            
