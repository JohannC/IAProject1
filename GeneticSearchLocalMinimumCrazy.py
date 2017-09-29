# -*- coding: utf-8 -*-
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from Path import Path
import random


class GeneticSearchLocalMinimumCrazy(GeneticSearch):
    
    MAX_NUMBER_OF_SIBLINGS = 120
    MIN_NUMBER_OF_SIBLINGS = 30
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 20
    MAX_NUMBER_OF_MUTATION = 1
    
    def __init__(self, cityMap, seed = None):
        super(GeneticSearchLocalMinimumCrazy, self).__init__(cityMap, seed)
        self.localResearcher = LocalSearch(self.cityMap)
        if seed != None:
           random.seed(seed)

    
    def search(self):
        noImprovement = 0
        population = self._generatePolulation(self.MIN_NUMBER_OF_SIBLINGS)
        actualBestElement = super(GeneticSearchLocalMinimumCrazy, self)._bestElement(population)
        while noImprovement < self.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            loopNumber = int((self.MAX_NUMBER_OF_SIBLINGS - self.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = super(GeneticSearchLocalMinimumCrazy, self)._selectParent(population)
                parent2 = super(GeneticSearchLocalMinimumCrazy, self)._selectParent(population)
                (kid1, kid2) = super(GeneticSearchLocalMinimumCrazy, self)._makeLove(parent1, parent2)
                kid1 = self.localResearcher.lightSearch(kid1)
                kid2 = self.localResearcher.lightSearch(kid2)
                
                population.append(Path(kid1,self.cityMap))
                population.append(Path(kid2,self.cityMap))
            population = super(GeneticSearchLocalMinimumCrazy, self)._keepBestElements(population, self.MIN_NUMBER_OF_SIBLINGS)
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
    """
    def _keepBestElements(self, population, numberToKeep):
        costClassification = dict()
        for i in range(0,len(population)):
            costClassification[population[i].pathcost]  = population[i] 
        sortedListOfBestElements = [value for (key, value) in sorted(costClassification.items())]
        newpop=sortedListOfBestElements[:int(numberToKeep/3)]
        for i in range(int(numberToKeep/3),numberToKeep):
            newpop.append(sortedListOfBestElements[random.randint(int(numberToKeep/3),numberToKeep-1)])
        return newpop
    """
    
            
