#Ejercicio 4: Identificar si un numero es positivo, negativo o es cero

num=int(input("Ingrese un numero para identificar si es positivo, negativo o cero: "))

if num>=1:
    print("El numero es positivo ")
elif num<0:
    print("El numero es negativo ")
else:
    print("El numero es 0 ")