#Un numero primo es un numero natural, entero y positivo
#debe ser mayor que uno, debe ser divisible por 1 y para si mismo
#para saber si una division es exacta debemos aplicar modulo "%" y que el resultado de cero "0"
#si el resultado de la division es "0" quiere decir que ese numero no es primo

#problema

#si queremos que todo el siguiente programa se repita por cada numero de un cierto intervalo lo pondremos dentro de un "for"
for num in range(1,1000):
    #verificar si el numero es natural y mayor a "1"
    if num > 1:
    #realizamos un contador para saber cuantos restos me dieron "0" (si el contador queda en cero es un numero primo)
    cont=0
    #La iteracion comienza desde 2
    i=2
    #si en un resto me da "0" ya corto el ciclo utilizando "while"
    #recorre desde i hasta el numero que ingresa el usuario, e "i" lo vamos aumentando en "1"
    #y mientras el contador sea igual a "0"
    #en el momento que el programa encuentre un resto el contador aumentara en 1, por lo que cuando vuelva al bucle while se cortara porque no sera un numero primo
    while i<num and cont==0:
        #en todas las iteraciones se deben de hacer modulos "%"
        resto=num%i

        if resto==0:
           cont+=1
        i+=1
    #si el contador quedo con el valor de cero el numero es primo
    if cont==0 
    print(num)
    #asdasdasdasd