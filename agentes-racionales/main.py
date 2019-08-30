from Enviroment import Enviroment
from AgenteEstados import AgenteEstado
from AgenteRandom import AgenteRandom
from AgenteSimple import Agente

import random

def obtenerPerformance(agente,env):
    env.world_builder()
    agente.think()
    env.get_perfomance() 
    env.reset_performance()
    print("#--#") 
    print("")  

entornos = [2,4,8,16,32,64,128]
suciedad = [10,20,40,80]


#env = Enviroment(8,8,0.1)

for entorno in entornos:
    print("Mapa de",entorno,"x",entorno)
    for rango in suciedad:
        print("Rango suciedad:",rango/100)
        #genero mapa
        env = Enviroment(entorno,entorno,rango)
        env.seed_generator()
        
        simple = Agente(env)
        random = AgenteRandom(env)
        print("AGENTE SIMPLE")    
        obtenerPerformance(simple,env)
        print("AGENTE RANDOM")
        obtenerPerformance(random,env)
        aux = input("Enter para continuar. ")
        if(aux=="1"):
            break
    if(aux=="1"):
        break
    print("-----------------")
    print("")