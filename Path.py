# -*- coding: utf-8 -*-
class Path:
    def __init__(self, path,cityMap):
        self.path = path
        self.pathcost = cityMap.getTotalCost(path)
    
    def getPathCost(self):
        return self.pathcost
    
    def getPath(self):
        return self.path
        