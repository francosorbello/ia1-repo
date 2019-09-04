import random

def CopyList(lista):
    nList = []
    for i in lista:
        nList.append(i)
    return nList
    
    return list
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

def CreateBoard(n):
    board = [0]*8
    for i in range(0,n):
        queenPos = random.randint(0,n-1)
        board[i] = queenPos
    return board

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

n = 8
board = CreateBoard(n)
#heurTable es una matriz con los valores de la heuristica
heurTable = [[0]*n for i in range(n)]

# board = [4,5,6,3,4,5,6,5]
h = heuristic(board)
life = 0
while life < 10000:
    
    solutions = []
    for y in range(0,len(board)):
        tempBoard = CopyList(board)
        for x in range(0,len(board)):
            # print("H Inicial:",h)
            #tempBoard es la tabla con la reina movida
            tempBoard[y] = x
            tempH = heuristic(tempBoard)
            heurTable[x][y] = tempH
            if(tempH < h):
                h = tempH
                solutions.append([x,y])
        
    # PrintBoard(heurTable,board)        
    
    #selecciono solucion al azar
    if len(solutions) > 0:
        solNum = random.randint(0,len(solutions)-1)
        newSol = solutions[solNum]
        board[newSol[1]] = newSol[0]
    if h==0:
        break
    life += 1
print()
print("#-----------#")
PrintBoard(heurTable,board)        
print(board)
print("Intentos:",life)
print("H final:",h)



