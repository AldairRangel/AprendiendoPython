# EDGAR ALDAIR RANGEL GARCIA        MATRICULA: 1741207      SALON 835
#FECHAD DE CREACION: 20/09/2019

Cuantas = int(input("Dime la cantidad de nombres que requieres guardar \n"))
Contador = 1
NombresGuardados = []

while Contador <= Cuantas :
    Nombre = input("Dame el nombre a guardar \n")
    Contador = Contador + 1
    NombresGuardados = NombresGuardados + [Nombre]

print (NombresGuardados)