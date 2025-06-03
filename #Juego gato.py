#Juego gato


tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def mostrar_tablero():
    print("   0   1   2")
    for i, fila in enumerate(tablero):
        print(f"{i}  "+" | ".join(fila))
        if i < 2:
            print("  ---+---+---")
            
        
def comprobar_ganador(jugador):
    # Comprobacion de Filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    # Comprobacion de Columnas    
    for col in range(3):
        if tablero[0][col] == jugador and tablero[1][col] == jugador and tablero[2][col] == jugador:
            return True
    #Comprobacion de diagonales
    if (tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2]) or (tablero[0][2] == jugador and tablero[1][1]== jugador and tablero[2][0] == jugador):
        return True
    return False

jugador_actual = "X"
turnos = 0

while True:
    mostrar_tablero()
    print(f"Turno del jugador {jugador_actual}")
    
    fila = int(input("Ingresa la fila (0,1,2)"))
    col = int(input("Ingresa la columna (0,1,2)"))
    
    if tablero[fila][col]== " ":
        tablero[fila][col]=jugador_actual
    else:
       print("La casilla está ocupada")
       continue
    turnos += 1
    if (comprobar_ganador(jugador_actual)):      #Eliminé el "NOT"
        mostrar_tablero()
        print(f"El jugador {jugador_actual} ha GANADO!!!!")
        break
    
    if turnos == 9:
        print("Empate")
        break
        
    if jugador_actual == "X":
        jugador_actual = "O"
    else:
        jugador_actual = "X"