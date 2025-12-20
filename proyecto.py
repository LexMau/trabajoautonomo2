#crear un juego de adivinar el numero en el que el usuario tiene 5 intentos para adivinar un numero entre 1 y 20, este juego debera contener estructuras de datos como listas o diccionarios y funciones como definir el numero secreto y verificar la adivinanza del usuario.
import random

def definir_numero_secreto():
    return random.randint(1, 20)

def verificar_adivinanza(adivinanza, numero_secreto):
    if adivinanza < numero_secreto:
        return "abajo"
    elif adivinanza > numero_secreto:
        return "arriba"
    else:
        return "correcto"

numero_secreto = definir_numero_secreto()
intentos = 5
print("Bienvenido al juego de adivinar el numero!")
print("Tengo un numero entre 1 y 20.")          
for intento in range(1, intentos + 1):
    adivinanza = int(input(f"Intento {intento} de {intentos}. ¿Cual es tu adivinanza? "))
    resultado = verificar_adivinanza(adivinanza, numero_secreto)
    if resultado == "abajo":
        print("Tu adivinanza esta abajo del numero.")
    elif resultado == "arriba":
        print("Tu adivinanza esta arriba del numero")
    else:
        print(f"¡Felicidades! Has adivinado el numero {numero_secreto} en {intento} intentos.")
        break