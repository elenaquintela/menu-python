#!/usr/bin/python3
import os
from pathlib import Path

os.getlogin

def eDirectorio():
    f = str(input("Introduce o nome dun ficheiro: "))
    print(f)
    ficheiro = Path().absolute()
    q = ficheiro / f
    if q.exists():
        print("Existe")
    else:
        print("Non existe")      
    if q.is_dir():
        print("O ficheiro é un directorio")
    else:
        print("O ficheiro é un arquivo")
    input("Preme enter para continuar ")   

def EBisiesto():
    ano = int(input("Introduce un ano: "))
    if ano % 4 == 0:
        print("É bisiesto")
    else:
        print("Non é bisiesto")
    input("Preme enter para continuar ")

def areaTriangulo():
    base = float(input("Introduce a base: "))
    altura = float(input("Introduce a altura: "))
    area = (base * altura) / 2
    print(f"A área é {area}")
    input("Preme enter para continuar ")
    return area

def taboaMultiplicar():
    num = int(input("Introduce un número: "))
    for a in range(11):
        mult = a * num
        print(f"{a} x {num} = {mult}")
    input("Preme enter para continuar ")
    return mult

def parImpar():
    num = int(input("Introduce un número: "))
    if num % 2 == 0:
        print(f"{num} é par")
    else:
        print(f"{num} é impar")
    input("Preme enter para continuar ")

opcion = " "
while opcion != "f":
    print("MENÚ:")
    print("a) Arquivo ou directorio")
    print("b) Ano bisiesto")
    print("c) Área dun triángulo")
    print("d) Táboa de multiplicar")
    print("e) Par ou impar")
    print("f) Saír")
    opcion = input("Elixe unha opción: ")

    if opcion == "a":
        eDirectorio()
    elif opcion == "b":
        EBisiesto()
    elif opcion == "c":
        areaTriangulo()
    elif opcion == "d":
        taboaMultiplicar()
    elif opcion == "e":
        parImpar()
    else:
        print("Saíndo")
