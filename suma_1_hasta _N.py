#Ejercicio 9:Pidir un número N (positivo) y muestra la suma del 1 hasta N.

Num=int(input("Ingrese un numero entero: "))

if Num<0:
    print("Error: Ingrese un numero que no sea negativo: ")

suma= Num * (Num + 1)//2

print(f"La suma de los numeros del 1 hasta N es: {suma}")