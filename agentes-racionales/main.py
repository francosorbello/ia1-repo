from agentes import *
from agenteEstados import AgenteEstado
import random
            
env = Enviroment(64,64,80)
# agente1 = Agente(env)
aux = input("1. Agente custom | 2. Agente random | 3.Agente con estados: ")
if(aux == "1"):
    agente1 = Agente(env)
elif aux == "2":
    agente1 = AgenteRandom(env)
else:
    agente1 = AgenteEstado(env)

env.world_builder()
print("#--Referencias--#")
print("*: posición del agente.")
print("1: cuadro sucio.")
print("0: cuadro limpio.")
print("")
env.print_enviroment()
aux = input("Presiona enter para empezar.")
print("#--START--#")
agente1.think()
env.get_perfomance()