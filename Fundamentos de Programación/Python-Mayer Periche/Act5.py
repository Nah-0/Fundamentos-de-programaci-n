#Ingreso de nombre
print("Ingrese su nombre y edad")
nombre=input("Nombre: ")
edad=int(input("Edad: "))
print(nombre +" tiene "+str(edad)+" años.\n")

#Ingreso de 2 numeros enteros
print("Por favor, escriba 2 numeros enteros")
a=float(input("Ingrese el primer número: "))
b=float(input("Ingrese el segudo número: "))
print("Resultado= ",a+b, "\n" )

#Ingreso del nombre de un producto, su precio, cuanto pagará y el calculo de su vuelto
print("Ingrese el nombre de un producto, su precio y con cuanto pagará")

producto=input("Nombre del producto: ")
precio=float(input("Precio del producto"))
dineropago=float(input("¿Cuánto dinero tienes para pagar?"))

print(f"\nProducto: {nombre} {dineropago-precio:.2f}")



