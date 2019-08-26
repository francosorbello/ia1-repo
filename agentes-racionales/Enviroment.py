import random
import math
class Enviroment:
    def __init__(self,sizeX,sizeY,dirt_rate):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.agentX = random.randint(0,sizeX-1)
        self.agentY = random.randint(0,sizeY-1)
        self.dirt_rate = dirt_rate 
        self.world = [[0]*sizeX for i in range(sizeY)]
        self.acciones = 10000
        self.rendimiento = 0

    def world_builder(self):
        total_casillas = self.sizeX * self.sizeY
        cant_sucias = (self.dirt_rate * total_casillas)/100
        cant_sucias = self.redondeo(cant_sucias)
        while(cant_sucias > 0):
            new_x = random.randint(0,self.sizeX-1)
            new_y = random.randint(0,self.sizeY-1)
            if(self.world[new_x][new_y] != 1):
                self.world[new_x][new_y] = 1
                cant_sucias -= 1
            
    def clean(self):
        self.world[self.agentX][self.agentY] = 0
        self.set_perfomance()
            
    def mover(self,posX,posY):
        if (posX >= 0 and posX < self.sizeX) and (posY>=0 and posY < self.sizeY):
            self.agentX = posX
            self.agentY = posY
            return True
        return False
        
    def accept_action(self,*args):   
        self.acciones -= 1     
        if len(args) == 1:
            return self.is_dirty()
        elif len(args) == 2:
            x,y = args
            return self.mover(x,y)
        else:
            print("Numero de parametros incorrecto")

    def is_dirty(self):
        if(self.world[self.agentX][self.agentY] == 1):
            return True
        return False

    def redondeo(self,x):
        if (math.floor(x)+0.5)<x:
            return math.ceil(x)
        return math.floor(x)

    def get_perfomance(self):
        total_casillas = self.sizeX * self.sizeY
        cant_sucias = (self.dirt_rate * total_casillas)/100
        cant_sucias = self.redondeo(cant_sucias)
        print("El agente limpió",self.rendimiento,"cuadros de los",cant_sucias,"cuadros sucios.")
        ptje_limpio = self.rendimiento * 100 / cant_sucias
        print("Eso es aproximadamente un",round(ptje_limpio,2),"% de la suciedad total.")
    
    def set_perfomance(self):
        self.rendimiento += 1

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
                if i==self.agentX and j==self.agentY:
                    valor = "*"
                else:
                    valor = self.world[i][j]
                
                print(valor,end=fin)
            print("")
        # aux = input("enter para seguir")
        print("-----------------------------")

