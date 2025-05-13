# Programa para encontrar el mayor y el menor de N números

# Solicitar al usuario la cantidad de números
N = int(input("¿Cuántos números deseas ingresar? "))

# Inicializar las variables para el mayor y el menor
mayor = None
menor = None

# Solicitar los números y encontrar el mayor y el menor
for i in range(N):
    numero = float(input(f"Ingrese el número {i + 1}: "))
    
    # Inicializar mayor y menor en la primera iteración
    if mayor is None or menor is None:
        mayor = numero
        menor = numero
    else:
        # Actualizar mayor y menor según corresponda
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero

# Mostrar los resultados
print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
