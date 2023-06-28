#Generacion del numero aleatorio.
import random
intentos = 0
número = random.randint(1, 100)

#Introduccion al juego, pedir nombre y contar las reglas de este.
nombre = input("Introduce tu nombre: ")
print("¡hola, "+ nombre + "! Tienes 8 intentos para adivinar un numero (del 1 al 100) que estoy pensando. ¿puedes adivinarlo?")

while intentos < 8:
    es_el_numero = input('¡Ingresa ese número!: ')
    intentos = intentos + 1

#Resultados si el numero ingresado es incorrecto, si este es menor o mayor, si no se introduce un numero y el descuento de intentos, excepto para le ultimo caso.
    if es_el_numero.isdigit() == False:
        print ("¡hey! ¡Debes ingresar un número!")
        intentos = intentos - 1
        continue
    es_el_numero = int(es_el_numero)
    if es_el_numero < número:
            print("incorrecto, estoy pensando en un número mas alto, te quedan " + str(8-intentos) + " intentos.")
    if es_el_numero > número:
            print("nope, estoy pensando en un número mas bajo, te quedan " + str(8-intentos) + " intentos.")
    if es_el_numero == número:
            break
    
#Resultado final, fallando o acertando el numero que hay que adivinar.
if es_el_numero == número:
    intentos = str(intentos)
    print("¡Ya está, " + nombre + "! ¡adivinaste mi número! ¡Y solo te tomó " + intentos + " intentos!")
if es_el_numero != número:
    número = str(número)
    print("has perdido, " + nombre + ", no lograste adivinar el número... este era " + número + " ¡suerte para la proxima!")