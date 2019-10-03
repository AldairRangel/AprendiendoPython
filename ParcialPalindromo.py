#Autor: Edgar Aldair Rangel García      MATRICULA: 1741207      SALON 835
#Fecha de creacion: 15/09/2019

nom=input("Introduzca una palabra: ")
palindromo = nom[::-1]
if palindromo==nom:
    print("Es un palindromo")
else:
    print("No es un palindromo")