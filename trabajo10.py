# Simulación de cajero automático simplificado

saldo = 1000.0  # saldo inicial
num_depositos = 0
num_retiros = 0

print("Bienvenido al Cajero Automático Simplificado")
print(f"Tu saldo inicial es: ${saldo:.2f}")

while True:
    print("\nElige una opción:")
    print("1. Depositar")
    print("2. Retirar")
    print("3. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        try:
            cantidad = float(input("Cantidad a depositar: $"))
            if cantidad <= 0:
                print("Por favor ingresa una cantidad positiva.")
                continue
            saldo += cantidad
            num_depositos += 1
            print(f"Depósito realizado. Saldo actual: ${saldo:.2f}")
        except ValueError:
            print("Cantidad inválida. Intenta de nuevo.")
    
    elif opcion == "2":
        try:
            cantidad = float(input("Cantidad a retirar: $"))
            if cantidad <= 0:
                print("Por favor ingresa una cantidad positiva.")
                continue
            if cantidad > saldo:
                print("Saldo insuficiente para realizar el retiro.")
            else:
                saldo -= cantidad
                num_retiros += 1
                print(f"Retiro realizado. Saldo actual: ${saldo:.2f}")
        except ValueError:
            print("Cantidad inválida. Intenta de nuevo.")
    
    elif opcion == "3":
        print("Gracias por usar el cajero automático.")
        print(f"Total depósitos realizados: {num_depositos}")
        print(f"Total retiros realizados: {num_retiros}")
        print(f"Saldo final: ${saldo:.2f}")
        break
    
    else:
        print("Opción no válida. Por favor elige 1, 2 o 3.")
