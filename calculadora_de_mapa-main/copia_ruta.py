import random
import time
import os
from collections import deque

#Parte 1: Crear el mapa aleatorio con numeros
filas = int(input('Ingresa el tamaño de la fila:'))
columnas = int(input('Ingresa el tamaño de la columna:'))

def generar_mapa(filas, columnas):
    valores =[0]*60 + [1]*20 + [2]*15 [3]*5
    mapa = []
    for _ in range(filas):
        fila = [[random.choice(valores)] for _ in range(columnas)]
        mapa.append(fila)
    return mapa

mapa_numericos = generar_mapa(filas, columnas)

#Parte 2: traducir a mapa para BFS(' '= libre, '#' = muro)
def convertir_a_tablero(mapa_numerico):
    tablero = []
    for fila in mapa_numericos:
        nueva_fila = []
        for celda in fila:
            if celda == 0:
                nueva_fila.append(' ')
            elif celda == 1:
                nueva_fila.append('#')
            elif celda == 2:
                nueva_fila.append('~')
            elif celda == 3:
                nueva_fila.append('X')
        tablero.append(nueva_fila)
    return tablero

#Parte 3: colocar inicio 'S' y fin 'E' en posiciones aleatorias validas
def encontrar_posicion_libre(): #busca casillas vacias al azar
    while True:
        x = random.randint(0, filas -1)
        y = random.randint(0, columnas -1)
        if tablero[x][y] == ' ':
            return x, y
        
sx, sy = encontrar_posicion_libre() # son la coordenadas donde se va a poner 'S'
ex, ey = encontrar_posicion_libre() # coordenadas donde se va a poner la 'E'
while (ex, ey) == (sx, sy):
    ex, ey = encontrar_posicion_libre

tablero[sx][sy] = 'S'
tablero[ex][ey] = 'E'

#Parte 4: Función para imprimir el tablero con animación
def imprimir_tablero(tablero, visitado=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, fila in enumerate(tablero):
        for j, celda in enumerate(fila):
            if visitado and visitado[i][j] and tablero[i][j] not in ('S', 'E'):
                print('⭐', end=' ')
            else:
                if celda == '#':
                    print("🚫", end=" ")
                elif celda == ' ':
                    print("🟫", end=" ")
                elif celda == 'S':
                    print("🚩", end=" ")
                elif celda == 'E':
                    print("🎯", end=" ")
                else:
                    print(celda, end=' ')
        print()

    time.sleep(0.2)

#Parte 5: Agoritmo BFS
def bfs(tablero, inicio):
    filas, columnas = len(tablero), len(tablero[0])
    visitado = [[False]*columnas for _ in range(filas)]
    cola = deque
    cola.append(inicio)
    visitado[inicio[0]][inicio[1]] = True

    while cola:
        x, y = cola.popleft()
        imprimir_tablero(tablero, visitado)

        if tablero[x][y] == 'E':
            print("¡Camino encontrado hasta el destino! 🎉")
            return True
        
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas:
                if not visitado[nx][ny] and tablero[nx][ny] != '#':
                    cola.append((nx, ny))
                    visitado[nx][ny] = True

    imprimir_tablero(tablero, visitado)
    print("No se encontró un camino 😢")
    return False 
    
#Parte 6: Ejecutar
def encontrar_inicio(tablero):
    for i in range(len(tablero)): # i: arriba, abajo
        for j in range(len(tablero[0])): #izquierda, derecha
            if tablero[i][j] == 'S':
                return (i,j)
    return None

inicio = encontrar_inicio(tablero)
if inicio:
    bfs(tablero, inicio)
else:
    print("Error: No se encontró el punto de inicio 'S'.")