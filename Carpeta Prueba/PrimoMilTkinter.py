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



pg.mixer.init()

def mostrarPrimo():
    resultado = buscarPrimo(int((inp.get())))
    var1.set(resultado)
    pg.mixer.music.load("Carpeta Prueba\sonido.mp3")
    pg.mixer.music.play()


def salir():
    ventana.destroy()


ventana = tk.Tk()                  
ventana.geometry("400x400")


lb1 = tk.Label(ventana, text="Ingrese el numero primo a buscar", font="ariel-black", background="orange")
lb1.pack(fill="x")

inp = tk.Entry(ventana, border="5px", font="ariel-black")
inp.pack()

bt1 = tk.Button(ventana, text = "Buscar", font= "ariel-black", command = mostrarPrimo)
bt1.pack()


bt2 = tk.Button(ventana, text = "Salir", font= "ariel-black", command = salir)
bt2.pack()

var1 = tk.StringVar()

lb2 = tk.Label(ventana, textvariable= var1, font="ariel-black", background="orange")
lb2.pack()








ventana.mainloop()
