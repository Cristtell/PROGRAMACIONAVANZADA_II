#Ejercicio 8: Ingresar un numero y mostrar la tabla de multiplicar del 1 hasta el 10

num=int(input("Ingrese un numero para crear su tabla de multiplicar: "))

for i in range (1,11):
    print(f"{num}X {i}={i*num}")