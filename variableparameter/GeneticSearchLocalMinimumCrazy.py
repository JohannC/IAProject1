# -*- coding: utf-8 -*-
from LocalSearch import LocalSearch
from random import randint
from random import shuffle
from GeneticSearch import GeneticSearch
from Path import Path
import math


class GeneticSearchLocalMinimumCrazy(GeneticSearch):
    
    #MAX_NUMBER_OF_SIBLINGS = 120
    #MIN_NUMBER_OF_SIBLINGS = 30
    #MAX_NUMBER_WITHOUT_IMPROVEMENT = 20
    #MAX_NUMBER_OF_MUTATION = 1
    
    MAX_NUMBER_OF_SIBLINGS_COEFF = 0.8
    MIN_NUMBER_OF_SIBLINGS_COEFF = 0.2
    MAX_NUMBER_WITHOUT_IMPROVEMENT_COEFF = 0.2
    
    def __init__(self, cityMap, seed = None):
        super(GeneticSearchLocalMinimumCrazy, self).__init__(cityMap, seed)
        (self.minNumberOfSiblings, self.maxNumberOfSiblings, self.maxNumberWithoutImprovement, self.maxNumberOfMutation) =  super(GeneticSearchLocalMinimumCrazy, self)._calculateParameters()
        print((self.minNumberOfSiblings, self.maxNumberOfSiblings, self.maxNumberWithoutImprovement, self.maxNumberOfMutation))
    
    def search(self):
        noImprovement = 0
        population = self._generatePolulation(self.minNumberOfSiblings)
        actualBestElement = super(GeneticSearchLocalMinimumCrazy, self)._bestElement(population)
        while noImprovement < self.maxNumberWithoutImprovement:
            loopNumber = int((self.maxNumberWithoutImprovement - self.minNumberOfSiblings)/2)
            for i in range(0, loopNumber):
                parent1 = super(GeneticSearchLocalMinimumCrazy, self)._selectParent(population)
                parent2 = super(GeneticSearchLocalMinimumCrazy, self)._selectParent(population)
                (kid1, kid2) = super(GeneticSearchLocalMinimumCrazy, self)._makeLove(parent1, parent2)
                kid1 = LocalSearch.searchTrial(self.cityMap, kid1)
                kid2 = LocalSearch.searchTrial(self.cityMap, kid2)
                
                population.append(Path(kid1,self.cityMap))
                population.append(Path(kid2,self.cityMap))
            population = super(GeneticSearchLocalMinimumCrazy, self)._keepBestElements(population, self.minNumberOfSiblings)
            newBestElement = population[0]
            if newBestElement.pathcost >= actualBestElement.pathcost:
                noImprovement +=1
            else:
                noImprovement =0
                actualBestElement = newBestElement
        result = actualBestElement.path
        return result
    
    def _generatePolulation(self, numberOfElement):
        population = list()
        for i in range(0, numberOfElement):
            member = super(GeneticSearchLocalMinimumCrazy, self)._generateRandomSolution()
            population.append(Path(member,self.cityMap))
        return population
    
            
