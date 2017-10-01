# -*- coding: utf-8 -*-
import random 
from Path import Path
import math
class GeneticSearch:
    
    MAX_NUMBER_OF_SIBLINGS_COEFF = 1.8
    MIN_NUMBER_OF_SIBLINGS_COEFF = 0.6
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 32
    MAX_NUMBER_OF_MUTATION_COEFF = 0.08
    COEFF_BIG_PROBLEMS_COEFF =0.3
    
    def __init__(self, cityMap, seed = None):
       self.seed = seed
       self.cityMap = cityMap
       if(self.__class__.__name__=='GeneticSearch'): #genetic
           (self.minNumberOfSiblings, self.maxNumberOfSiblings, self.maxNumberWithoutImprovement, self.maxNumberOfMutation) = self._calculateParameters()
       else: #genticwithlocalminimum
           (self.minNumberOfSiblings, self.maxNumberOfSiblings, self.maxNumberWithoutImprovement) = self._calculateParameters()
       if seed != None:
           random.seed(seed)

    
    def search(self):
        noImprovement = 0
        population = self._generatePolulation(self.minNumberOfSiblings)
        actualBestElement = self._bestElement(population)
        while noImprovement < self.maxNumberWithoutImprovement:
            loopNumber = int((self.maxNumberOfSiblings - self.minNumberOfSiblings)/2)
            for i in range(0, loopNumber):
                parent1 = self._selectParent(population)
                parent2 = self._selectParent(population)
                (kid1, kid2) = self._makeLove(parent1, parent2)
                for j in range(0, random.randint(0,self.maxNumberOfMutation)):
                    self._mutate(kid1)
                    self._mutate(kid2)
                population.append(Path(kid1,self.cityMap))
                population.append(Path(kid2,self.cityMap))
            population = self._keepBestElements(population, self.minNumberOfSiblings)
            newBestElement = population[0]
            if (newBestElement.getPathCost() >= actualBestElement.getPathCost()):
                noImprovement +=1
            else:
                noImprovement =0
                actualBestElement = newBestElement
        result = actualBestElement.getPath()
        return result
    
    @classmethod
    def _makeLove(self, father, mother):
        halfNumberOfCities = int(len(father)/2)
        startOfSelection = random.randint(0,halfNumberOfCities)
        child1 = list()
        child2 = list()
        nextIndiceToFillForChild1=0
        nextIndiceToFillForChild2=0
        for i in range(0, len(father)):
            if i >= startOfSelection and i < startOfSelection+halfNumberOfCities :
                child1.insert(i, father[i])
                child2.insert(i, mother[i])
                nextIndiceToFillForChild1=i+1
                nextIndiceToFillForChild2=i+1
            if i >= startOfSelection+halfNumberOfCities:
                if mother[i] not in child1:
                    child1.insert(i, mother[i])
                    nextIndiceToFillForChild1=i+1
                if father[i] not in child2:
                    child2.insert(i, father[i])
                    nextIndiceToFillForChild2=i+1
        for i in range(0, len(father)):
            if nextIndiceToFillForChild1 == len(father):
                nextIndiceToFillForChild1 = 0
            if nextIndiceToFillForChild2 == len(father):
                nextIndiceToFillForChild2 = 0
            if mother[i] not in child1:
                child1.insert(nextIndiceToFillForChild1, mother[i])
                nextIndiceToFillForChild1 +=1
            if father[i] not in child2:
                child2.insert(nextIndiceToFillForChild2, father[i])
                nextIndiceToFillForChild2 +=1
        
        return (child1, child2)
    def _calculateParameters(self):
        maxNumberWithoutImprovement=self.MAX_NUMBER_WITHOUT_IMPROVEMENT
        if(self.cityMap.getNumberOfCities()>=100):
            aux=self.COEFF_BIG_PROBLEMS_COEFF
            maxNumberWithoutImprovement=int(maxNumberWithoutImprovement*aux*3)
        else:
            aux=1.0
        minNumberOfSiblings = int(self.cityMap.getNumberOfCities()*self.MIN_NUMBER_OF_SIBLINGS_COEFF*aux)
        maxNumberOfSiblings = int(self.cityMap.getNumberOfCities()*self.MAX_NUMBER_OF_SIBLINGS_COEFF*aux)
        if(self.__class__.__name__=='GeneticSearch'):
            maxNumberOfMutation = int(self.cityMap.getNumberOfCities()*self.MAX_NUMBER_OF_MUTATION_COEFF*aux)
            return(minNumberOfSiblings, maxNumberOfSiblings, maxNumberWithoutImprovement, maxNumberOfMutation)
        else:
            return(minNumberOfSiblings, maxNumberOfSiblings, maxNumberWithoutImprovement)
        
    
    def _mutate(self, child):
        swapPosition1 = random.randint(0,len(child)-1)
        swapPosition2 = random.randint(0,len(child)-1)
        temp = child[swapPosition1]
        child[swapPosition1] = child[swapPosition2]
        child[swapPosition2] = temp
        
    def _generateRandomSolution(self):
        solution = list(self.cityMap.getCityList())
        random.shuffle(solution)
        return solution
    
    def _generatePolulation(self, numberOfElement):
        population = list()
        for i in range(0, numberOfElement):
            path=self._generateRandomSolution()
            population.append(Path(path,self.cityMap))
        return population
    
    def _selectParent(self, population):
        indice1 = random.randint(0,len(population)-1)
        indice2 = random.randint(0,len(population)-1)
        if (population[indice1].getPathCost() >= population[indice1].getPathCost()):
            return population[indice2].getPath()
        else:
            return population[indice1].getPath()
    
    def _bestElement(self, population):
        element = 0
        for i in range(1, len(population)):
            if(population[i].getPathCost() < population[element].getPathCost()):
                element = i
        return population[element]
    
    def _keepBestElements(self, population, numberToKeep):
        costClassification = dict()
        for i in range(0,len(population)):
            costClassification[population[i].getPathCost()]  = population[i] 
        sortedListOfBestElements = [value for (key, value) in sorted(costClassification.items())]
        n = int(math.ceil(numberToKeep/2))
        "Keeps top n elements, where n is selected number/2"
        filteredSortedListOfBestElements = sortedListOfBestElements[:n] 
        "Calculates how many will be left"
        amountLeft = len(population) - n
        "Gets in a separate list the not chosen elements"
        notSelectedElementList = sortedListOfBestElements[:-amountLeft]
        "Shuffles the list"
        random.shuffle(notSelectedElementList)
        "Selects the first n random elements"
        randomSelectedElementList = notSelectedElementList[:n]
        
        return filteredSortedListOfBestElements + randomSelectedElementList  
            
