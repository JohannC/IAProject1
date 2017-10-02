import datetime
from LocalSearch import LocalSearch
from GeneticSearch import GeneticSearch
from GeneticSearchLocalMinimum import GeneticSearchLocalMinimum
from ReadCityMapFromFile import ReadCityMapFromFile
try:
    times=int(input('Choose times to test:'))
except ValueError:
    print ("Not a valid number, testing 10 times..")
    times=10
cityMap1 = ReadCityMapFromFile.read("test/si175.tsp")
totalcost=0
startTime = datetime.datetime.now()
bestseed=0
bestcost=9999999
for seed in range(0,times):
    path = GeneticSearchLocalMinimum(cityMap1, seed).search()
    actualcost=cityMap1.getTotalCost(path)
    totalcost+=actualcost
    if(actualcost<bestcost):
        bestcost=actualcost
        bestseed=seed
endTime = datetime.datetime.now()
print('Average Cost: '+str(totalcost/times))
print('Average Time: '+str((endTime-startTime)//times))
print('Best Seed: '+str(bestseed))
print('Best Cost: '+str(bestcost))