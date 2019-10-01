#Edgar Aldair Rangel García GRUPO 22 SALON 835 MATRICULA: 1741207

print("Bienvenido")

veces = int(input("¿Cuantas palabras tiene tu frase?: "))
contador = 1
ListadoPalabras = ""
while contador <= veces:
    palabras = input("Ingresa la palabra: ")
    ListadoPalabras = ListadoPalabras + palabras
    contador = contador + 1

palindromo = ListadoPalabras [::-1]
print (ListadoPalabras)
if ListadoPalabras == palindromo:
    print("Esta es una frase palindroma")
else:
    print ("Esta frase no es palindroma")

print("Fin del ejercicio")