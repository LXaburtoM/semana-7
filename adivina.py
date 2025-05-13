import datetime
import random
import time as T


fecha=datetime.datetime.today()
print(f"Bienvenido \n{fecha}")
def adivinar(num_user, num_random):
    if num_user == num_random:
        t.sleep(3)
        print("¡Felicidades! Adivinaste el número.")
    else:
        print("Lo siento, no es el numero.")
        
def main():
    numero_r = random.randint(1, 10)  
    resp = "s"
    while resp.lower() == "s":
        num= input("Adivina el número entre 1 y 10: ")
        adivinar(int(num), numero_r)
        resp = input("¿Quieres jugar de nuevo? (s/n/r): ")
        if resp.lower() == "r":
            numero_r = random.randint(1, 10)  
            print("Número aleatorio reiniciado.")
       
main()