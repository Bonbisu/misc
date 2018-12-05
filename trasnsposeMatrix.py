import os

dimension = ''
while len(dimension) != 3:
    dimension = input('Insira a dimensao da matriz. Ex: "3x3"')
    
lines, columns = int(dimension[0]),int(dimension[-1])
matrix = [[0 for x in range (columns)] for y in range(lines)]
transpose = [[0 for x in range (lines)] for y in range(columns)]
realDimension = lines * columns

def verifyNull():
    termZero = 0
    for i in range(lines):
        for j in range(columns):
            if matrix[i][j] == 0:
                termZero += 1
            if termZero == realDimension:
                nul=input('Matriz Nula inserida, deseja inserir outra matriz? [s\n]: ')
                if nul == 's':
                    writeMatrixEach()
                else:
                    break                

def writeMatrixEach():
    for i in range(lines):
        for j in range(columns):
            term = input('Insira o termo a[' + str(i+1) + '][' + str(j+1) + '] da matriz : ')
            matrix[i][j] = term

def transposeMatrix():
    for i in range(columns):
        for j in range(lines):
            transpose[i][j] = matrix[j][i]

def matrixFormat():
    print('Matriz: ')
    for i in range(lines):
        print(matrix[i])

def transposeFormat():
    print('Transposta: ')
    for i in range(columns):
        print(transpose[i])

while True:
    c=int(input('Operações com matrizes: \n 1- Inserir matrix \
    \n 2- Imprimir matriz \
    \n 3- Imprimir a transposta da matrix \
    \n 4- Sair\n'))
    # semelhante a um 'switch-case' usando 'elifs'
    if c==1:
        os.system('clear')
        writeMatrixEach()
        transposeMatrix()
    if c==2:
        os.system('clear')
        verifyNull()
        matrixFormat()
    if c==3:
        os.system('clear')
        verifyNull()
        transposeMatrix()
        transposeFormat()
    if c==4:
        quit()
    else:
        print ('opção inexistente')


writeMatrixEach()
transposeMatrix()
print('\n')
matrixFormat()
print('\n')
transposeFormat()
