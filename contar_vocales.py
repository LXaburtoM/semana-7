# Solicitar al usuario una cadena
cadena = input("Introduce una cadena de texto: ").lower()  # Convertir a minúsculas para simplificar la comparación

# Inicializar contadores para cada vocal
contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0

# Recorrer la cadena y contar las vocales
for caracter in cadena:
    if caracter == 'a':
        contador_a += 1
    elif caracter == 'e':
        contador_e += 1
    elif caracter == 'i':
        contador_i += 1
    elif caracter == 'o':
        contador_o += 1
    elif caracter == 'u':
        contador_u += 1

# Mostrar los resultados
print(f"Cantidad de 'a': {contador_a}")
print(f"Cantidad de 'e': {contador_e}")
print(f"Cantidad de 'i': {contador_i}")
print(f"Cantidad de 'o': {contador_o}")
print(f"Cantidad de 'u': {contador_u}")