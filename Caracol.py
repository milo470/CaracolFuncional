
def getArchivo():
    return "Matriz.txt"

def leer_archivo(txt):
    return [[int(x) for x in y] for y in [x.split(" ") for x in [y.strip("\n") for y in open(txt).readlines()]]]

print (leer_archivo(getArchivo()))

def tamano(matriz):
    return len(matriz[0])
def getArriba(matriz):
    return matriz[1:]

def getDerecha(matriz):
    [x.pop() for x in matriz]
    return matriz

def getAbajo(matriz, tamano):
    return matriz[:(tamano-1)]

def getIzquierda(matriz):
    [x.pop(0) for x in matriz]
    return matriz

def recorrido(direccion, matriz, i, j):
    
    if(i>=0):
        if(j>=0):
            try:
                print(matriz[i][j])
                
                if(direccion == 1):
                    print [[i],[j]]
                    if((j+1) == len(matriz)):
                        recorrido(2, getArriba(matriz), (i), (j)) 
                    recorrido(direccion, matriz, (i), (j+1)) 
                    
                elif(direccion == 2):
                    print [[i],[j]]
                    if((i+1) == len(matriz)):
                        recorrido(3, getDerecha(matriz), (i), (j-1)) 
                    recorrido(direccion, matriz, (i+1), (j)) 
                   
                elif(direccion == 3):
                    print [[i],[j]]
                    if( j == 0):
                        recorrido(4, getAbajo(matriz, len(matriz)), (i-1), (j)) 
                    recorrido(direccion, matriz, (i), (j-1)) 

                elif(direccion == 4):
                    print [[i],[j]]
                    if( i == 0):
                        recorrido(1, getIzquierda(matriz), (i), (j+1)) 
                    recorrido(direccion, matriz, (i-1), (j)) 
            except:
                print(matriz[i][j])
                print [[i],[j]]
                print ("Recorrido finalizado")
                
                
        else:
            print (" ")
            
    else:
        print (" ")
        
        
                
        


print(recorrido(1, leer_archivo(getArchivo()), 0 , 0))
