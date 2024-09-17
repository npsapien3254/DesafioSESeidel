#Funcion que nos permite obtener la matriz transformada a partir de las matrices iniciales A, B
def def_generar_matriz(A, B, tam):
    x = 0 
    M = [0]*tam
    C = [0]*tam
    for i in A:
        linea = [0]*tam
        y = 0
        for j in i:
            linea[y] = (j/i[x])*(-1)
            if(x==y): linea[y] = 0
            y+=1
        M[x] = linea
        C[x] = B[x]/i[x]
        x+=1
    #Esta funcion retorna las matrices M, C para utilizarlos en el metodo de Seidel
    return M, C

#Funcione que usa el metodo Seidel para calcular el valor X del sistema de ecuaciones
def def_seidel_iteraciones(M,C, tam):
    #Arreglos donde se almacenan los valores calculados y los errores correspondientes
    valores = [0]*tam
    errores = [0]*tam
    #Definir la tolerancia del sistema
    TOLERANCIA = 1e-7
    #Contador que nos permite iterar hasta un limite MAX_ITER
    cont = 0
    MAX_ITER = 100
    sw = True
    while cont<MAX_ITER and sw==True:
        x = 0
        #Calculo de los valores de cada iteracion
        for i in M:
            acu = 0
            for j in range(tam):
                acu += i[j]*valores[j]
            errores[x] = abs(valores[x]-(acu+C[x]))/abs(acu+C[x])
            valores[x] = acu+C[x]
            x+=1
        #Loop que verifica si algun error calculado es cero, ya que,
        for k in range(tam):
            if(errores[k]<=TOLERANCIA): sw=False
            
        #Lineas de codigo para mostrar las iteraciones y sus errores correspondientes
        for j in range(tam):
            print(f'x{j+1}: {valores[j]} | error: {errores[j]}')
        print('--------------------------------')
        cont+=1
    return valores, cont



#MAIN del programa

#Lineas de codigo para poder ingresar las matrices por consola        
#tam = int(input(f'Ingrese el tamaño de la matriz nxn-->'))
#A = #[0]*tam
#for i in range(tam):
#    linea = list(map(float,input(f'Ingrese la fila {i+1}-->').split()))
#    A[i] = linea
#B = list(map(float,input(f'Ingrese los valores de la matriz B -->').split()))

tam = 3
A = [[0.52, 0.2, 0.25],
     [0.3, 0.5, 0.2],
     [0.18, 0.3, 0.55]]

B = [4800, 5810, 5690]

#generacion de matrices M, C
M,C = def_generar_matriz(A, B, tam)
#Generar resultados del sistema de ecuaciones
X, numIteraciones = def_seidel_iteraciones(M, C, tam)
print(f"""Resultados finales en metros cubicos, tras {numIteraciones+1} iteraciones:
Para la cantera 1: {X[0]}
Para la cantera 2: {X[1]}
Para la cantera 3: {X[2]}
""")