import time
#Vamos a buscar el numero primo mil

#Busquemos un iterador primero
#El final del iterador va a ser primoNumeroMil = 1000
#Seria un contador de corte el primo mil


#Como calcular un primo???
#Un numero que se divide por 1 por si mismo, o sea tiene 2 divisores que tienen resto = 0
#Podemos usar el %2 como idea
#Para limpiar codigo podemos poner que chequee si es primo en una funcion

iterador = 100
cont = 0
listaPares = []

#Con for podemos iterar si ya sabemos cuanto queremos iterar de antemano
for i in range(iterador):
    if i % 2 == 0 and i>0:
        listaPares.append(i)
        cont +=1
        if cont == 10:
            break
print(listaPares)
print(listaPares[-1])



def esPrimo(num):
    cont = 0
    for i in range(1,num+1):
        if num%i == 0:
            cont +=1
    return True if cont == 2 or num == 1 else False #Operador ternario
    """Es lo mismo que poner
    if cont == 2 or num == 1:
        return True
    else:
        return False
    """
ListaPrimo=[]    
iter = 887
for i in range(iter+1):
    if esPrimo(i):
        ListaPrimo.append(i)
print("es el primo numero ", len(ListaPrimo), " el ", ListaPrimo[-1])
#Con while podemos hacerlo infinito sin saber cuanto tenemos q iterar de antemano
#Falta pasar a codigo para verificar si es primo un nro


inicio = time.time()
numeroSumando = 0
contadorWhile = 0
ListaWhile = []
while(True):
    if numeroSumando %2 == 0 and numeroSumando>0:
        ListaWhile.append(numeroSumando)
        contadorWhile +=1
    if contadorWhile == 1000:
        break
    numeroSumando +=1


print("El numero par numero ", contadorWhile, " es: ", ListaWhile[-1])

fin =time.time()


print(fin - inicio)
    