#Vamos a buscar el numero primo mil

#ac� lo que quiero hacer es definir un funci�n que me diga si los numero son primos o no 
def primo (numero):
    if numero <= 1:
        return False
    #primero le digo que el 1 no 
    for i in range (2, int ()): #la funci�n range la pens� poque podes genera un secuencia, pero si tiene otra idea mejor 
        if (numero%i==0) and (numero%1==0):
            return True 
        #y ac� es donde se me rompe, porque no logro decirle que me determine si es par o no

#pienso la segunda funcion que llame a la funcion anterior y que el contador corte cuando encuentre el numero 1000
def primo_numero_mil ():
    contador=0
    while contador <1000: 
        if primo (numero):
            contador += 1
            if contador==1000:
                return #?? 
resultado = primo_numero_mil ()
print (resultado)
print("hola")