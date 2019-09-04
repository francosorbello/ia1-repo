class PriorityQueue:
    def __init__(self):
        self.queue = []
    def.Add(self,elem):


class AStar:
    def __init__(self,startPos,endPos,env):
        self.startPos = startPos
        self.endPos = endPos
        self.frontier = []
        self.visited = []
        self.path = []
        self.env = env
    
    def Search(self):
        self.frontier.add(self.startPos)
