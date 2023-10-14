#Vamos a buscar el numero primo mil

#Busquemos un iterador primero
#El final del iterador va a ser primoNumeroMil = 1000
#Seria un contador de corte el primo mil


#Como calcular un primo???
#Un numero que se divide por 1 por si mismo

iterador = 100
cont = 0
listaPares = []

for i in range(iterador):
    if i % 2 == 0:
        listaPares.append(i)
        cont +=1
        if cont == 10:
            break
print(listaPares)
print(listaPares[-1])
    