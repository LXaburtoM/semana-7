# Solicitar al usuario un número entero positivo
numero = int(input("Introduce un número entero positivo: "))

# Inicializar el acumulador para el producto
factorial = 1

# Verificar que el número sea positivo
if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    # Calcular el factorial usando un bucle while
    contador = 1
    while contador <= numero:
        factorial *= contador  # Acumular el producto
        contador += 1  # Incrementar el contador

    # Mostrar el resultado
    print(f"El factorial de {numero} es {factorial}.")
    
