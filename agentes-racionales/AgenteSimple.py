class Agente:
    def __init__(self,env):
        self.env = env
        self.posX = env.agentX
        self.posY = env.agentY
        self.sizeX = env.sizeX
        self.sizeY = env.sizeY
        self.sucio = False;

    def up(self):
        self.env.accept_action(self.env.agentX-1,self.env.agentY)
        #print("Move up.")

    def down(self):
        self.env.accept_action(self.env.agentX+1,self.env.agentY)
        #print("Move down.")

    def left(self):
        self.env.accept_action(self.env.agentX,self.env.agentY-1)
        #print("Move left.")
    
    def right(self):
        self.env.accept_action(self.env.agentX,self.env.agentY+1)
        #print("Move right.")
    
    def stand(self):
        #print("Stand.")
        self.env.accept_action(self.env.agentX,self.env.agentY)

    def suck(self):
        self.env.clean()
        #print("Clean.")


    def perspective(self):
        self.posX = self.env.agentX
        self.posY = self.env.agentY
        self.sucio = self.env.is_dirty()
    
    def think(self):
        while(self.env.acciones>0):
            self.perspective()
            if(self.sucio):
                self.suck()
            else:
                # si estoy en la ultima posicion, subo
                if (self.posX == (self.sizeX-1)) and (self.posY == (self.sizeY-1)):
                    self.up()
                    continue
                if ((self.posX-1) % 2 == 0):
                    if(self.posY == (self.sizeY-1)):
                        self.down()
                    else:
                        self.right()    
                else:
                    if(self.posY == 0 and self.posX != (self.sizeX-1)):
                        self.down()
                    else:
                        self.left()
