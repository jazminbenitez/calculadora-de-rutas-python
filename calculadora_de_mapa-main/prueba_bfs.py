import time
import os
from collections import deque

# 🧱 Tablero de ejemplo (S = inicio, E = fin, ' ' = camino libre, # = obstáculo)
tablero = [
    ['S', ' ', ' ', '#', ' ', ' ', ' '],
    ['#', '#', ' ', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ', '#', ' '],
    [' ', '#', '#', '#', ' ', ' ', 'E'],
]

# 🖼️ Función para imprimir el tablero paso a paso
def imprimir_tablero(tablero, visitado=None):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola (Windows o Unix)
    for i, fila in enumerate(tablero):
        for j, celda in enumerate(fila):
            if visitado and visitado[i][j] and tablero[i][j] not in ('S', 'E'):
                print('.', end=' ')  # Marca el camino visitado
            else:
                print(celda, end=' ')
        print()
    time.sleep(0.2)  # Espera 0.2 segundos para simular movimiento

# 🚶 BFS que recorre el tablero desde el inicio hasta el final
def bfs(tablero, inicio):
    filas, columnas = len(tablero), len(tablero[0])
    visitado = [[False]*columnas for _ in range(filas)]
    cola = deque()
    cola.append(inicio)
    visitado[inicio[0]][inicio[1]] = True

    while cola:
        x, y = cola.popleft()
        imprimir_tablero(tablero, visitado)

        if tablero[x][y] == 'E':
            print("¡Llegamos al final con éxito! 🎯")
            return True

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:  # Direcciones: arriba, abajo, izq, der
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas:
                if not visitado[nx][ny] and tablero[nx][ny] != '#':
                    cola.append((nx, ny))
                    visitado[nx][ny] = True

    imprimir_tablero(tablero, visitado)
    print("No se encontró un camino 😢")
    return False

# 🔍 Buscar posición de inicio 'S'
def encontrar_inicio(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] == 'S':
                return (i, j)
    return None

# 🚀 Ejecutar todo
inicio = encontrar_inicio(tablero)
if inicio:
    bfs(tablero, inicio)
else:
    print("Error: No se encontró el punto de inicio 'S'.")
