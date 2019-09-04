class Enviroment:
    def __init__(self,sizeX,sizeY,rateObstacle):
        self.sizeX = sizeX
        self.sizeY = sizeY
        # self.world = [[0]*self.sizeX for i in range(self.sizeY)]
        self.world = self.SampleMap()
        self.rateObstacle = rateObstacle
    
    def SampleMap(self):
        map = [["_"]*self.sizeX for i in range(self.sizeY)]
        for i in range(0,5):
            map[i][3] = 1
        map[i][2]=1
        return map

    def print_enviroment(self):
        lenx = self.sizeX
        leny = self.sizeY
        fin = ""
        valor = ""
        for i in range(0,lenx):
            print("[",end="")
            for j in range(0,leny):
                if j != leny-1:
                    fin = ","
                else:
                    fin = "]"

                if self.world[i][j]==1:
                    valor = "#"
                else:
                    valor = self.world[i][j]
                
                print(valor,end=fin)
            print("")
        # aux = input("enter para seguir")
        print("-----------------------------")



    def WorldGenerator(self):
        totalSquares = self.sizeX * self.sizeY
        obstacles = (self.rateObstacle * totalSquares)/100
        while(obstacles > 0):
            x = random.randint(0,self.sizeX-1)
            y = random.randint(0,self.sizeY-1)
            self.world[x][y] = 1

    def GetNeighbors(self,x,y):
        neighbors = []
        #cases = arriba, abajo, derecha, izquierda
        cases = [ [x+1,y],[x-1,y],[x,y+1],[x,y-1] ]
        for move in cases:
            #para cada caso me fijo que no se salga de los limites ni que sea obstaculo
            if(move[0]<self.sizeX and move[1]<self.sizeY and self.world[move[0]][move[1]]):
                neighbors.append(move)
        return neighbors