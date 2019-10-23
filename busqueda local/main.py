import time, csv
from estadistica import calcEstadistica
from genetico import ExecGenetic
from hillClimb import ExecHillClimb
from templeSim import ExecTempleSim

def calcularDatos(arcsv,algoritmo,n):
    nIter = []
    aux = 0
    while aux < 30:
        startT = time.time()
        sol = algoritmo(n)
        tf = time.time()-startT
        aux += 1
        nIter = [algoritmo.__name__,n,aux,sol[0],sol[1],tf]
        arcsv.writerow(nIter)
        print(aux)
    print("#--#")
    arcsv.writerow(["","","","","",""])

aux = 0
with open('datos.csv', mode='w') as archivo:
    datos = csv.writer(archivo,delimiter=",")
    #--n = 8--#
    calcularDatos(datos,ExecGenetic,(8))
    calcularDatos(datos,ExecHillClimb,(8))
    calcularDatos(datos,ExecTempleSim,(8))
    #--n = 10--#
    calcularDatos(datos,ExecGenetic,(10))
    calcularDatos(datos,ExecHillClimb,(10))
    calcularDatos(datos,ExecTempleSim,(10))

# with open('ejb.csv', mode='w') as archivo:
#     datos = csv.writer(archivo,delimiter=",")
#     datos.writerow(ExecHillClimb(8))
#     datos.writerow(ExecTempleSim(8))
#     datos.writerow(ExecGenetic(8))
