import time

from estadistica import calcEstadistica
from genetico import ExecGenetic
from hillClimb import ExecHillClimb
from templeSim import ExecTempleSim
aux = 0
bestSol = 0
tiempos=[]
startTotal = time.time()
while aux < 30:
    startT = time.time()
    sol = ExecGenetic(8)
    tf = time.time()-startT
    tiempos.append(tf)
    print(tf)
    aux += 1
    if (sol == 0):
        bestSol += 1
        calcEstadistica(tiempos)
    print()
print("Tiempo de ejecución total:",time.time()-startTotal)
print("Se obtuvo una una solución "+str(bestSol),"veces")
print("Llegó a la solución óptima con un ptje de: "+str(bestSol/30*100)+"%")