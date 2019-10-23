import random
from PriorityQueue import PriorityQueue

def CopyList(lista):
    nList = []
    for i in lista:
        nList.append(i)
    return nList

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
    print("-----------------------------")

def CreateBoard(n):
    board = [0]*n
    posibilities = [x for x in range(0,n)]
    x = 0
    while len(posibilities)>0:
        i = random.randint(0,len(posibilities)-1)
        elem = posibilities.pop(i)
        board[x] = elem
        x += 1
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

def ExecHillClimb(n):
    board = CreateBoard(n)
    #h_list = [] 
    h = heuristic(board)
    life = 0
    while life < 1000:
        solutions = PriorityQueue()
        for y in range(0,len(board)):
            tempBoard = board.copy()
            for x in range(0,len(board)):
                #tempBoard es la tabla con la reina movida
                tempBoard[y] = x
                tempH = heuristic(tempBoard)
                if(tempH < h):
                    h = tempH
                    solutions.Enqueue([x,y],tempH)
        #selecciono solucion al azar
        #h_list.append(h)
        if solutions.Length() > 0:
            newSol = solutions.Dequeue()
            board[newSol[1]] = newSol[0]
        if h==0:
            break
        life += 1
    
    return (h,life)
    #return h_list
