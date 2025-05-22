#Ejercicio 5: Identificar si el numero que ingreso es un numero par o impar

Num=int(input("Ingrese un numero para identificar si es par o impar"))

residuo=Num%2==0

if residuo:
    print("El numero es par")
else:
    print("El numero es impar")