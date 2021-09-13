import socket

print("***** Bienvenido al Gato Dummy *****")
HOST = input("Introduzca la dirección IP: ")
PORT = int(input("Introduzca el puerto destino: "))

buffer_size = 1024


# Dificultad del juego
def seleccionar_dificultad():
    print("\nSeleccione dificultad del Gato Dummy:")
    print("1. Principiante: Tablero 3x3")
    print("2. Avanzado: Tablero 5x5")
    seleccion = input()
    return seleccion


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))  # Conexión con el servidor

    print("¡La conexión con el servidor se ha realizado correctamente!")

    # Selección de dificultad
    dificultad = seleccionar_dificultad()
    while dificultad != '1' and dificultad != '2':
        dificultad = seleccionar_dificultad()
    print("Enviando dificultad... ")
    TCPClientSocket.sendall(str.encode(dificultad))
    print("Esperando tablero... ")
    data = TCPClientSocket.recv(buffer_size)
    print(data.decode('UTF-8'))

    # Tiros
    edo = "Jugando"
    print(" Usted es el jugador X \n")
    if dificultad == '1':
        while edo == "Jugando":
            tiro = input("Elija la posición que quiere ocupar (0-8): ")
            TCPClientSocket.sendall(str.encode(tiro))
            data = TCPClientSocket.recv(buffer_size)
            dataDeco = data.decode('UTF-8')
            print(dataDeco)
            if dataDeco == "Ha ganado: X" or dataDeco == "Ha ganado: O" or dataDeco == "EMPATE":
                edo = "Ganar"
        time = TCPClientSocket.recv(buffer_size)
        print(time.decode('UTF-8'))

    else:
        while edo == "Jugando":
            tiro = input("Elija la posición que quiere ocupar (0-24): ")
            TCPClientSocket.sendall(str.encode(tiro))
            data = TCPClientSocket.recv(buffer_size)
            dataDeco = data.decode('UTF-8')
            print(dataDeco)
            if dataDeco == "Ha ganado: X" or dataDeco == "Ha ganado: O" or dataDeco == "EMPATE":
                edo = "Ganar"
        time = TCPClientSocket.recv(buffer_size)
        print(time.decode('UTF-8'))
