import os


print("Bienvenido al programa donde calclamos sus notas")

nota1=float(input("ingrese su primera nota"))
nota2=float(input("ingrese su segunda nota"))
nota3=float(input("ingrese su tercera nota"))
nota4=float(input("ingrese su cuarta nota"))
nota5=float(input("ingrese su quinta nota"))

cantidad = 5
aprobado = 3.5
print(f"Sus notas ingresadas son : {nota1} , {nota2} , {nota3} , {nota4} , {nota5}.")
promedio= (nota1 + nota2 + nota3 + nota4 + nota5) / cantidad
print(f"El promedio de notas es : {promedio}")

if promedio >= aprobado :
    print("Aprobo su materia, felicidades")
else :
    print("Reprobo su materia")