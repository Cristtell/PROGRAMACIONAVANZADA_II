#Crear un ejerccio que calcule la edad de una persona 
import os
os.system('cls' if os.name == 'int' else 'clear')

Nacimiento=int (input("Ingrese su año de nacimiento"))
actual=2025

edad=actual-Nacimiento
print("La edad de la persona es:", edad)

if edad>=21:
    print("Es mayor de edad ",edad)
elif edad >= 18:
    print("Solo es ciudadano ", edad)
else:
    print("Es menor de edad ",edad)

