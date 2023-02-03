################### PROYECTO FINAL IITA: RAYUELA DINÁMICA ###################
# Alumno: Valentín Imperio.
# Profesor: Renzo Acuña Diaz.
# Fecha: 18/10/2022.

#################### LIBRERÍAS ####################
# Para comenzar se llaman a las librerías y paquetes a utilizar a lo largo del proyecto final.

from ast import If
import keyboard
import time
import random

############## IMPRESIÓN DE LA RAYUELA ##############
# La rayuela o su "tablero" tendrá 12 filas que se generarán de forma completamente 
# ALEATORIA para que así los jugadores puedan jugar varias veces sin acostumbrarse al tablero.

# PARTE A) - Definición de las filas
# A continuación se definen las 12 filas y las inscripciones "Cielo" y "Tierra".

cielo = "  ☁️ CIELO 😇 "

fila12 = [[" ┏-----┳-----┓ ",
           " |  12 |  12 | ",
           " ┗--┏--┻--┓--┛ "], [" ┏-----┳-----┓ ",
           " |  12 |  12 | ",
           " ┣-----╋-----┫ "], ["    ┏-----┓ ",
           "    |  12 |  ",
           "    ┣-----┫ "],  ["    ┏-----┓ ",
           "    |  12 |  ",
           " ┏--┗--┳--┛--┓ "]] 


fila11 = [["  ",
        " |  11 |  11 | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  11 |  11 | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  11 |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  11 |  ",
        " ┏--┗--┳--┛--┓ "]]


fila10 = [["  ",
        " |  10 |  10 | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  10 |  10 | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  10 |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  10 |  ",
        " ┏--┗--┳--┛--┓ "]]


fila9= [["  ",
        " |  9  |  9  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  9  |  9  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  9  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  9  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila8= [["  ",
        " |  8  |  8  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  8  |  8  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  8  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  8  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila7= [["  ",
        " |  7  |  7  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  7  |  7  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  7  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  7  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila6= [["  ",
        " |  6  |  6  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  6  |  6  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  6  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  6  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila5 = [["  ",
        " |  5  |  5  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  5  |  5  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  5  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  5  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila4 = [["  ",
        " |  4  |  4  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  4  |  4  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  4  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  4  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila3 = [["  ",
        " |  3  |  3  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  3  |  3  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  3  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  3  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila2 = [["  ",
        " |  2  |  2  | ",
        " ┗--┏--┻--┓--┛ "], ["  ",
        " |  2  |  2  | ",
        " ┣-----╋-----┫ "], ["  ",
        "    |  2  |  ",
        "    ┣-----┫ "],  ["  ",
        "    |  2  |  ",
        " ┏--┗--┳--┛--┓ "]]


fila1 = [["  ",
        " |  1  |  1  | ",
        " ┗-----┻-----┛ "],["  ",
        " |  1  |  1  | ",
        " ┗-----┻-----┛ "],["  ",
        "    |  1  |  ",
        "    ┗-----┛ "],["  ",
        "    |  1  |  ",
        "    ┗-----┛ "]]

tierra = "  🌱 TIERRA 🌎 "

# PARTE B) - Generación de las casillas aleatoriamente
# Una vez definidas las filas, mediante la creación de dos funciones "random_simulation()" y 
# "rayuela_cuerpo()" se procede a generar los números aleatorios de forma encadenada para las 12 filas.
# Se necesitan que los números estén encadenados para poder recordar la elección anterior, es decir si 
# la fila anterior fue una casilla simple o doble. Pudiendo recordar la elección se logra 
# armar la rayuela aleatoria coherentemente ensamblada.
# Agradecimiento especial a: Andrew Ryan de la comunidad de StackOverFlow por la prestación de su ayuda
# para el armado de estas dos funciones.

def random_simulation(entry_number): # Genera un número aleatorio basado en un input dado a la función.
    if entry_number == 0 or entry_number == 1:
        return random.choice([1,3]) # Devuelve el valor hacia dónde es llamada la función.
    elif entry_number == 2 or entry_number == 3:
        return random.choice([0,2]) # Devuelve el valor hacia dónde es llamada la función.

def rayuela_cuerpo():
    origin_number = 0 
    posiciones_casillas = []
    for _ in range(12): # Recorre la función 12 veces y actualiza el valor para la próxima vez que es corrida la función.
        posiciones_casillas += [origin_number]
        origin_number = random_simulation(origin_number)
    return posiciones_casillas # Devuelve las 12 casillas aleatorias generadas guardadas en una lista.


# PARTE C) - Impresión de la rayuela

