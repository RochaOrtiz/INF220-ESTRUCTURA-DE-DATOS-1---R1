#PRIMER CODIGO SIN PEP8
#---------------------------------------------------------------------------------------------
def calcularpromedio(lista):
    suma=0
    for i in lista:
        suma=suma+i
    return suma/len(lista)

nombre="Carlos"
edAD=20
notas=[80,90,75,85]

print("Nombre:",nombre)
print("Edad:",edAD)
print("Promedio:",calcularpromedio(notas))

#---------------------------------------------------------------------------------------------

#CODIGO CORREGIDO USANDO LA PRACTICA DE PEP8

#---------------------------------------------------------------------------------------------
def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma = suma + nota

    return suma / len(notas)


nombre = "Carlos"
edad = 20
notas = [80, 90, 75, 85]

print("Nombre:", nombre)
print("Edad:", edad)
print("Promedio:", calcular_promedio(notas))

#-----------------------------------------------------------------------------------------------

