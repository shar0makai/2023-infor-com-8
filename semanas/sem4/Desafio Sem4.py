#import para el presupuesto del inmueble
from datetime import date

#Lista de inmuebles
inmobiliario = [{'año': 2010, 'metros': 150, 'habitaciones': 4, 'garaje': True, 'zona': 'C', 'estado': 'Disponible'},\
                {'año': 2016, 'metros': 80, 'habitaciones': 2, 'garaje': False, 'zona': 'B', 'estado': 'Reservado'},\
                {'año': 2000, 'metros': 180, 'habitaciones': 4, 'garaje': True, 'zona': 'A', 'estado': 'Disponible'},\
                {'año': 2015, 'metros': 95, 'habitaciones': 3, 'garaje': True, 'zona': 'B', 'estado': 'Vendido'},\
                {'año': 2008, 'metros': 60, 'habitaciones': 2, 'garaje': False, 'zona': 'C', 'estado': 'Disponible'}]

#reglas de validacion
def validacion(inmueble):
    if inmueble['año'] < 2000:
        return False
    if inmueble['metros'] < 60:
        return False
    if inmueble['habitaciones'] < 2:
        return False
    if inmueble['zona'] != 'A' and inmueble['zona'] != 'B' and inmueble['zona'] != 'C':
        return False
    if inmueble['estado'] != 'Disponible' and inmueble['estado'] != 'Reservado' and inmueble['estado'] != 'Vendido':
        return False
    return True

#menu de interracion
print(f"Este es el menú para la gestión de inmuebles; estas son las opciones disponibles: ""\n1. Agregar inmueble"\
    "\n2. Editar inmueble""\n3. Eliminar inmueble""\n4. Cambiar estado del inmueble"\
    "\n5. Buscar inmuebles según su presupuesto""\n6. ver las reglas de validacion")
opcion = int(input("Ingrese el número para la acción que deseé realizar: "))
while opcion < 1 or opcion > 6:
    print("La opción no existente")
    opcion = int(input("Ingrese el número para la acción que deseé realizar: "))

#Visualizacion de los inmuebles
def inmuebles_totales():
    print("Los inmuebles existentes son: ")
    for inmueble in inmobiliario:
        print(inmueble)

# Agregar un inmueble
if opcion == 1:
    inmueble = {'año': int(input("Ingrese el año de inauguracion: ")),
                'metros': int(input("Ingrese los metros cuadrados: ")),
                'habitaciones': int(input("Ingrese la cantidad de habitaciones: ")),
                'garaje': bool(input("Ingrese si poseé garaje (True/False): ")),
                'zona': input("Ingrese la zona de ubicación (A/B/C): ").capitalize(),
                'estado': input("Ingrese el estado (Disponible/Reservado/Vendido): ").capitalize()}
    if validacion(inmueble):
        inmobiliario.append(inmueble)
        print(f"El inmueble fue agregado correctamente: {inmobiliario}")
    else:
        print("El inmueble no puede ser agregado al no cumplir con las reglas de validacón")

# Editar un inmueble
elif opcion == 2:
    inmuebles_totales()
    inmueble = int(input("Ingrese el número del inmueble a editar, a partir del valor 0: "))
    if inmueble in range(0, len(inmobiliario)):
        modif_valor = input(f"¿Qué desea modificar del inmueble {inmueble}? (año/metros/habitaciones/garaje/zona/estado): ").lower()
        if modif_valor == 'año' or modif_valor == 'metros' or modif_valor == 'habitaciones':
            n_valor_numerico = int(input(f"Ingrese el nuevo valor de {modif_valor}: "))
            if validacion(n_valor_numerico):
                inmobiliario[inmueble][modif_valor] = n_valor_numerico
            else:
                print("No se puede aceptar esta modificacion al no cumplir con las reglas de validacón")
        else:
            n_valor_alfabetico = input(f"Ingrese el nuevo valor de {modif_valor}: ").capitalize()
            if validacion(n_valor_alfabetico):
                inmobiliario[inmueble][modif_valor] = n_valor_alfabetico
            else:
                print("El inmueble no cumple con las reglas de validación")
    else:
        print("El inmueble no existe")
        
## Eliminar inmueble
elif opcion == 3:
    inmuebles_totales()
    inmueble = int(input("Ingrese el número del inmueble que desea eliminar, a partir del valor 0: "))
    if inmueble in range(0, len(inmobiliario)):
        inmobiliario.pop(inmueble)
        print(f"El inmueble se eliminó correctamente, la lista actual del imobiliario es la siguiente: {inmobiliario}")
    else:
        print("El inmueble no existe")

# Cambiar estado del inmueble
elif opcion == 4:
    inmuebles_totales()
    inmueble = int(input("Ingrese el número del inmueble que desea cambiar de estado, a partir del valor 0: "))
    if inmueble in range(0, len(inmobiliario)):
        estado = input("Ingrese el nuevo estado del inmueble (Disponible/Reservado/Vendido): ").capitalize()
        if estado != 'Disponible' and estado != 'Reservado' and estado != 'Vendido':
            print("El estado ingresado no es válido")
        else:
            inmobiliario[inmueble]['estado'] = estado
            print(f"El estado del inmueble se cambió correctamente, la lista actual del imobiliario es la siguiente:: {inmobiliario}")
    else:
        print("El inmueble no existe")
   
# Busqueda de inmuebles en base a un presupuesto dado
elif opcion == 5:
    presupuesto = float(input(f" ingrese el presupuesto disponible del cliente, se le mostrará cual inmueble es/son acorde/s a este: "))

    def precios_inmuebles(inmobiliario, presupuesto):
        year = date.today().year
        esta_disp = []
        for inmueble in inmobiliario:
            if inmueble['estado'] == 'Disponible' or inmueble['estado'] == 'Reservado':
                if inmueble['zona'] == 'A':
                    precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1-(year - inmueble['año'])/100)
                elif inmueble['zona'] == 'B':
                    precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1-(year - inmueble['año'])/100) * 1.5
                elif inmueble['zona'] == 'C':
                    precio = (inmueble['metros'] * 100 + inmueble['habitaciones'] * 500 + inmueble['garaje'] * 1500) * (1-(year - inmueble['año'])/100) * 2
                if precio <= presupuesto:
                    esta_disp.append((inmueble, precio))
        return esta_disp
    esta_disp = precios_inmuebles(inmobiliario, presupuesto)
    if len(esta_disp) == 0:
        print("No hay inmuebles disponibles para el presupuesto ingresado")
    else:
        print("Los inmuebles disponibles para el presupuesto ingresado son: ")
        for inmueble in esta_disp:
            print(f"{inmueble[0]} Con un valor de ${inmueble[1]}")

# reglas de validacion del inmueble:
elif opcion == 6:
    print("Zona de inmuebles: A, B o C.")
    print("Estados del inmueble: Disponible, Reservado o Vendido")
    print("Posteriores al año 2000")
    print("Mas de 60 metros cuadrados")
    print("Mas de 2 habitaciones")

print(f"Hasta pronto.")