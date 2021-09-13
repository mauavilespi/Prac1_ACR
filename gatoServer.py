import socket
import time
import random

HOST = "127.0.0.1"  # Localhost
PORT = 65432
buffer_size = 1024


# Funciones utilizadas
# Tablero 3x3
tab_1 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def createtable_principiante():
    row1 = ' ' + str(tab_1[0]) + ' | ' + str(tab_1[1]) + ' | ' + str(tab_1[2])
    row2 = ' ' + str(tab_1[3]) + ' | ' + str(tab_1[4]) + ' | ' + str(tab_1[5])
    row3 = ' ' + str(tab_1[6]) + ' | ' + str(tab_1[7]) + ' | ' + str(tab_1[8])
    separator = '\n' + ('-' * 11) + '\n'
    return row1 + separator + row2 + separator + row3


# Tableto 5x5
tab_2 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',
         ' ', ' ', ' ', ' ', ' ', ]


def createtable_avanzado():
    row1 = ' ' + str(tab_2[0]) + ' | ' + str(tab_2[1]) + ' | ' + str(tab_2[2]) + ' | ' + str(tab_2[3]) + ' | ' + \
           str(tab_2[4])
    row2 = ' ' + str(tab_2[5]) + ' | ' + str(tab_2[6]) + ' | ' + str(tab_2[7]) + ' | ' + str(tab_2[8]) + ' | ' + \
           str(tab_2[9])
    row3 = ' ' + str(tab_2[10]) + ' | ' + str(tab_2[11]) + ' | ' + str(tab_2[12]) + ' | ' + str(tab_2[13]) + ' | ' + \
           str(tab_2[14])
    row4 = ' ' + str(tab_2[15]) + ' | ' + str(tab_2[16]) + ' | ' + str(tab_2[17]) + ' | ' + str(tab_2[18]) + ' | ' + \
           str(tab_2[19])
    row5 = ' ' + str(tab_2[20]) + ' | ' + str(tab_2[21]) + ' | ' + str(tab_2[22]) + ' | ' + str(tab_2[23]) + ' | ' + \
           str(tab_2[24])
    separator = '\n' + ('-' * 19) + '\n'
    return row1 + separator + row2 + separator + row3 + separator + row4 + separator + row5


def seleccion_tablero(selec):
    if selec == '1':
        tablero_sel = createtable_principiante()
    else:
        tablero_sel = createtable_avanzado()
    return tablero_sel


def estado_del_juego_principiante(tabla):
    # Lineas Horizontales
    if tabla[0] == tabla[1] == tabla[2] != ' ':
        estado_actual = "Ganador"
    elif tabla[3] == tabla[4] == tabla[5] != ' ':
        estado_actual = "Ganador"
    elif tabla[6] == tabla[7] == tabla[8] != ' ':
        estado_actual = "Ganador"

    # Lineas Verticales
    elif tabla[0] == tabla[3] == tabla[6] != ' ':
        estado_actual = "Ganador"
    elif tabla[1] == tabla[4] == tabla[7] != ' ':
        estado_actual = "Ganador"
    elif tabla[2] == tabla[5] == tabla[8] != ' ':
        estado_actual = "Ganador"

    # Lineas Diagonales
    elif tabla[0] == tabla[4] == tabla[8] != ' ':
        estado_actual = "Ganador"
    elif tabla[6] == tabla[4] == tabla[2] != ' ':
        estado_actual = "Ganador"
    else:
        estado_actual = "Jugando"

    return estado_actual


def estado_del_juego_avanzado(tabla2):
    # Lineas Horizontales
    if tabla2[0] == tabla2[1] == tabla2[2] == tabla2[3] == tabla2[4] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[5] == tabla2[6] == tabla2[7] == tabla2[8] == tabla2[9] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[10] == tabla2[11] == tabla2[12] == tabla2[13] == tabla2[14] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[15] == tabla2[16] == tabla2[17] == tabla2[18] == tabla2[19] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[20] == tabla2[21] == tabla2[22] == tabla2[23] == tabla2[24] != ' ':
        estado_actual2 = "Ganador"

    # Lineas Verticales
    elif tabla2[0] == tabla2[5] == tabla2[10] == tabla2[15] == tabla2[20] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[1] == tabla2[6] == tabla2[11] == tabla2[16] == tabla2[21] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[2] == tabla2[7] == tabla2[12] == tabla2[17] == tabla2[22] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[3] == tabla2[8] == tabla2[13] == tabla2[18] == tabla2[23] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[4] == tabla2[9] == tabla2[14] == tabla2[19] == tabla2[24] != ' ':
        estado_actual2 = "Ganador"

    # Lineas Diagonales
    elif tabla2[0] == tabla2[6] == tabla2[12] == tabla2[18] == tabla2[24] != ' ':
        estado_actual2 = "Ganador"
    elif tabla2[4] == tabla2[8] == tabla2[12] == tabla2[16] == tabla2[20] != ' ':
        estado_actual2 = "Ganador"
    else:
        estado_actual2 = "Jugando"

    return estado_actual2


