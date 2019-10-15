import math

def getVarianza(datos,media):
    sol = 0
    for elem in datos:
        sol += (elem-media)**2
    return (sol/len(datos))

def calcEstadistica(datos):
    media = sum(datos)/len(datos)
    print("media:",media)
    varianza = getVarianza(datos,media)
    desviacion = math.sqrt(varianza)
    print("desviacion:",desviacion)
    
