class AgenteEstado:
    def __init__(self,env):
        self.env = env
        self.posX = env.agentX
        self.posY = env.agentY
        self.sizeX = env.sizeX
        self.sizeY = env.sizeY
        self.estados = []
        self.enInicio = False
    def up(self):
        self.env.accept_action(self.env.agentX-1,self.env.agentY)
        print("Move up.")

    def down(self):
        self.env.accept_action(self.env.agentX+1,self.env.agentY)
        print("Move down.")

    def left(self):
        self.env.accept_action(self.env.agentX,self.env.agentY-1)
        print("Move left.")
    
    def right(self):
        self.env.accept_action(self.env.agentX,self.env.agentY+1)
        print("Move right.")
    
    def stand(self):
        print("Stand.")
        self.env.accept_action(self.env.agentX,self.env.agentY)

    def suck(self):
        self.env.clean()
        print("Clean.")

    def perspective(self):
        self.posX = self.env.agentX
        self.posY = self.env.agentY
        self.sucio = self.env.is_dirty()
        #guardo el estado actual
        estado = [[self.posX,self.posY],self.sucio]
        self.estados.append(estado)

    # devuelve true o false segun estuvimos en ese cuadro o no
    def estadoConocido(self,x,y):
        estados = self.estados
        pos = [x,y]
        for state in estados:
            if(state[0] == pos):
                return True
        return False

    #esta funcion checkea que estemos en la posicion (0,0)
    def checkInicio(self):
        if(self.posX == 0 and self.posY == 0 and (self.estadoConocido(1,0) or self.estadoConocido(0,1))):
            print("En Inicio!!!")
            self.enInicio = True
        
    def think(self):
        while(self.env.acciones>0):
            self.perspective()
            # self.env.print_enviroment()

            if(self.sucio):
                self.suck()
            else:
                self.checkInicio()
                if(not(self.enInicio)):
                    if(self.posX == 0):
                        self.left()
                    else:
                        self.up()
                else:
                    #en filas pares voy a la derecha
                    if ((self.posX) % 2 == 0):
                        # print(self.posY)
                        if(self.posY == (self.sizeY-1)):
                            self.down()
                        else:
                            self.right()    
                    else:
                        #en filas impares voy a la izquierda
                        if(self.posX==(self.sizeX-1) and self.posY == 0 and self.enInicio):
                            self.stand()
                            continue
                        if(self.posY == 0 and self.posX != (self.sizeX-1)):
                            self.down()
                        else:
                            self.left()
