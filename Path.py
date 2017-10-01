# -*- coding: utf-8 -*-
class Path:
    def __init__(self, path,map):
        self.path = path
        self.pathcost = map.getTotalCost(path)
    
    def getPathCost(self):
        return self.pathcost
    
    def getPath(self):
        return self.path
        