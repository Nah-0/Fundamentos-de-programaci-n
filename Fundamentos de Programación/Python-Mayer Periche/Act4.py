
#Calculo de expresion 2
x=float(input("Ingresa el valor de x: "))
y=float(input("Ingresa el valor de y: "))
c=float(input("Ingresa el valor de c: "))

# Calcular el numerador: 5 * x^3 * y^2
numerador = 5 * (x ** 3) * (y ** 2)

# Calcular el radicando: raíz cuarta de (2 * c^3)
radicando = 2 * (c ** 3)

# Verificar que el radicando no sea negativo (para raíces pares)

if radicando < 0:
    print("Error: No se puede calcular la raíz cuarta de un número negativo en los reales.")
else:
    denominador = radicando ** (1 / 4)

    # Calcular el resultado final
    resultado = numerador / denominador

    # Mostrar resultados
    print(f"\nPaso 1 - Numerador: 5 * ({x}^3) * ({y}{2}) = {numerador}")
    print(f"Paso 2 - Denominador: raíz cuarta de (2 * {c}^3) = {denominador}")
    print(f"\nResultado final: {numerador} / {denominador} = {resultado}")