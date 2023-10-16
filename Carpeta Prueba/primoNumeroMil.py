#Vamos a buscar el numero primo mil

#Busquemos un iterador primero
#El final del iterador va a ser primoNumeroMil = 1000
#Seria un contador de corte el primo mil


#Como calcular un primo???
#Un numero que se divide por 1 por si mismo
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


numeroSumando = 0
contadorWhile = 0
ListaWhile = []


#Con while podemos hacerlo infinito sin saber cuanto tenemos q iterar de antemano
#Falta pasar a codigo para verificar si es primo un nro
while(True):
    if numeroSumando %2 == 0 and numeroSumando>0:
        ListaWhile.append(numeroSumando)
        contadorWhile +=1
    if contadorWhile == 15:
        break
    numeroSumando +=1

print(ListaWhile)
print("El numero par numero ", contadorWhile, " es: ", ListaWhile[-1])

    