#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int FILAS = 10;
const int COLUMNAS = 10;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

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


// BFS simple - solo nos dice si podemos llegar
bool puedeLlegar(pair<int, int> inicio, pair<int, int> fin) {
    // La cola es como una lista de tareas por hacer
    queue<pair<int, int>> cola;

    // El array visitado es como marcar con un lapiz los lugares donde ya fuiste 
    vector<vector<bool>> visitado(FILAS, vector<bool>(COLUMNAS, false));

    // Empezamos desde el inicio
    cola.push(inicio);
    visitado[inicio.first][inicio.second] = true;

    cout << "Comenzando busqueda desde (" << inicio.first << ", " << inicio.second << ")" << endl;

    int pasos = 0;
    while (!cola.empty()) {
        auto posicionActual = cola.front();
        cola.pop();

        int x = posicionActual.first;
        int y = posicionActual.second;

        cout << "Revisando la posicion (" << x << ", " << y << ")" << endl;

        // Llegamos al destino?
        if (make_pair(x, y) == fin) {
            cout << "Llegamos al destino en " << pasos << " pasos!" << endl;
            return true;
        }

        // Exploramos las 4 direcciones
        cout << " Explorando vecinos..." << endl;
        for (int i = 0; i < 4; i++) {
            int nuevaX = x + dx[i];
            int nuevaY = y + dy[i];

            if (esValido(nuevaX, nuevaY) && !visitado[nuevaX][nuevaY]) {
                cola.push({nuevaX, nuevaY});
                visitado[nuevaX][nuevaY] = true;
                cout << " ✅Agregando (" << nuevaX << ", " << nuevaY << ") a la lista" << endl;
            }
        }
        pasos++;

        // Para que no se haga muy largo, limitamos la salida
        if (pasos > 20) {
            cout << " ... (continuando busqueda en silenciosamente)" << endl;
            break;
        }
    }

    // Terminamos la busqueda silenciosamente
    while (!cola.empty()) {
        auto posicionActual = cola.front();
        cola.pop();

        int x = posicionActual.first;
        int y = posicionActual.second;

        if (make_pair(x, y) == fin) {
            cout << "¡Encontramos el destino" << endl;
            return true;
        }

        for (int i = 0; i < 4; i++) {
            int nuevaX = x + dx[i];
            int nuevaY = y + dy[i];

            if (esValido(nuevaX, nuevaY) && !visitado[nuevaX][nuevaY]) {
                cola.push({nuevaX, nuevaY});
                visitado[nuevaX][nuevaY] = true;
            }
        }
    }

    cout << "No se pudo llegar al destino" << endl;
    return false;
}



void imprimirMapa() {
    cout << "Mapa del laberinto (0 = libre, 1 = muro):" << endl;
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            cout << mapa[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;
}

    int main() {
        cout << "=== BUSCADOR DE CAMINO (BFS) ===" << endl;
        cout << "BFS es como explorar un laberinto nivel por nivel" << endl;
        cout << "Primero exploramos todos los lugares a paso" << endl;
        cout << "Luego todos los lugares a 2 pasos, y asi..." << endl;
        cout << endl;

        imprimirMapa();

        pair<int, int> inicio, fin;
        cout << "Ingresa coordenadas de inicio (fila columna): ";
        cin >> inicio.first >> inicio.second;
        cin.ignore();
        cout << "Ingresa coordenadas de destino (fila columna): ";
        cin >> fin.first >> fin.second;

        if (!esValido(inicio.first, inicio.second)) {
            cout << "La posicion del inicio no es valida" << endl;
            return 1;
        }
        if (!esValido(fin.first, fin.second)) {
            cout << "La posicion del destino no es valida" << endl;
            return 1;
        } 
        if (puedeLlegar(inicio, fin)) {
            cout << "Si hay un camino" << endl;
        } else {
            cout << "NO hay camino posible" << endl;
        }

    return 0;

}

