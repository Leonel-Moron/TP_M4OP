import time #libreria para medir tiempo de ejecución

#Vamos a buscar el numero primo mil

#Busquemos un iterador primero
#El final del iterador va a ser el numero ingresado por consola // primo mil
#Seria un contador de corte el input

#¿¿Como calcular un primo???
#Un numero que se divide por 1 y por si mismo, o sea tiene 2 divisores que tienen resto = 0
#Podemos usar el %2 como idea
#Para limpiar codigo podemos poner que chequee si es primo en una funcion
""""        
    La idea es que el primo es divisible por 1 y por si mismo, entonces tiene q haber una bandera q active cuando
    se divida. Y si es resto = 0, se incrementa la bandera.
    Si contador/bandera > 2 significa que no es primo xq mas de 2 numeros lo dividieron con resto 0
    1 no es primo asi q para q sea primo es cont/bandera == 2
"""

def esPrimo(num):               # Funcion para validar si el nro que reciba es Primo
    cont = 0
    for i in range(1,num+1):    # Iteramos desde 1 hasta el numero que pasamos
        if num%i == 0:          # Dividimos el numero recibido por todos sus previos
            cont +=1            # Si el resto es 0 sumamos al contador 1  
    if cont == 2:               # La condición que aclaramos antes para q sea primo       
        return True             # Si es primo retornamos un TRUE
    else:
        return False            #Si no es primo retornamos un FALSE
                                #return True if cont == 2 or num == 1 else False        (Operador ternario)

def buscarPrimo(busqueda):
    listaPrimo = []                             # En esta lista vamos a guardar los primos que encontremos
    aumentador = 1                              # Es lo que vamos a usar para iterar
    contador = 0
    while(True):                                # True loopea hasta que cortemos con un break
        if esPrimo(aumentador):                 # Llamamos a la funcion para chequear si es primo, pasando un 1 primero que va a ir en aumento
            listaPrimo.append(aumentador)       # Si la funcion nos devuelve un TRUE, guardamos el numero en una Lista
            contador += 1                       # Y ademas aumentamos +1 el contador 
        if contador == busqueda:                # Cuando el contador llegue al input cortamos, Podriamos escribir la condicion de corte en el While
            break                               # Cortamos el loop con un break, la lista ya contiene todos los primos que hay hasta el nro que pasamos
        aumentador +=1                          # Aumentador para pasar a la funcion esPrimo un numero cada vez mas grande.
    return listaPrimo[-1]                       # Devolvemos el ultimo primo q guardamos en la Lista: el numero primo que pedimos buscar


buscar = int(input("Ingresa el numero primo que quieras buscar: "))  # Pedimos por consola el nro primo que vamos a buscar
inicio = time.time()
resultado = buscarPrimo(buscar)                 # Llamamos a la función, que a su vez va a llamar a la otra funcion. Pasamos el input y el resultado lo guardamos en la variable
fin = time.time()
print("El numero primo", buscar, "es el:",resultado)
print("Tardamos en encontrarlo: ", fin-inicio, " seg")
