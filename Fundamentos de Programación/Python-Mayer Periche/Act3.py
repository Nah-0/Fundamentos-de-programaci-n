
#Calculo de expresion 1
a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
d=float(input("Ingrese el valor de d: "))

#Resultado del numerador
numerador = (a ** 3) * b
#Resultado del denominador
denominador = 2*a*(b**2)

import math

# Verificar si el número es negativo
if d < 0:
    print("No se puede calcular la raíz cuadrada de un número negativo en los números reales.")
if denominador == 0:
    print("Error: El denominador es cero. No se puede dividir.")
else:
    cociente= numerador/denominador
    raiz = math.sqrt(12*(d**4))
    resultado=cociente-raiz
    
print(f"\nPaso 1 - Fracción: ({a}^3 * {b}) / (2 * {a} * {b}^2) = {cociente}")
print(f"Paso 2 - Raíz cuadrada de (12 * {d}^4) = {raiz}")
print(f"\nResultado final de la expresión: {cociente} - {raiz} = {resultado}")
