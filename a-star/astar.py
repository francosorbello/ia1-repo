from PriorityQueue import PriorityQueue
class Node:
    def __init__(self,x,y,parent):
        self.x = x
        self.y = y
        self.gScore = 0
        self.hScore = 0
        self.fScore = 0
        self.parent = parent
    
    def __str__(self):
        return "["+str(self.x)+","+str(self.y)+"]"
        
    def GetPosition(self):
        return [self.x,self.y]
    
    def UpdateFscore(self):
        self.fScore = self.gScore + self.hScore
        
class AStar:
    def __init__(self,startPos,endPos,env):
        self.startPos = startPos
        self.endPos = endPos
        self.openList = PriorityQueue()
        self.closedList = []
        self.path = []
        self.env = env
    
    def Manhattan(self,start,end):
        x = abs(start[0]-end[0])
        y = abs(start[1]-end[1])
        return x + y

    def isInClosedList(self,element):
        if len(self.closedList)==0:
            return False
        
        pos = element.GetPosition()
        for closedNode in self.closedList:
            if closedNode.GetPosition() == pos:
                return True
        
        return False
    
    def Search(self):
        
        start = Node(self.startPos[0],self.startPos[1],None)
        start.gScore = self.Manhattan(self.startPos,start.GetPosition())
        start.hScore = self.Manhattan(self.endPos,start.GetPosition())
        start.UpdateFscore()
            
        G = start.gScore
        
        self.openList.Enqueue(start,start.fScore)
        
        while self.openList.Length() > 0:
            #obtengo el nodo con menor f y lo guardo en los visitados
            current = self.openList.Dequeue()
            self.closedList.append(current)
            
            #si estoy en el nodo objetivo, termino
            if current.GetPosition() == self.endPos:
                print("ENCONTRADO")
                path = []
                while current is not None:
                    path.append(current.GetPosition())
                    current = current.parent
                
                self.env.PrintPath(path)
                break
            
            #genero los vecinos
            neighbours = self.env.GetNeighbors(current.x,current.y)
            for neigbhour in neighbours:
                
                neirNode = Node(neigbhour[0],neigbhour[1],current)

                #calculo f para el vecino
                neirNode.gScore = self.Manhattan(self.startPos,neirNode.GetPosition())
                neirNode.hScore = self.Manhattan(self.endPos,neirNode.GetPosition())
                neirNode.UpdateFscore()
                
                #si ya esta en los visitados lo ignoro
                if(self.isInClosedList(neirNode)):
                    continue
                
                #si ya hay un camino mejor en la frontera lo ignoro
                auxSearch = self.openList.Search(neirNode)
                if auxSearch != -1 and self.openList[auxSearch].value.gScore > neirNode.gScore:
                    continue        
                self.openList.Enqueue(neirNode,neirNode.fScore)