def crear_mapa(filas, columnas):
    mapa = []
    for i in range(filas):
        fila = ['.' for _ in range(columnas)]
        mapa.append(fila)
    return mapa

def colocar_inicio_fin(mapa, inicio, fin):
    x_ini, y_ini = inicio
    x_fin, y_fin = fin
    mapa[x_ini][y_ini] = 'S'
    mapa[x_fin][y_fin] = 'F'

def imprimir_mapa(mapa):
    for fila in mapa:
        print(' '.join(fila))

# Pedimos al usuario que diga el tamaño
filas = int(input("Dime cuántas filas quieres para el mapa: "))
columnas = int(input("Dime cuántas columnas quieres para el mapa: "))

# Colocamos el inicio y el fin siempre en posiciones válidas
inicio = (0, 0)            
fin = (filas - 1, columnas - 1)

# Creamos el mapa y lo mostramos
mapa = crear_mapa(filas, columnas)
colocar_inicio_fin(mapa, inicio, fin)
imprimir_mapa(mapa)

