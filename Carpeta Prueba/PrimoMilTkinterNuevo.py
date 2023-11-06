import time 
import tkinter as tk
import pygame as pg

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
    cont = 0                    # Inicializamos un contador
    for i in range(1,num+1):    # Iteramos desde 1 hasta el numero que pasamos
        if num%i == 0:          # Dividimos el numero por todos sus previos, si el resto es 0 sumamos al contador 1  
            cont +=1
    if cont == 2:                
        return True             #Si es primo retornamos un TRUE 
    else:
        return False            #Si no es primo retornamos un FALSE
                                #return True if cont == 2 or num == 1 else False        (Operador ternario)

def buscarPrimo(busqueda):
    listaPrimo = []
    aumentador = 1
    contadorMil = 0
    while(True):                                # True loopea hasta que cortemos con un break
        if esPrimo(aumentador):                 # Llamamos a la funcion para chequear si es primo
            listaPrimo.append(aumentador)       # Si la funcion nos devuelve un TRUE, guardamos el numero en una Lista
            contadorMil += 1                    # Y ademas aumentamos +1 el contador 
        if contadorMil == busqueda:             # Cuando el contador llegue al que pedimos cortamos
            break                               # Cortamos el loop con un break, el contador ya tiene el nro primo MIL
        aumentador +=1                          # Aumentador para pasar a la funcion un numero cada vez mas grande
    return listaPrimo[-1]                       # Devolvemos el ultimo primo q guardamos, el numero mil



def salir():
    pg.mixer.init()
    pg.mixer.music.load("Carpeta Prueba\sonido2.mp3")
    pg.mixer.music.play()
    time.sleep(3)
    root.destroy()

def mostrarPrimo():
    inicio = time.time()
    resultado = buscarPrimo(int(inp2.get()))
    fin = time.time()
    tiempo = fin-inicio
    label2 = tk.Label(miFrame, text="El primo numero "+ inp2.get() + " es el: " + str(resultado),font=("Helvetica", 15))
    label2.grid(row=3,column=1, columnspan=2, padx=10,pady=10)
    
    label3 = tk.Label(miFrame, text= "Se tardó en encontrarlo: "+ str(tiempo) + "seg", font=("Helvetica", 15))
    label3.grid(row=4,column=1, columnspan=2, padx=10,pady=10)
    pg.mixer.init()
    pg.mixer.music.load("Carpeta Prueba\sonido.mp3")
    pg.mixer.music.set_volume(0.5)
    pg.mixer.music.play()


root = tk.Tk()
root.config(background="dark blue", padx=20, pady=20)
root.title("App para buscar numeros primos")

miFrame = tk.Frame()
miFrame.pack(expand="True")



label1 = tk.Label(miFrame, text="Indique el numero primo que quiera buscar",font=("Helvetica", 15))
label1.grid(row=0,column=1, columnspan=2, padx=10,pady=10)

inp2 = tk.StringVar()
inp = tk.Entry(miFrame, background="black", textvariable=inp2, foreground="green", font=("Helvetica", 15))
inp.grid(row=1,column=1, columnspan=2,padx=10,pady=10)

botonBuscar = tk.Button(miFrame, text="Buscar", command=mostrarPrimo, font=("Helvetica", 10))
botonBuscar.grid(row=2,column=1, padx=10,pady=10)

botonSalir = tk.Button(miFrame, text="Salir", command=salir, font=("Helvetica", 10))
botonSalir.grid(row=2,column=2, padx=10,pady=10)

root.mainloop()

