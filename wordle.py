import random 
import linecache
from threading import Timer

def una_funcion():
    if palabraIngresada != palabra:
        print(" ")
        print("Se acabo el tiempo, la palabra era: ", palabra)
        exit()

t = Timer(10.0, una_funcion)
t.start()

f = open("diccionario.txt", "r")
palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
while len(palabra) != 5:
    palabra = linecache.getline("diccionario.txt",random.randint(1,80383))
    palabra = palabra.lower()[:-1]
print(palabra)
   
palabraIngresada = ""

while palabraIngresada != palabra: 
    palabraIngresada = str(input("ingrese palabra (de 5 letras): "))
    comparativa = ["", "", "", "", ""]
    i = 1
    for i in range (len(palabra)):
        if palabraIngresada[i-1] == palabra[i-1]:
            comparativa[i-1] = "="
        elif palabraIngresada[i-1] in palabra:
            comparativa[i-1] = "-"
        else:
            comparativa[i-1] = " "
        i += 1
    
    
    print(palabraIngresada[0], " ", palabraIngresada[1], " ", palabraIngresada[2], " ", palabraIngresada[3], " ", palabraIngresada[4])
    print(comparativa[0], " ", comparativa[1], " ", comparativa[2], " ", comparativa[3], " ", comparativa[4])


if palabraIngresada == palabra:
    print("ganaste!!  gg")
    exit()