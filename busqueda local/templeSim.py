import random
import math
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

def ExecTempleSim(n):
    board = CreateBoard(n)

    h = heuristic(board)
    life = 0

    while life < 10000:
        tempBoard = board.copy()
        
        #obtengos vecino random
        y = random.randint(0,len(board)-1)
        x = random.randint(0,len(board)-1)
        
        tempBoard[y] = x
        tempH = heuristic(tempBoard)
        
        #si menos reinas se comen es una solucion mejor
        if(tempH <= h):
            h = tempH
            solution = [x,y]
            board[y] = x
            if h==0:
                break
        else:
            prob = random.random()
            t = (10000-life+1)/10000
            e = math.exp((h-tempH)/t)
            if(prob < e):
                h = tempH
                solution = [x,y]
                board[y] = x
        
        life += 1
    print()
    print("#-----------#")
    # PrintBoard(heurTable,board)        
    print(board)
    print("Intentos:",life)
    print("H final:",h)
    return h
ExecTempleSim(8)