# Constantes iniciales
jugador_actual = "X"
edo_actual = "Jugando"
edo_actual2 = "Jugando"
turno = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))  # Conexión primer socket
    TCPServerSocket.listen()  # El socket espera conexiones

    print("El servidor TCP para jugar Gato Dummy está disponible y en espera de solicitudes")

    client_conn, client_addr = TCPServerSocket.accept()  # El socket recibe una conexión y ha sido aceptada

    while True:
        print("Se ha conectado un jugador. Esperando dificultad... ")
        data = client_conn.recv(buffer_size)  # El servidor recibe la dificultad
        if not data:
            break
        dif = data.decode('UTF-8')
        print("El jugador ha seleccionado la dificultad ", dif)
        print("Enviando tablero a ", client_addr)
        tablero_enviado = seleccion_tablero(dif)
        client_conn.sendall(str.encode(tablero_enviado))

        # Iniciamos el reloj
        start = time.time()

        # Jugamos hasta que haya ganador
        # Principiante
        if dif == '1':
            while True:
                bandera = 0
                jugador_actual = 'X'
                print("Esperando tiro del jugador... ")
                tiro = client_conn.recv(buffer_size)
                tiroJugador = tiro.decode('UTF-8')
                if tiroJugador >= '0' or tiroJugador >= '8':
                    if tab_1[int(tiroJugador)] != " ":
                        client_conn.sendall(str.encode("La casilla " + tiroJugador + " ya está ocupada. Elija otra\n"))
                    else:
                        tab_1[int(tiroJugador)] = 'X'
                        turno = turno + 1
                        bandera = 1
                else:
                    client_conn.sendall(str.encode("Posición no válida"))

                if bandera == 1:
                    edo_actual = estado_del_juego_principiante(tab_1)

                    if turno >= 9:
                        client_conn.sendall(str.encode("EMPATE"))
                        break

                    if edo_actual == "Jugando":
                        if jugador_actual == "X":
                            # Tiro RANDOM
                            jugador_actual = "O"
                            tiroRandom = random.randrange(0, 9)
                            while tab_1[int(tiroRandom)] != " ":
                                tiroRandom = random.randrange(0, 9)
                            tab_1[int(tiroRandom)] = jugador_actual
                            turno = turno + 1
                            edo_actual = estado_del_juego_principiante(tab_1)
                            if edo_actual == "Ganador":
                                client_conn.sendall(str.encode("Ha ganado: " + jugador_actual))
                    else:
                        client_conn.sendall(str.encode("Ha ganado: " + jugador_actual))
                        end = time.time()
                        timeplay = str(end - start)
                        client_conn.sendall(str.encode("Tiempo de juego: " + timeplay + " segundos"))
                        break

                    new_tablero = seleccion_tablero(dif)
                    client_conn.sendall(str.encode(new_tablero))

        # Avanzado
        else:
            while True:
                bandera = 0
                jugador_actual = 'X'
                print("Esperando tiro del jugador... ")
                tiro = client_conn.recv(buffer_size)
                tiroJugador = tiro.decode('UTF-8')
                if tiroJugador >= '0' or tiroJugador >= '24':
                    if tab_2[int(tiroJugador)] != " ":
                        client_conn.sendall(str.encode("La casilla " + tiroJugador + " ya está ocupada. Elija otra\n"))
                    else:
                        tab_2[int(tiroJugador)] = 'X'
                        turno = turno + 1
                        bandera = 1
                else:
                    client_conn.sendall(str.encode("Posición no válida"))

                if bandera == 1:
                    edo_actual2 = estado_del_juego_avanzado(tab_2)

                    if turno >= 25:
                        client_conn.sendall(str.encode("EMPATE"))
                        break

                    if edo_actual2 == "Jugando":
                        if jugador_actual == "X":
                            # Tiro RANDOM
                            jugador_actual = "O"
                            tiroRandom = random.randrange(0, 25)
                            while tab_2[int(tiroRandom)] != " ":
                                tiroRandom = random.randrange(0, 25)
                            tab_2[int(tiroRandom)] = jugador_actual
                            turno = turno + 1
                            edo_actual2 = estado_del_juego_avanzado(tab_2)
                            if edo_actual2 == "Ganador":
                                client_conn.sendall(str.encode("Ha ganado: " + jugador_actual))
                    else:
                        client_conn.sendall(str.encode("Ha ganado: " + jugador_actual))
                        end = time.time()
                        timeplay = str(end-start)
                        client_conn.sendall(str.encode("Tiempo de juego: " + timeplay + " segundos"))
                        break

                    new_tablero2 = seleccion_tablero(dif)
                    client_conn.sendall(str.encode(new_tablero2))
