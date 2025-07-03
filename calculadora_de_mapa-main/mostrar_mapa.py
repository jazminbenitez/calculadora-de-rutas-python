# Primero, vamos a entender qué significa cada número en nuestro mapa
# 0 = LIBRE (puedes caminar)
# 1 = EDIFICIO (no puedes pasar)

# Este es nuestro mapa como números
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

print("=== MAPA CON NÚMEROS ===")
print("0 = camino libre, 1 = edificio (no puedes pasar)")
for fila in mapa:
    for celda in fila:
        print(celda, end=' ')
    print()

print("\n=== MAPA CON SÍMBOLOS ===")
print(". = camino libre, X = edificio")
for fila in mapa:
    for celda in fila:
        if celda == 0:
            print(". ", end='')  # Punto para camino libre
        else:
            print("X ", end='')  # X para edificio
    print()
