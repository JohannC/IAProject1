#https://fr.wikipedia.org/wiki/Probl%C3%A8me_du_voyageur_de_commerce
#https://fr.wikipedia.org/wiki/2-opt
#https://fr.wikipedia.org/wiki/Recherche_locale_(optimisation)

from random import randint
from random import shuffle


def makeLove(father, mother):
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

def mutate(child):
    swapPosition1 = randint(0,len(child)-1)
    swapPosition2 = randint(0,len(child)-1)
    temp = child[swapPosition1]
    child[swapPosition1] = child[swapPosition2]
    child[swapPosition2] = temp
    
def generateRandomSolution(cityList):
    solution = list(cityList)
    shuffle(solution)
    return solution

def generatePolulation(cityList, numberOfElement):
    population = list()
    for i in range(0, numberOfElement):
        population.append(generateRandomSolution(cityList))
    return population

def getTotalCost(path, costs):
    cost = 0
    for i in range(0, len(path)):
        if i+1 == len(path):
            j = 0
        else:
            j = i+1
        cost += getCost(path[i], path[j], costs)
    return cost

def getCost(pointA, pointB, costs):
    if pointA < pointB:
        return costs[(pointA, pointB)]
    else:
        return costs[(pointB, pointA)]

def selectParent(population, costs):
    indice1 = randint(0,len(population)-1)
    indice2 = randint(0,len(population)-1)
    if getTotalCost(population[indice1], costs) >= getTotalCost(population[indice2], costs):
        return population[indice2]
    else:
        return population[indice1]

def bestElement(population, costs):
    bestScore = int()
    element = None
    for i in range(0, len(population)):
        elementScore = getTotalCost(population[i], costs)
        if i == 0:
            bestScore = elementScore 
            element = population[i]
        elif elementScore < bestScore:
            bestScore = elementScore
            element = population[i]
    return element

def keepBestElements(population, costs, numberToKeep):
    newPopulation  = list()
    for i in range(0,numberToKeep):
        element = bestElement(population, costs)
        newPopulation.append(element)
        population.remove(element)
    return newPopulation

def geneticSearch(cities, costs):
    noImprovement = 0
    population = generatePolulation(cities, 30)
    while noImprovement <5:
        actualBestElement = bestElement(population, costs)
        for i in range(0,20):
            parent1 = selectParent(population, costs)
            parent2 = selectParent(population, costs)
            (kid1, kid2) = makeLove(parent1, parent2)
            mutate(kid1)
            mutate(kid2)
            population.append(kid1)
            population.append(kid2)
        population = keepBestElements(population, costs, 30)
        newBestElement = bestElement(population, costs)
        if getTotalCost(newBestElement, costs) >= getTotalCost(actualBestElement, costs):
            noImprovement +=1
    result = bestElement(population, costs)
    return (result, getTotalCost(result, costs))

cities1 = ('A','B','C','D','E')
costs1 = {
            ('A', 'B') : 3,
            ('A', 'C') : 100,
            ('A', 'D') : 8,
            ('A', 'E') : 1,
            ('B', 'C') : 6,
            ('B', 'D') : 1,
            ('B', 'E') : 1,
            ('C', 'D') : 6,
            ('C', 'E') : 7,
            ('D', 'E') : 5        
        }  

print(geneticSearch(cities1, costs1))


