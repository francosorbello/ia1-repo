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

h = heuristic(board)
life = 0
#t=a*x:funcion schedule
t=0
while life < 1000:
    t += 0.0001
    tempBoard = board.copy()
    
    #obtengos vecino random
    y = random.randint(0,len(board)-1)
    x = random.randint(0,len(board)-1)
    
    tempBoard[y] = x
    tempH = heuristic(tempBoard)
    #si menos reinas se comen es una solucion mejor
    if(tempH < h):
        h = tempH
        solution = [x,y]
    else:
        prob = random.randint(0,99)
        e = math.exp((h-tempH)/t)
        if(prob>e and t>0):
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



