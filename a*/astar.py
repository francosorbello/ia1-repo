class QueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.queue = []
        
    def Length(self):
        return len(self.queue)
    
    def Enqueue(self,elem,priority):
        node = QueueNode(elem,priority)
        if len(self.queue) == 0:
            self.queue.append(node)
            return
        
        for i in range(0,len(self.queue)):
            if priority < self.queue[i].priority:
                self.queue.insert(node)
                return
        
        self.queue.append(node)
        
    def Dequeue(self):
        aux = self.queue.pop(0)
        return aux.value
    
    def Exists(self,position):
        for elem in self.queue:
            if [elem.value.x,elem.value.y] == position:
                return True
        return False
        
class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.gScore = 0
        self.hScore = 0
        self.fScore = 0
    
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
        
        start = Node(self.startPos[0],self.startPos[1])
        start.gScore = self.Manhattan(self.startPos,start.GetPosition())
        start.hScore = self.Manhattan(self.endPos,start.GetPosition())
        start.UpdateFscore()

        self.openList.Enqueue(start,start.fScore)
        
        while self.openList.Length() > 0:
            
            current = self.openList.Dequeue()
            self.closedList.append(current)
            
            if current.GetPosition() == self.endPos:
                print("ENCONTRADO")
                aux = []
                for elm in self.closedList:
                    aux.append(elm.GetPosition())
                    print(elm)
                self.env.PrintPath(aux)
                break
            
            neighbours = self.env.GetNeighbors(current.x,current.y)
            for neigbhour in neighbours:
                
                neirNode = Node(neigbhour[0],neigbhour[1])
                
                #si ya esta en la frontera lo ignoro
                if(self.openList.Exists(neigbhour)):
                    continue
                
                #calculo f para el vecino
                neirNode.gScore = self.Manhattan(self.startPos,neirNode.GetPosition())
                neirNode.hScore = self.Manhattan(self.endPos,neirNode.GetPosition())
                neirNode.UpdateFscore()
                #si f es menor que el score actual y el nodo no fue visitado lo añado a la frontera
                if neirNode.fScore <= current.fScore and not self.isInClosedList(neirNode):
                    self.openList.Enqueue(neirNode,neirNode.fScore)
