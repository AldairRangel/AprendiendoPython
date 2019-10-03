#Entrada.py
#Autor: Edgar Aldair Rangel García  AULA: 835 MATRICULA: 17 41 207
#Fecha Elaboración: 24/09/2019

#El método isdigit () devuelve True si todos los caracteres son dígitos; de lo contrario, False.
#La variable booleana tiene como fin detectar si es un digito. De ser asi, indicara si lo capturado es un numero entero. 
#int()  -> entero       float -> decimal

valorIngresado = input("Dame un valor ")
print(type(valorIngresado))
if  str.isdigit (valorIngresado):
    print ("Dato entero. ¡Muy bien!")
else:
    print ("Dato no es entero. Intentar nuevamente")