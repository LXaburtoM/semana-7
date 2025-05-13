# Solicitar al usuario una frase
frase = input("Introduce una frase: ")

# Inicializar el contador de palabras
contador_palabras = 0

# Dividir la frase en palabras usando el método split()
palabras = frase.split()

# Contar las palabras usando un bucle for
for palabra in palabras:
    contador_palabras += 1  # Incrementar el contador por cada palabra

# Mostrar el resultado
print(f"La frase contiene {contador_palabras} palabras.")
