#Condicionales en python
a=int (input("Ingrese un numero:"))

if a%2==0:
    if a==0:
        print("El numero 0 no se clasifica como par o impar")
    else:
        print(f"{a} es Par")
else:
    print (f"{a} es impar")
