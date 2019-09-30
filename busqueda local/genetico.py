import random

#devuelve la suma de todos los fitness
def getAllFitness(diccionario):
    fitness = 0
    for key,elems in diccionario:
        fitness += len(diccionario[key])
    return fitness

def PrintBoard(heurBoard,board):
    lenx = len(heurBoard)
    leny = len(heurBoard)
    fin = ""
    valor = ""
    for i in range(0,lenx):
        print("[",end="")
        for j in range(0,leny):
            if j != leny-1:
                fin = ","
            else:
                fin = "]"
            
            if i == board[j]:
                valor = "#"
            else:
                valor = heurBoard[i][j]

            print(valor,end=fin)
        print("")
    # aux = input("enter para seguir")
    print("-----------------------------")

#seleccion proporcional
def Selection(population):
    #obtengo los fitness de la poblacion
    randProb = random.randint(0,100) / 100
    pr = 0
    sumFitness = sum(list(population.keys()))

    for fit,fitList in population.items():
        pr += (fit/sumFitness)
        if(pr > randProb):
           print("encontrado")
           print(pr)
           print(fitList)
           return fitList
    print("PR:",pr)

#seleccion por torneo
def Selection2(population):
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
def Evolution(population):
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
        
        parent1 = replace(parent1,changeMap)
        newPopulation.append(parent1.copy())
        
        parent2 = replace(parent2,changeMap)
        newPopulation.append(parent2.copy())
        aux += 1
    
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
    val = 0
    selected = []
    mutProb = 0.01 #probabilidad de mutar
    mutCant = 1 #porcentaje de la poblacion que muto
    while life < 1000:
        life+=1
        selected = Selection2(population)
        randMut = random.randint(0,100) / 100
        evolved = Evolution(selected)
        population = generatePopulation(evolved)
        if mutProb == randMut:
            size = mutCant*populationSize/100
            Mutation(population,size)

        bestFit = min(list(population.keys()))
        if (bestFit == 0):
            break
        
    print("Intentos:",life+1)
    fSol = min(list(population.keys()))
    solution = population[fSol][0]
    print(solution)
    print("Fitness:",fSol)
    return fSol