def imprimir_rayuela():
    posiciones_casillas = rayuela_cuerpo()
    print(cielo)
    print(*fila12[posiciones_casillas[11]],sep = "\n", end = "" )
    print(*fila11[posiciones_casillas[10]],sep = "\n", end = "" )
    print(*fila10[posiciones_casillas[9]],sep = "\n", end = "" )
    print(*fila9[posiciones_casillas[8]],sep = "\n", end = "" )
    print(*fila8[posiciones_casillas[7]],sep = "\n", end = "" )
    print(*fila7[posiciones_casillas[6]],sep = "\n", end = "" )
    print(*fila6[posiciones_casillas[5]],sep = "\n", end = "" )
    print(*fila5[posiciones_casillas[4]],sep = "\n", end = "" )
    print(*fila4[posiciones_casillas[3]],sep = "\n", end = "" )
    print(*fila3[posiciones_casillas[2]],sep = "\n", end = "" )
    print(*fila2[posiciones_casillas[1]],sep = "\n", end = "" )
    print(*fila1[posiciones_casillas[0]],sep = "\n")
    print(tierra)
    return posiciones_casillas

# Para imprimir el tablero solo se debe llamar a la función de la siguiente forma: 
#imprimir_rayuela()

############### LANZAMIENTO DE LA PIEDRA ###############
# Se crea la función para lanzar la roca.

def lanzamiento(Turno,posicion1,posicion2,jugador1,jugador2,posiciones_casillas):

    while posicion1 != 12 or posicion2 != 12:
        if Turno == 1:
            print("Comienza el Turno de ", jugador1,"!" )
            print("Debes presionar Space/Barra cuando veas el número de casillas que quieres saltar")
            print("Manten presionadas la tecla al menos un segundo.")
            print("Pero se preciso, los números avanzarán rápido y no están ordenados!")
            time.sleep(12)
            rayuela_final(posiciones_casillas)
            print("turno de ",jugador1)
            print("Recuerde que está en la casilla",posicion1)
            time.sleep(2)
            print("Listo? Empiece a lanzar!")

            while Turno==1:
                lanzamiento=random.randint(1,14-posicion1)
                print(lanzamiento)
                time.sleep(0.5)
                try:  
                    if keyboard.is_pressed('space'):
                        print("Has tirado tu piedrita",lanzamiento,"posiciones.")
                        if lanzamiento > 12-posicion1: # El jugador 1 falla el tiro. Pierde el turno.
                            print("Has fallado el tiro y ha caido fuera de la rayuela.")
                            print("Pierdes tu turno.")
                            Turno = 0
                            
                        else: # El jugador 1 acierta el tiro. Sigue su turno.
                            print("Tienes que saltar hasta la casilla",posicion1+lanzamiento)
                            print("Empiezan los saltos!")
                            print("Debes tocar la tecla W para saltar a casillas individuales y las teclas A + D  para saltar a casillas dobles")
                            print("Manten presionadas las teclas al menos un segundo.")
                            print("Pero no seas muy lento o vas a tropezar y perder el turno!")
                            time.sleep(12)
                            print("Preparado? Empiece a Saltar!")

                            
                            while Turno == 1 and lanzamiento != 0:
                               
                                if posiciones_casillas[posicion1] == 0 or posiciones_casillas[posicion1] == 1:

                                    time.sleep(1)
                                    print(" A + D ")
                                    end_time = time.time() + 10
                                    try:  
                                        if keyboard.read_key()=='a' and keyboard.read_key()=='d' and time.time() <= end_time:
                                            posicion1 +=1
                                            if posicion1==12:
                                                print("Has llegado al  ☁️ CIELO 😇 !!")
                                                print ("You are winner",jugador1,"!!!")
                                                exit()
                                            else:
                                                lanzamiento -=1
                                                print("✔")
                                                print("Estas en la casilla ", posicion1,"te faltan ", lanzamiento)
                                        else:
                                            print ("Te tropiezas y pierdes el turno :(")
                                            lanzamiento = 0
                                            Turno = 0

                                    except: 
                                        exit()

                                            
                                elif posiciones_casillas[posicion1] == 2 or posiciones_casillas[posicion1] == 3:
                                    
                                    time.sleep(1)
                                    print(" W ")
                                    end_time = time.time() + 10
                                    try:  
                                        if keyboard.read_key()=='w' and time.time() <= end_time:
                                            posicion1 +=1
                                            if posicion1==12:
                                                print("Has llegado al  ☁️ CIELO 😇 !!")
                                                print ("You are winner",jugador1,"!!!")
                                                exit()
                                            else:
                                                lanzamiento -=1
                                                print("✔")
                                                print("Estas en la casilla ", posicion1,"te faltan ", lanzamiento)
                                        else:
                                            print ("Te tropiezas y pierdes el turno :(")
                                            lanzamiento = 0  
                                            Turno = 0
                                    except: 
                                        exit()
                                                            
                except:
                    exit()

        if Turno == 0:
            print("Comienza el Turno de ", jugador2,"!" )
            print("Debes presionar Space/Barra cuando veas el número de casillas que quieres saltar")
            print("Manten presionadas la tecla al menos un segundo.")
            print("Pero se preciso, los números avanzarán rápido y no están ordenados!")
            time.sleep(12)
            rayuela_final(posiciones_casillas)
            print("turno de ",jugador2)
            print("Recuerde que está en la casilla",posicion2)
            time.sleep(2)
            print("Listo? Empiece a lanzar!")


            while Turno==0:
                lanzamiento=random.randint(1,14-posicion2)
                print(lanzamiento)
                time.sleep(0.5)
                try:  
                    if keyboard.is_pressed('space'):
                        print("Has tirado tu piedrita",lanzamiento,"posiciones.")
                        if lanzamiento > 12-posicion2: # El jugador 2 falla el tiro. Pierde el turno.
                            print("Has fallado el tiro y ha caido fuera de la rayuela.")
                            print("Pierdes tu turno.")
                            Turno = 1
                            
                        else: # El jugador 2 acierta el tiro. Sigue su turno.
                            print("Tienes que saltar hasta la casilla",posicion2+lanzamiento)
                            print("Empiezan los saltos!")
                            print("Debes tocar la tecla W para saltar a casillas individuales y las teclas A + D  para saltar a casillas dobles")
                            print("Manten presionadas las teclas al menos un segundo.")
                            print("Pero no seas muy lento o vas a tropezar y perder el turno!")
                            time.sleep(12)
                            print("Preparado? Empiece a Saltar!")
                            
                            while Turno == 0 and lanzamiento != 0:
                               
                                if posiciones_casillas[posicion2] == 0 or posiciones_casillas[posicion2] == 1:

                                    time.sleep(1)
                                    print(" A + D ")
                                    end_time = time.time() + 10
                                    try:  
                                        if keyboard.read_key()=='a' and keyboard.read_key()=='d' and time.time() <= end_time:
                                            posicion2 +=1
                                            if posicion2==12:
                                                print("Has llegado al  ☁️ CIELO 😇 !!")
                                                print ("You are winner",jugador2,"!!!")
                                                exit()
                                            else:
                                                lanzamiento -=1
                                                print("✔")
                                                print("Estas en la casilla ", posicion2,"te faltan ", lanzamiento)
                                        else:
                                            print ("Te tropiezas y pierdes el turno :(")
                                            lanzamiento = 0
                                            Turno = 1

                                    except: 
                                        exit()

                                            
                                elif posiciones_casillas[posicion2] == 2 or posiciones_casillas[posicion2] == 3:

                                    time.sleep(1)
                                    print(" W ")
                                    end_time = time.time() + 10
                                    try:  
                                        if keyboard.read_key()=='w' and time.time() <= end_time:
                                            posicion2 +=1
                                            if posicion2==12:
                                                print("Has llegado al  ☁️ CIELO 😇 !!")
                                                print ("You are winner",jugador2,"!!!")
                                                exit()
                                            else:
                                                lanzamiento -=1
                                                print("✔")
                                                print("Estas en la casilla ", posicion2,"te faltan ", lanzamiento)
                                        else:
                                            print ("Te tropiezas y pierdes el turno :(")
                                            lanzamiento = 0  
                                            Turno = 1

                                    except: 
                                        exit() 

                except:
                    exit()
                

