M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(cuadricula, hilera, columna, numero):
    for x in range(9):
        if cuadricula[hilera][x] == numero:
            return False
             
    for x in range(9):
        if cuadricula[x][columna] == numero:
            return False
 
 
    startRow = hilera - hilera % 3
    startCol = columna - columna % 3
    for i in range(3):
        for j in range(3):
            if cuadricula[i + startRow][j + startCol] == numero:
                return False
    return True
 
def Suduko(cuadricula, hilera, columna):
 
    if (hilera == M - 1 and columna == M):
        return True
    if columna == M:
        hilera += 1
        columna = 0
    if cuadricula[hilera][columna] > 0:
        return Suduko(cuadricula, hilera, columna + 1)
    for numero in range(1, M + 1, 1): 
     
        if solve(cuadricula, hilera, columna, numero):
         
            cuadricula[hilera][columna] = numero
            if Suduko(cuadricula, hilera, columna + 1):
                return True
        cuadricula[hilera][columna] = 0
    return False
 
'''0 significa que la casilla no esta activada'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]
 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("la solucion no existe :(")