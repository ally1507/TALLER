import os
print("bienvenido al programa de tablas de multiplicar")

numero= int (input("Ingrese ell numero de tabla que desea consultar:"))
print("Tabla consultada :")

if 1 <= numero <10 :
    print(f"\n Tabla de multiplicar {numero} \n")
    for i in range (1,10 + 1) :
        tabla = numero * 1
        print(f"{numero} * {i} = {tabla}")

else:
    print("ERROR, El numero debe de estar entre 1 y 10")
    