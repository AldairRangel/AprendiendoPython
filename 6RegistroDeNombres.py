#Edgar Aldair Rangel García GRUPO 22 SALON 835 MATRICULA: 1741207

Cantidad = int(input("Dime la cantidad de nombres a guardar: "))
contador = 1
listanombre = []
while contador <= Cantidad:
    nombre = input("Dame un nombre: ")
    contador = contador + 1
    listanombre = listanombre + [nombre]
    print (listanombre)