# Programa para sumar números pares e impares

print("Introduce números enteros (ingresa 0 para finalizar):")

suma_pares = 0
suma_impares = 0

while True:
    try:
        numero = int(input("Número: "))
    except ValueError:
        print("Por favor ingresa un número entero válido.")
        continue

    if numero == 0:
        break  # Fin de la entrada

    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

# Resultado
print(f"Suma de números pares: {suma_pares}")
print(f"Suma de números impares: {suma_impares}")

