#Ejercicio con el ciclo for para ver las tablas de multiplicar
import os
os.system('cls' if os.name == 'int' else 'clear')

for i in range (0):
    print(i)

tabla=int(input("Ingrese la tabla de multiplicar que desee ver"))
for i in range (1,11):
    print(f"{tabla}x{i}={i*tabla}")
