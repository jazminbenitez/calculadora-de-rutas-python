import random
import time
import os
from collections import deque

# Pregunta el tamaño del mapa
filas = int(input('Ingresa el tamaño de la fila: '))
columnas = int(input('Ingresa el tamaño de la columna: '))

# Genera un mapa aleatorio
def generar_mapa(filas, columnas):
    valores = [0]*60 + [1]*20 + [2]*15 + [3]*5
    mapa = []
    for _ in range(filas):
        fila = [random.choice(valores) for _ in range(columnas)]
        mapa.append(fila)
    return mapa

mapa_numerico = generar_mapa(filas, columnas)

# Convierte el mapa numérico a símbolos visuales
def convertir_a_tablero(mapa_numerico):
    tablero = []
    for fila in mapa_numerico:
        nueva_fila = []
        for celda in fila:
            if celda == 0:
                nueva_fila.append(' ')   # libre
            elif celda == 1:
                nueva_fila.append('#')   # edificio
            elif celda == 2:
                nueva_fila.append('~')   # agua
            elif celda == 3:
                nueva_fila.append('X')   # zona bloqueada
        tablero.append(nueva_fila)
    return tablero

# Agrega obstáculos personalizados
def agregar_obstaculo_personalizado(mapa_numerico, filas, columnas):
    while True:
        opcion = input("¿Quieres agregar un obstáculo personalizado? (s/n): ").strip().lower()
        if opcion == 's':
            try:
                x = int(input("🧭 Ingresa la fila del obstáculo: "))
                y = int(input("🧭 Ingresa la columna del obstáculo: "))
                tipo = int(input("🏗️ Tipo de obstáculo (1: edificio, 2: agua, 3: zona bloqueada): "))

                if 0 <= x < filas and 0 <= y < columnas:
                    if tipo in [1, 2, 3]:
                        mapa_numerico[x][y] = tipo
                        print("✅ ¡Obstáculo añadido con éxito! 🧱")
                    else:
                        print("🚫 Tipo de obstáculo inválido. Usa 1, 2 o 3.")
                else:
                    print("📍 Las coordenadas están fuera del mapa. Intenta de nuevo.")
            except ValueError:
                print("⚠️ ¡Eso no era un número! Intenta de nuevo con dígitos reales.")
        elif opcion == 'n':
            print("👌 No se agregaron más obstáculos.")
            break
        else:
            print("❓ Por favor responde con 's' o 'n'.")

# Pedir coordenadas válidas
def pedir_coordenadas(nombre, tablero):
    while True:
        try:
            x = int(input(f"Ingrese la fila de {nombre}: "))
            y = int(input(f"Ingrese la columna de {nombre}: "))
            if 0 <= x < filas and 0 <= y < columnas and tablero[x][y] == ' ':
                return x, y
            else:
                print("❌ Coordenadas inválidas o sobre obstáculo.")
        except:
            print("⚠ Entrada no válida.")

# Imprimir el mapa bonito
def imprimir_tablero(tablero, visitado=None):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i, fila in enumerate(tablero):
        for j, celda in enumerate(fila):
            if visitado and visitado[i][j] and tablero[i][j] not in ('S', 'E'):
                print("⭐", end=' ')
            elif celda == '🐧' or celda == '*':
                print("🐧", end=' ')
            elif celda == ' ':
                print("🟫", end=' ')
            elif celda == '#':
                print("🏢", end=' ')
            elif celda == '~':
                print("💧", end=' ')
            elif celda == 'X':
                print("⛔", end=' ')
            elif celda == 'S':
                print("🚩", end=' ')
            elif celda == 'E':
                print("🎯", end=' ')
        print()
    time.sleep(0.2)

# Búsqueda BFS
def bfs(tablero, inicio, fin):
    filas, columnas = len(tablero), len(tablero[0])
    visitado = [[False]*columnas for _ in range(filas)]
    padre = [[None]*columnas for _ in range(filas)]
    cola = deque()

    x0, y0 = inicio
    cola.append((x0, y0))
    visitado[x0][y0] = True

    encontrado = False  # <- NUEVO: para saber si llegamos al final

    while cola and not encontrado:  # <- solo seguimos si no lo hemos encontrado
        x, y = cola.popleft()
        imprimir_tablero(tablero, visitado)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas:
                if not visitado[nx][ny] and tablero[nx][ny] in (' ', 'E'):
                    visitado[nx][ny] = True
                    padre[nx][ny] = (x, y)
                    cola.append((nx, ny))

                    if (nx, ny) == fin:
                        encontrado = True
                        break  # Ya encontramos el final, salimos del bucle

    if encontrado:
        print("¡Ruta encontrada! 🎉")
        return reconstruir_rutas(padre, inicio, fin), visitado
    else:
        print("No se encontró un camino 😓")
        return None, visitado

# Reconstruir el camino encontrado
def reconstruir_rutas(padre, inicio, fin):
    camino = []
    x, y = fin
    while (x, y) != inicio:
        camino.append((x, y))
        x, y = padre[x][y]
        if (x, y) is None:
            break  # No hay camino
    camino.reverse()
    return camino

# ------------ EJECUCIÓN PRINCIPAL ------------

agregar_obstaculo_personalizado(mapa_numerico, filas, columnas)
tablero = convertir_a_tablero(mapa_numerico)

sx, sy = pedir_coordenadas("INICIO", tablero)
ex, ey = pedir_coordenadas("FIN", tablero)

tablero[sx][sy] = 'S'
tablero[ex][ey] = 'E'

inicio = (sx, sy)
fin = (ex, ey)
ruta, visitado = bfs(tablero, inicio, fin)

if ruta:
    for x, y in ruta:
        if tablero[x][y] not in ('S', 'E'):
            tablero[x][y] = '*'
        imprimir_tablero(tablero, visitado)
    print("✨ Ruta final marcada con ⭐")

else:
    imprimir_tablero(tablero)
    print("❌ No se encontró ningún camino válido. ¡Ups! 🚫😓")
