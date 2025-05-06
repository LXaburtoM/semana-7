# Solicitar al usuario un número entero positivo
N = int(input("Introduce un número entero positivo: "))

# Verificar que el número sea positivo
if N > 0:
    suma = 0  # Inicializar el acumulador
    for i in range(1, N + 1):  # Iterar desde 1 hasta N (inclusive)
        suma += i  # Acumular la suma
    print(f"La suma de los números desde 1 hasta {N} es: {suma}")
else:
    print("Por favor, introduce un número entero positivo.")