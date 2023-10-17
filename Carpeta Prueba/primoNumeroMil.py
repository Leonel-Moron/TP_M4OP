import time
#Vamos a buscar el numero primo mil

#Busquemos un iterador primero
#El final del iterador va a ser primoNumeroMil = 1000
#Seria un contador de corte el primo mil

#Como calcular un primo???
#Un numero que se divide por 1 por si mismo, o sea tiene 2 divisores que tienen resto = 0
#Podemos usar el %2 como idea
#Para limpiar codigo podemos poner que chequee si es primo en una funcion

def esPrimo(num):
    cont = 0
    for i in range(1,num+1):    # Iteramos desde 1 hasta el numero que pasamos
        if num%i == 0:          # Dividimos el numero por todos sus previos, si el resto es 0 sumamos al contador 1  
            cont +=1
    """"        
    La idea es que el primo es divisible por 1 y por si, 
    si contador > 2 significa que no es primo xq mas de 2 numeros lo dividieron con resto 0
    Sumamos la condicion num == 1 porque 1 es primo pero no puede cumplir la condicion contador == 2 
    if cont =< 2: incluiria al 1, nos ahorramos escribir 1 condicion
    """
    if cont <=2:                
        return True             #Si es primo retornamos un TRUE
    else:
        return False            #Si no es primo retornamos un FALSE
                                #return True if cont == 2 or num == 1 else False        #Operador ternario


listaPrimo=[]    
aumentador = 1
contadorMil = 0

inicio = time.time()

while(True):                                #True loopea hasta que cortemos con un break
    if esPrimo(aumentador):                 # Llamamos a la funcion para chequear si es primo
        listaPrimo.append(aumentador)       # Si la funcion nos devuelve un TRUE, guardamos el numero en una Lista
        contadorMil += 1                    # Y ademas aumentamos +1 el contador 
    if contadorMil == 1000:                 # Cuando el contador llegue a 1000 cortamos, Podriamos escribir la condicion de corte en el While
        break                               # Cortamos el loop con un break, el contador ya tiene el nro primo MIL
    aumentador +=1                          # Aumentador para pasar a la funcion un numero cada vez mas grande


print("El primo numero mil es: ", listaPrimo[-1])
fin = time.time()
print("Tardamos para encontrarlo: ",fin - inicio)