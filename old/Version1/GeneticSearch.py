# -*- coding: utf-8 -*-
from random import randint
from random import shuffle

class GeneticSearch:
    
    MAX_NUMBER_OF_SIBLINGS = 70
    MIN_NUMBER_OF_SIBLINGS = 30
    MAX_NUMBER_WITHOUT_IMPROVEMENT = 10
    
    @staticmethod
    def search(cityMap):
        noImprovement = 0
        population = GeneticSearch.__generatePolulation(cityMap.getCityList(), GeneticSearch.MAX_NUMBER_OF_SIBLINGS)
        while noImprovement < GeneticSearch.MAX_NUMBER_WITHOUT_IMPROVEMENT:
            actualBestElement = GeneticSearch.__bestElement(population, cityMap)
            loopNumber = int((GeneticSearch.MAX_NUMBER_OF_SIBLINGS - GeneticSearch.MIN_NUMBER_OF_SIBLINGS)/2)
            for i in range(0, loopNumber):
                parent1 = GeneticSearch.__selectParent(population, cityMap)
                parent2 = GeneticSearch.__selectParent(population, cityMap)
                (kid1, kid2) = GeneticSearch.__makeLove(parent1, parent2)
                GeneticSearch.__mutate(kid1)
                GeneticSearch.__mutate(kid2)
                population.append(kid1)
                population.append(kid2)
            population = GeneticSearch.__keepBestElements(population, cityMap, GeneticSearch.MIN_NUMBER_OF_SIBLINGS)
            newBestElement = GeneticSearch.__bestElement(population, cityMap)
            if cityMap.getTotalCost(newBestElement) >= cityMap.getTotalCost(actualBestElement):
                noImprovement +=1
        result = GeneticSearch.__bestElement(population, cityMap)
        return (result, cityMap.getTotalCost(result))
    
    @staticmethod
    def __makeLove(father, mother):
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
    
    @staticmethod
    def __mutate(child):
        swapPosition1 = randint(0,len(child)-1)
        swapPosition2 = randint(0,len(child)-1)
        temp = child[swapPosition1]
        child[swapPosition1] = child[swapPosition2]
        child[swapPosition2] = temp
        
    @staticmethod
    def __generateRandomSolution(cityList):
        solution = list(cityList)
        shuffle(solution)
        return solution
    
    @staticmethod
    def __generatePolulation(cityList, numberOfElement):
        population = list()
        for i in range(0, numberOfElement):
            population.append(GeneticSearch.__generateRandomSolution(cityList))
        return population
    
    @staticmethod
    def __selectParent(population, cityMap):
        indice1 = randint(0,len(population)-1)
        indice2 = randint(0,len(population)-1)
        if cityMap.getTotalCost(population[indice1]) >= cityMap.getTotalCost(population[indice2]):
            return population[indice2]
        else:
            return population[indice1]
    
    @staticmethod
    def __bestElement(population, cityMap):
        bestScore = int()
        element = None
        for i in range(0, len(population)):
            elementScore = cityMap.getTotalCost(population[i])
            if i == 0:
                bestScore = elementScore 
                element = population[i]
            elif elementScore < bestScore:
                bestScore = elementScore
                element = population[i]
        return element
    
    @staticmethod
    def __keepBestElements(population, cityMap, numberToKeep):
        newPopulation  = list()
        for i in range(0,numberToKeep):
            element = GeneticSearch.__bestElement(population, cityMap)
            newPopulation.append(element)
            population.remove(element)
        return newPopulation
            
