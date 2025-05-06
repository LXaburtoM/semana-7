# Solicitar al usuario un número entero positivo
M = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if M > 0:
    producto = 1  # Inicializar el acumulador para el producto
    contador = 0  # Contador de números pares encontrados
    numero = 2  # Primer número par

    while contador < M:  # Repetir hasta encontrar M números pares
        producto *= numero  # Multiplicar el acumulador por el número par actual
        contador += 1  # Incrementar el contador de números pares
        numero += 2  # Pasar al siguiente número par

    print(f"El producto de los primeros {M} números pares es: {producto}")
else:
    print("Por favor, introduce un número entero positivo.")
    