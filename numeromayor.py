#Ejercicio 6: Identificar cual de los 3 numeros es mayor

Num1=int(input("Ingrese el primer numero: "))
Num2=int(input("Ingrese el segundo numero: "))
Num3=int(input("Ingrese el tercer numero: "))

if Num1>Num2 and Num1>Num3:
    print(f"El numero mayor es el primer numero: {Num1}")
elif Num2>Num1 and Num2>Num3:
    print(f"El numero mayor es el segundo numero: {Num2}")
else:
    print(f"El numero mayor es el tercer numero: {Num3}")
