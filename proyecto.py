#crear un juego de adivinar el numero en el que el usuario tiene 5 intentos para adivinar un numero entre 1 y 20
import random
numero_secreto = random.randint(1, 20)
intentos = 5
print("Bienvenido al juego de adivinar el numero!")
print("Tengo un numero entre 1 y 20.")          
for intento in range(1, intentos + 1):
    adivinanza = int(input(f"Intento {intento} de {intentos}. ¿Cual es tu adivinanza? "))
    if adivinanza < numero_secreto:
        print("Tu adivinanza esta abajo del numero.")
    elif adivinanza > numero_secreto:
        print("Tu adivinanza esta arrriba del numero")
    else:
        print(f"¡Felicidades! Has adivinado el numero {numero_secreto} en {intento} intentos.")
        break