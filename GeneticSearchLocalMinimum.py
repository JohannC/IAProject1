# -*- coding: utf-8 -*-
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from Path import Path


class GeneticSearchLocalMinimum(GeneticSearch):
    
    MAX_NUMBER_OF_SIBLINGS = 16
    MIN_NUMBER_OF_SIBLINGS = 4
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 3
    MAX_NUMBER_OF_MUTATION = 1
    
    def __init__(self, cityMap, seed = None):
        super(GeneticSearchLocalMinimum, self).__init__(cityMap, seed)
        self.localResearcher = LocalSearch(self.cityMap)

    def search(self):
        noImprovement = 0
        population = self._generatePolulation(self.MAX_NUMBER_OF_SIBLINGS)
        actualBestElement = super(GeneticSearchLocalMinimum, self)._bestElement(population)
        while noImprovement < self.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            loopNumber = int((self.MAX_NUMBER_OF_SIBLINGS - self.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = super(GeneticSearchLocalMinimum, self)._selectParent(population)
                parent2 = super(GeneticSearchLocalMinimum, self)._selectParent(population)
                (kid1, kid2) = super(GeneticSearchLocalMinimum, self)._makeLove(parent1, parent2)
                kid1Improved = self.localResearcher.search(kid1)
                kid2Improved = self.localResearcher.search(kid2)
                population.append(Path(kid1Improved,self.cityMap))
                population.append(Path(kid2Improved,self.cityMap))
            population = super(GeneticSearchLocalMinimum, self)._keepBestElements(population, self.MIN_NUMBER_OF_SIBLINGS)
            newBestElement = population[0]
            if newBestElement.getPathCost() >= actualBestElement.getPathCost():
                noImprovement +=1
            else:
                noImprovement =0
                actualBestElement = newBestElement
        result = actualBestElement.getPath()
        return result
    
    def _generatePolulation(self, numberOfElement):
        population = list()
        for i in range(0, numberOfElement):
            member = super(GeneticSearchLocalMinimum, self)._generateRandomSolution()
            memberImproved= self.localResearcher.search(member)
            population.append(Path(memberImproved,self.cityMap))
        return population
    
            
