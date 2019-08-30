import random
class AgenteRandom:
    def __init__(self,env):
        self.env = env
        self.posX = env.agentX
        self.posY = env.agentY
        self.sizeX = env.sizeX
        self.sizeY = env.sizeY
        self.sucio = False;
        self.acciones = {
            1: "up",
            2: "down",
            3: "left",
            4: "right",
            5: "stand",
        }

    def up(self):
        self.env.accept_action(self.env.agentX-1,self.env.agentY)
        # print("Move up.")

    def down(self):
        self.env.accept_action(self.env.agentX+1,self.env.agentY)
        # print("Move down.")

    def left(self):
        self.env.accept_action(self.env.agentX,self.env.agentY-1)
        # print("Move left.")
    
    def right(self):
        self.env.accept_action(self.env.agentX,self.env.agentY+1)
        # print("Move right.")
    
    def stand(self):
        # print("Stand.")
        self.env.accept_action(self.env.agentX,self.env.agentY)

    def suck(self):
        self.env.clean()
        # print("Clean.")


    def perspective(self):
        self.posX = self.env.agentX
        self.posY = self.env.agentY
        self.sucio = self.env.is_dirty()
    
    def think(self):
        while(self.env.acciones>0):
            self.perspective()
            # self.env.print_enviroment()
            if(self.sucio):
                self.suck()
                continue
            nroAccion = random.randint(1,5)
            nombreAccion = self.acciones.get(nroAccion)
            accion = getattr(self,nombreAccion)
            accion()
