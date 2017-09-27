# -*- coding: utf-8 -*-
from random import randint
from random import shuffle 
from Path import Path
class GeneticSearch:
    
    MAX_NUMBER_OF_SIBLINGS = 110
    MIN_NUMBER_OF_SIBLINGS = 30
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 30
    MAX_NUMBER_OF_MUTATION = 1
    
    @classmethod
    def search(cls, cityMap):
        noImprovement = 0
        population = cls._generatePolulation(cityMap.getCityList(), cls.MAX_NUMBER_OF_SIBLINGS,cityMap)
        actualBestElement = cls._bestElement(population)
        while noImprovement < cls.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            loopNumber = int((cls.MAX_NUMBER_OF_SIBLINGS - cls.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = cls._selectParent(population)
                parent2 = cls._selectParent(population)
                (kid1, kid2) = cls._makeLove(parent1, parent2)
                for j in range(0, cls.MAX_NUMBER_OF_MUTATION):
                    cls._mutate(kid1)
                    cls._mutate(kid2)
                population.append(Path(kid1,cityMap))
                population.append(Path(kid2,cityMap))
            population = cls._keepBestElements(population, cls.MIN_NUMBER_OF_SIBLINGS)
            newBestElement = population[0]
            if (newBestElement.pathcost >= actualBestElement.pathcost):
                noImprovement +=1
            else:
                noImprovement =0
                actualBestElement = newBestElement
        result = actualBestElement.path
        return result
    
    @classmethod
    def _makeLove(cls, father, mother):
        halfNumberOfCities = int(len(father)/2)
        startOfSelection = randint(0,halfNumberOfCities)
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
    
    @classmethod
    def _mutate(cls, child):
        swapPosition1 = randint(0,len(child)-1)
        swapPosition2 = randint(0,len(child)-1)
        temp = child[swapPosition1]
        child[swapPosition1] = child[swapPosition2]
        child[swapPosition2] = temp
        
    @classmethod
    def _generateRandomSolution(cls, cityList):
        solution = list(cityList)
        shuffle(solution)
        return solution
    
    @classmethod
    def _generatePolulation(cls, cityList, numberOfElement,cityMap):
        population = list()
        for i in range(0, numberOfElement):
            path=cls._generateRandomSolution(cityList)
            population.append(Path(path,cityMap))
        return population
    
    @classmethod
    def _selectParent(cls, population):
        indice1 = randint(0,len(population)-1)
        indice2 = randint(0,len(population)-1)
        if (population[indice1].pathcost >= population[indice1].pathcost):
            return population[indice2].path
        else:
            return population[indice1].path
    
    @classmethod
    def _bestElement(cls, population):
        element = 0
        for i in range(1, len(population)):
            if(population[i].pathcost < population[element].pathcost):
                element = i
        return population[element]
    
    @classmethod
    def _keepBestElements(cls, population, numberToKeep):
        newPopulation  = list()
        for i in range(0,numberToKeep):
            element = cls._bestElement(population)
            newPopulation.append(element)
            population.remove(element)
        return newPopulation
            
