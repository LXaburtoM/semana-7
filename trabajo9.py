# Programa para calcular la frecuencia de cada dígito en un número

# Solicitar al usuario un número entero
numero = input("Introduce un número entero: ")

# Inicializar un diccionario para contar la frecuencia de los dígitos
frecuencia = {str(digito): 0 for digito in range(10)}

# Contar la frecuencia de cada dígito
for digito in numero:
    if digito.isdigit():  # Verificar que el carácter sea un dígito
        frecuencia[digito] += 1

# Mostrar los resultados
print("Frecuencia de cada dígito:")
for digito, cuenta in frecuencia.items():
    print(f"Dígito {digito}: {cuenta} veces")
