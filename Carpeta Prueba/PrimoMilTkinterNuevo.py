import time 
import tkinter as tk
import pygame as pg



def esPrimo(num):               # Funcion para validar si el nro que reciba es Primo
    cont = 0
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
    label2 = tk.Label(miFrame, text="El primo numero "+ inp2.get() + " es el : " + str(resultado))
    label2.grid(row=3,column=1, columnspan=2, padx=10,pady=10)
    
    label3 = tk.Label(miFrame, text= "Se tardó en encontrarlo: "+ str(tiempo) + "seg")
    label3.grid(row=4,column=1, columnspan=2, padx=10,pady=10)
    pg.mixer.init()
    pg.mixer.music.load("Carpeta Prueba\sonido.mp3")
    pg.mixer.music.play()

root = tk.Tk()
root.config(background="dark blue", padx=20, pady=20)
root.title("App para buscar numeros primos")

miFrame = tk.Frame()
miFrame.pack(expand="True")



label1 = tk.Label(miFrame, text="Indique el numero primo que quiera buscar")
label1.grid(row=0,column=1, columnspan=2, padx=10,pady=10)

inp2 = tk.StringVar()
inp = tk.Entry(miFrame, background="black", textvariable=inp2, foreground="green")
inp.grid(row=1,column=1, columnspan=2,padx=10,pady=10)

botonBuscar = tk.Button(miFrame, text="Buscar", command=mostrarPrimo)
botonBuscar.grid(row=2,column=1, padx=10,pady=10)

botonSalir = tk.Button(miFrame, text="Salir", command=salir)
botonSalir.grid(row=2,column=2, padx=10,pady=10)

root.mainloop()

