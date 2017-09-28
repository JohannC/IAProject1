# -*- coding: utf-8 -*-
from LocalSearch import LocalSearch
from random import randint
from GeneticSearch import GeneticSearch
from Path import Path


class GeneticSearchLocalMinimumCrazy(GeneticSearch):
    
    MAX_NUMBER_OF_SIBLINGS = 120
    MIN_NUMBER_OF_SIBLINGS = 30
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 20
    MAX_NUMBER_OF_MUTATION = 1
    
    @classmethod
    def search(cls, cityMap):
        noImprovement = 0
        population = cls._generatePolulation(cityMap.getCityList(), cls.MIN_NUMBER_OF_SIBLINGS, cityMap)
        actualBestElement = super(GeneticSearchLocalMinimumCrazy, cls)._bestElement(population)
        while noImprovement < cls.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            loopNumber = int((cls.MAX_NUMBER_OF_SIBLINGS - cls.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = super(GeneticSearchLocalMinimumCrazy, cls)._selectParent(population)
                parent2 = super(GeneticSearchLocalMinimumCrazy, cls)._selectParent(population)
                (kid1, kid2) = super(GeneticSearchLocalMinimumCrazy, cls)._makeLove(parent1, parent2)
                kid1 = LocalSearch.searchTrial(cityMap, kid1)
                kid2 = LocalSearch.searchTrial(cityMap, kid2)
                
                population.append(Path(kid1,cityMap))
                population.append(Path(kid2,cityMap))
            population = cls._keepBestElements(population, cls.MIN_NUMBER_OF_SIBLINGS)
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
            member = super(GeneticSearchLocalMinimumCrazy, cls)._generateRandomSolution(cityList)
            population.append(Path(member,cityMap))
        return population
    @classmethod
    def _keepBestElements(cls, population, numberToKeep):
        costClassification = dict()
        for i in range(0,len(population)):
            costClassification[population[i].pathcost]  = population[i] 
        sortedListOfBestElements = [value for (key, value) in sorted(costClassification.items())]
        newpop=sortedListOfBestElements[:int(numberToKeep/3)]
        for i in range(int(numberToKeep/3),numberToKeep):
            newpop.append(sortedListOfBestElements[randint(int(numberToKeep/3),numberToKeep-1)])
        return newpop
    
            
