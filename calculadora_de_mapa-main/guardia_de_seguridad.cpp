#include <iostream>
#include <vector>
using namespace std;

const int FILAS = 10;
const int COLUMNAS = 10;
const int LIBRE = 0;
const int EDIFICIO = 1;

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

// Esta función es como un guardia de seguridad
// Verifica si puedes moverte a una posición
bool esValido(int x, int y) {
    // ¿Está dentro del mapa?
    bool dentroDelMapa = (x >= 0 && x < FILAS && y >= 0 && y < COLUMNAS);
    
    // ¿Es un camino libre?
    bool esLibre = false;
    if (dentroDelMapa) {
        esLibre = (mapa[x][y] == LIBRE);
    }
    
    return dentroDelMapa && esLibre;
}

int main() {
    cout << "=== PROBANDO SI PODEMOS MOVERNOS A DIFERENTES POSICIONES ===" << endl;
    
    // Vamos a probar diferentes posiciones
    vector<pair<int, int>> posiciones = {
        {0, 0},   // Esquina superior izquierda
        {0, 2},   // Un edificio
        {4, 4},   // Centro del mapa
        {-1, 5},  // Fuera del mapa (arriba)
        {5, 15},  // Fuera del mapa (derecha)
        {9, 9}    // Esquina inferior derecha
    };
    
    for (auto pos : posiciones) {
        int x = pos.first;
        int y = pos.second;
        
        cout << "Posición (" << x << ", " << y << "): ";
        
        if (esValido(x, y)) {
            cout << "✅ SÍ puedes moverte aquí" << endl;
        } else {
            cout << "❌ NO puedes moverte aquí";
            
            // Explicamos por qué no puede
            if (x < 0 || x >= FILAS || y < 0 || y >= COLUMNAS) {
                cout << " (fuera del mapa)";
            } else if (mapa[x][y] != LIBRE) {
                cout << " (hay un edificio)";
            }
            cout << endl;
        }
    }
    
    // Ahora tú prueba una posición
    int miX, miY;
    cout << "\n¡Tu turno! Ingresa una posición para probar (fila columna): ";
    cin >> miX >> miY;
    
    if (esValido(miX, miY)) {
        cout << "¡Genial! Puedes moverte a (" << miX << ", " << miY << ")" << endl;
    } else {
        cout << "¡Ups! No puedes moverte a (" << miX << ", " << miY << ")" << endl;
    }
    
    return 0;
}
