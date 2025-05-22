#Crear un programa que muestre el total de una compra de un solo producto calculado el impuesto sobre venta y dar un descuento 
# solamente cuando el total de la cuenta sea mayor a 10,000.00 el descuento sera del 25%

print("Variedades Criss")
cantidad=int (input("Ingrese la cantidad"))
precio=int (input("Ingrese el precio del producto"))

total=cantidad*precio+0.15
descuento=total-0.25

if total<=10000:
    total==total
    print(f"{total } Su total es: ")
else:
    print(f"{descuento}Su total con descuento es:")