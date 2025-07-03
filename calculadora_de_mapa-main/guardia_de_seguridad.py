# Definimos las constantes mágicas
FILAS = 10
COLUMNAS = 10
LIBRE = 0
EDIFICIO = 1

# Nuestro mapa, igualito al de C++, pero con más sabor Python 🐍
mapa = [
    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0, 0, 1, 1, 0]
]

# Esta función es como el guardia del mapa 🚷
def es_valido(x, y):
    dentro_del_mapa = (0 <= x < FILAS and 0 <= y < COLUMNAS)
    
    es_libre = False
    if dentro_del_mapa:
        es_libre = (mapa[x][y] == LIBRE)
    
    return dentro_del_mapa and es_libre

# Probamos diferentes posiciones como en el C++
print("=== PROBANDO SI PODEMOS MOVERNOS A DIFERENTES POSICIONES ===")

posiciones = [
    (0, 0),    # Esquina superior izquierda
    (0, 2),    # Un edificio
    (4, 4),    # Centro del mapa
    (-1, 5),   # Fuera del mapa (arriba)
    (5, 15),   # Fuera del mapa (derecha)
    (9, 9)     # Esquina inferior derecha
]

for x, y in posiciones:
    print(f"Posición ({x}, {y}): ", end="")
    if es_valido(x, y):
        print("✅ SÍ puedes moverte aquí")
    else:
        print("❌ NO puedes moverte aquí", end="")
        if x < 0 or x >= FILAS or y < 0 or y >= COLUMNAS:
            print(" (fuera del mapa)")
        elif mapa[x][y] != LIBRE:
            print(" (hay un edificio)")
        else:
            print()
            
# Tu turno, jugadora oficial del laberinto 🧙‍♀️
try:
    miX = int(input("\n¡Tu turno! Ingresa una posición para probar (fila): "))
    miY = int(input("Ahora la columna: "))

    if es_valido(miX, miY):
        print(f"¡Genial! Puedes moverte a ({miX}, {miY}) 🎯")
    else:
        print(f"¡Ups! No puedes moverte a ({miX}, {miY}) ❌")
except ValueError:
    print("Por favor, ingresa números válidos 🧠")
