#include <iostream>
#include <vector>

using namespace std;

// Primero vamos a entender que significa cada numero en nuestro mapa
// 0 = LIBRE (puedo caminar)
// 1 = EDIFICIO (no puedo pasar)

int main() {
    // Este es nuestro mapa como numeros
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

    cout << "=== MAPA CON NUMEROS ===" << endl;
    cout << "0 = camino libre, 1 = edificio (no puedes pasar)" << endl;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            cout << mapa[i][j] << " ";
        }
        cout << endl;
    }

    cout << "\n=== MAPA CON SÍMBOLOS ===" << endl;
    cout << ". = camino libre, X = edificio" << endl;
    for (int i = 0; i < 10; i++) {
        for (int j = 0; j < 10; j++) {
            if (mapa[i][j] == 0) {
                cout << ". ";   // Punto para camino libre
            } else {
                cout << "X ";   // X para edificio
            }
        }
        cout << endl;
    }
    return 0;

}