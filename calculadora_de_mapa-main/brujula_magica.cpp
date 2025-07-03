#include <iostream>
#include <vector>

using namespace std;

const int FILAS = 10;
const int COLUMNAS = 10;

// Estos arrays son como una brujula magica
// Te dicen como moverte en 4 direcciones
int dx[4] = {-1, 1, 0, 0}; // movimiento en filas: arriba, abajo, quieto, quieto
int dy[4] = {0, 0, -1, 1}; // movimiento en columnas: quieto, quieto, izquierda, derecha

vector<vector<int>> mapa = {
    {0, 0, 1, 0, 0, 0, 1, 0, 0, 0},
    {0, 1, 1, 0, 1, 0, 1, 1, 1, 0},
    {0, 0, 0, 0, 1, 0, 0, 0, 1, 0},
    {1, 1, 0, 1, 1, 1, 0, 1, 1, 0},
    {0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
    {0, 1, 1, 1, 1, 1, 0, 1, 0, 1},
    {0, 0, 0, 0, 0, 0, 0, 1, 0, 0},
    {1, 1, 1, 1, 1, 1, 0, 1, 1, 0},
    {0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
    {0, 1, 1, 1, 0, 0, 0, 1, 1, 0}
};

bool esValido(int x, int y) {
    return x >= 0 && x < FILAS && y >= 0 && y < COLUMNAS && mapa[x][y] == 0;
}

void mostrarMapa() {
    cout << "   ";
    for (int j = 0; j < COLUMNAS; j++) {
        cout << j << " ";
    }
    cout << endl;

    for (int i = 0; i < FILAS; i++) {
        cout << i << ": ";
        for (int j = 0; j < COLUMNAS; j++) {
            if (mapa[i][j] == 0) {
                cout << ". ";
            } else {
                cout << "X ";
            }
        }
        cout << endl;
    }
}

int main() {
    cout << "=== ENTENDIENDO LOS MOVIMIENTOS ===" << endl;
    cout << "Índice 0: Arriba,    Índice 1: Abajo" << endl;
    cout << "Índice 2: Izquierda, Índice 3: Derecha" << endl;
    cout << endl;

    mostrarMapa();

    int x, y;
    cout << "\nIngresa tu posición actual (fila columna): ";
    cin >> x >> y;

    if (!esValido(x, y)) {
        cout << "¡Esa posición no es válida!" << endl;
        return 1;
    }

    cout << "\nDesde la posición (" << x << ", " << y << ") puedes moverte a:" << endl;

    // Nombres de las direcciones para que sea mas facil de entender
    string direcciones[4] = {"Arriba", "Abajo", "Izquierda", "Derecha"};

    for (int i = 0; i < 4; i++) {
        int nuevaX = x + dx[i];
        int nuevaY = y + dy[i];

        cout << direcciones[i] << " -> (" << nuevaX << ", " << nuevaY << "): ";

        if (esValido(nuevaX, nuevaY)) {
            cout << "✅ SÍ puedes ir" << endl;
        } else {
            cout << "❌ NO puedes ir";
            if (nuevaX < 0 || nuevaX >= FILAS || nuevaY < 0 || nuevaY >= COLUMNAS) {
                cout << " (fuera del mapa)";
            } else {
                cout << " (hay obstáculo)";
            }
            cout << endl;
        }
    }

    return 0;
    
}