fila = []
columna = []

def crear_mapa (filas, columnas):
    mapa = [['🐧' for _ in range(filas)] for _ in range(columnas)]
    return mapa

def mostrar_mapa(mapa):
    for fila in mapa:
        print(" ".join(fila))

def pedir_numero(mensaje):
    while True: 
        try:
            valor = int(input(mensaje))
            if valor <= 0:
                print("¡Ey! El número debe ser mayor que cero, no un número fantasma 👻.")
            else:
                return valor
        except ValueError:
            print("Eso no es un número válido. Intenta de nuevo, ¡no es tan difícil! 🤓")

def posicion(mapa):
    filas = len(mapa)
    columnas = len(mapa[0])
    mapa [0][0] = '🚩'
    mapa [filas - 1][columnas - 1] = '🏁'
    return mapa

print("¡Vamos a crear tu mapa! ¿Cunatas filas y columnas querés?")

filas = pedir_numero("Ingresa la cantidad de filas: ")
columnas = pedir_numero("Ingresa la cantidad de columnas: ")

mapa = crear_mapa(filas, columnas)
mapa = posicion(mapa)

print("\nEste es tu mapa inicial:")
mostrar_mapa(mapa)


