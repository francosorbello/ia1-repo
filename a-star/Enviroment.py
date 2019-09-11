from PyColor import *
class Enviroment:
    def __init__(self,sizeX,sizeY,rateObstacle):
        self.sizeX = sizeX
        self.sizeY = sizeY
        # self.world = [[0]*self.sizeX for i in range(self.sizeY)]
        self.world = self.SampleMap2()
        self.rateObstacle = rateObstacle
        self.startPos = [0,0]
        self.endPos = [6,1]
    
    
    def SampleMap(self):
        map = [["_"]*self.sizeX for i in range(self.sizeY)]
        for i in range(0,5):
            map[i][3] = 1
        map[i][2]=1
        return map
    
    def SampleMap2(self):
        map = [["_"]*self.sizeX for i in range(self.sizeY)]
        for i in range(0,4):
            map[i][3] = 1
        for j in range(0,3):
            map[i][j] = 1
        map[2][3] = "_"
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

    def PrintPath(self,path):
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
                elif [i,j] in path:
                    valor = "\033[92m{}\033[00m" .format("*")
                else:
                    valor = "-"

                if [i,j] == self.startPos:
                    valor = "\033[93m{}\033[00m" .format("I")

                if [i,j] == self.endPos:
                    valor = "\033[93m{}\033[00m" .format("F")
                
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
            if(move[0]>-1 and move[1]>-1 and move[0]<self.sizeX and move[1]<self.sizeY and self.world[move[0]][move[1]] != 1):
                neighbors.append(move)
        return neighbors