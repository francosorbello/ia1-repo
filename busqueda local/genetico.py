import random

def CountElems(mapa):
    aux = 0
    for key in mapa:
        aux += len(mapa[key])
    return aux

#devuelve la suma de todos los fitness
def getAllFitness(diccionario):
    fitness = 0
    for key in diccionario:
        fitness += len(diccionario[key])
    return fitness

#seleccion proporcional
def SelectionProp(population):

    randProb = random.randint(0,100) / 100
    pr = 0
    sumFitness = sum(list(population.keys()))

    for fit,fitList in population.items():
        pr += (fit/sumFitness)
        if(pr > randProb):
           print(pr)
           print(fitList)
           return fitList
    print("PR:",pr)

#seleccion por torneo
def SelectionTour(population):
    aux = 0
    fitList = list(population.keys())
    selected = []
    while aux < 50:
        #selecciono 2 fitness al azar
        r1 = random.randint(0,len(fitList)-1)
        r2 = random.randint(0,len(fitList)-1)
        fit1 = fitList[r1]
        fit2 = fitList[r2]
        if fit1 < fit2:
            individuals = population[fit1]
        else:
            individuals = population[fit2]
        #selecciono una de las soluciones con mejor fitness al azar
        sol = random.randint(0,len(individuals)-1)
        #si el individuo ya fue seleccionado lo ignoro. Comentado porque bajaba mucho la performance
        #if (selected.count(individuals[sol]) > 0):
        #    continue
        
        selected.append(individuals[sol])
        aux += 1
    return selected

def replace(parent,changeMap):
    for i in range(0,len(parent)):
        parent[i] = changeMap.get(parent[i],parent[i])
    
    return parent

#almacena los individuos en un mapa segun su fitness
def generatePopulation(individuals):
    population = {}
    keys = population.keys()
    for elem in individuals:
        #calculo fitness
        hInd = heuristic(elem)
        #si la key no existe creo un nuevo elemento
        if (keys.isdisjoint([hInd])):
            population[hInd] = []
            
        population[hInd].append(elem)
        
    return population

def Mutation(population,size):
    rndKey = random.randint(0,len(population.keys())-1)
    individuals = population[list(population.keys())[rndKey]]
    while size > 0:
        #selecciono individuo(s) al azar
        rndInd = random.randint(0,len(individuals)-1)
        genoma = individuals[rndInd]
        #selecciono elementos a permutar al azar
        aux1 = random.randint(0,len(genoma)-1)
        aux2 = random.randint(0,len(genoma)-1)
        auxVal = genoma[aux1]
        genoma[aux1] = genoma[aux2]
        genoma[aux2] = auxVal
        size -= 1
    return population

#genera nuevas cadenas a partir del metodo PMX
def EvolutionPMX(population):
    x1 = 3
    x2 = 4
    newPopulation = []
    aux = 0
    while aux<50:
        #selecciono 2 padres al azar
        rand1 = random.randint(0,len(population)-1)
        rand2 = random.randint(0,len(population)-1)
        if(rand1 == rand2):
            continue
        parent1 = population[rand1]
        parent2 = population[rand2]
        
        #creo mapa con los valores y reemplazo en los hijos
        changeMap = {
            parent1[x1] : parent2[x1],
            parent1[x2] : parent2[x2],
            parent2[x1] : parent1[x1],
            parent2[x2] : parent1[x2]
        }
        
        newParent1 = replace(parent1.copy(),changeMap)
        newPopulation.append(newParent1.copy())
        
        newParent2 = replace(parent2.copy(),changeMap)
        newPopulation.append(newParent2.copy())
        aux += 1
    
    return newPopulation

def Contains(lista,elem):
    if(lista.count(elem)>0):
        return True
    return False

def crossover(parent,child):
    ic = 0
    while len(parent)>0 and ic<len(child):
        #si la pos no esta vacia la ignoro
        if child[ic] != -1:
            ic += 1
            continue

        elem = parent.pop(0)
        if not Contains(child,elem):
            child[ic] = elem
            ic += 1
    return child

#evolucion por crossover
def EvolutionCross(population):
    x1 = 3
    x2 = 4
    newPopulation = []
    aux = 0
    while aux<50:
        #selecciono 2 padres al azar
        rand1 = random.randint(0,len(population)-1)
        rand2 = random.randint(0,len(population)-1)
        if(rand1 == rand2):
            continue
        parent1 = population[rand1]
        parent2 = population[rand2]
        
        #creo los hijos
        child1 = [-1]*len(parent1)
        child1[x1] = parent1[x1]
        child1[x2] = parent1[x2]

        child2 = [-1]*len(parent1)
        child2[x1] = parent2[x1]
        child2[x2] = parent2[x2]
        
        child1 = crossover(parent2.copy(),child1.copy())
        newPopulation.append(child1.copy())
        child2 = crossover(parent1.copy(),child2.copy())
        newPopulation.append(child2.copy())
        aux+=1
    return newPopulation

#retorna el nro de pares de reinas atacandose
def heuristic(board):
    attacking = 0
    for y in range(0,len(board)):
        x = board[y]
        for i in range(y+1,len(board)):
            #me fijo si estan en la misma fila o si los catetos son iguales(para ver si estan en diagonal)
            if x==board[i] or ( abs(x-board[i]) == abs(y-i) ):
                attacking += 1
    return attacking

def ExecGenetic(n):
    #creo poblacion inicial
    populationSize = 100
    #population = { fitness : [individuos] }
    population = {}
    aux = 1
    board = [x for x in range(0,n)]
    population[heuristic(board)] = [board]
    while aux < populationSize:
        
        y1 = random.randint(0,len(board)-1)
        y2 = random.randint(0,len(board)-1)
        
        tempX = board[y1]
        board[y1] = board[y2]
        board[y2] = tempX
        hSol = heuristic(board)
        
        #si la key no existe creo un nuevo elemento
        if (population.keys().isdisjoint([hSol])):
            population[hSol] = []
            
        population[hSol].append(board.copy())
        aux += 1
        
    life = 0
    #sumFitness = getAllFitness(population)
    selected = []
    mutProb = 0.1 #probabilidad de mutar
    mutCant = 1 #porcentaje de la poblacion que muto
    while life < 1000:
        life+=1
        selected = SelectionTour(population)
        randMut = random.randint(0,100) / 100
        evolved = EvolutionCross(selected)
        population = generatePopulation(evolved)
        
        if mutProb == randMut:
            size = mutCant*populationSize/100
            Mutation(population,size)
        #print(population.keys())
        bestFit = min(list(population.keys()))
        if (bestFit == 0):
            break
        
    #print("Intentos:",life)
    fSol = min(list(population.keys()))
    #solution = population[fSol][0]
    #print(solution)
    #print("Fitness:",fSol)
    return (fSol,life)
#ExecGenetic(8)