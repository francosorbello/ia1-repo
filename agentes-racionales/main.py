from agentes import *
import random
            
env = Enviroment(64,64,80)
agente1 = Agente(env)
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