######## INGRESO Y SELECCIÓN DE JUGADORES ########
#Se lo muestra a los jugadores junto a la Bienvenida y se les pide que ingresen sus nombre.
print("Bienvenido a la Rayuela Dinámica v1.0, lo último en desarrollo de juegos de Python!!")
print("Para comenzar la experiencia ambos jugadores deben ingresar sus nombres.")
nombre1 = input("Por favor ingrese el nombre del primer jugador: ")
nombre2 = input("Por favor ingrese el nombre del segundo jugador: ")

# Se selecciona al jugador que empezará primero, aleatoriamente.
if random.choice([1,2]) == 1:
    jugador1 = nombre1
    jugador2 = nombre2
else:
    jugador1 = nombre2
    jugador2 = nombre1


# Se crea el tablero de la rayuela
posiciones_casillas = imprimir_rayuela()
# Se fija el tablero de la rayuela obtenida para utilizar siempre el mismo a lo largo del juego.
def rayuela_final(posiciones_casillas):
    print(cielo)
    print(*fila12[posiciones_casillas[11]],sep = "\n", end = "" )
    print(*fila11[posiciones_casillas[10]],sep = "\n", end = "" )
    print(*fila10[posiciones_casillas[9]],sep = "\n", end = "" )
    print(*fila9[posiciones_casillas[8]],sep = "\n", end = "" )
    print(*fila8[posiciones_casillas[7]],sep = "\n", end = "" )
    print(*fila7[posiciones_casillas[6]],sep = "\n", end = "" )
    print(*fila6[posiciones_casillas[5]],sep = "\n", end = "" )
    print(*fila5[posiciones_casillas[4]],sep = "\n", end = "" )
    print(*fila4[posiciones_casillas[3]],sep = "\n", end = "" )
    print(*fila3[posiciones_casillas[2]],sep = "\n", end = "" )
    print(*fila2[posiciones_casillas[1]],sep = "\n", end = "" )
    print(*fila1[posiciones_casillas[0]],sep = "\n")
    print(tierra)

############ INICIALIZACIÓN DE VARIABLES ############
# Se ingresan todas las variables que sean necesarias.
lanzamiento(1,0,0,jugador1,jugador2,posiciones_casillas)
############ EMPIEZA EL JUEGO! ############



