#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int FILAS = 10;
const int COLUMNAS = 10;

enum Terreno { LIBRE = 0, EDIFICIO = 1, AGUA = 2, BLOQUEADO = 3 };

int dx[4] = {-1, 1, 0, 0}; // movimiento en filas: arriba, abajo
int dy[4] = {0, 0, -1, 1}; // movimiento en columnas: izquierda, derecha

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
    return x >= 0 && x < FILAS && y >= 0 && y < COLUMNAS && mapa[x][y] == LIBRE;
}

bool bfs(pair<int, int> inicio, pair<int, int> fin, vector<vector<char>>& mapaVisible) {
    queue<pair<int, int>> q;
    vector<vector<bool>> visitado(FILAS, vector<bool>(COLUMNAS, false));
    vector<vector<pair<int, int>>> padre(FILAS, vector<pair<int, int>>(COLUMNAS, {-1, -1}));

    q.push(inicio);
    visitado[inicio.first][inicio.second] = true;

    while (!q.empty()) {
        auto [x, y] = q.front(); q.pop();

        if (make_pair(x, y) == fin) {
            while (make_pair(x, y) != inicio) {
                mapaVisible[x][y] = '*';
                tie(x, y) = padre[x][y];
            }
            mapaVisible[inicio.first][inicio.second] = 'S';
            mapaVisible[fin.first][fin.second] = 'F';
            return true;
        }

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i], ny = y + dy[i];
            if (esValido(nx, ny) && !visitado[nx][ny]) {
                q.push({nx, ny});
                visitado[nx][ny] = true;
                padre[nx][ny] = {x, y};
            }
        }
    }

    return false;
}

void imprimirMapaVisible(const vector<vector<char>>& mapaVisible) {
    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            cout << mapaVisible[i][j] << " ";
        }
        cout << endl;
    }
}

int main() {
    pair<int, int> inicio, fin;

    cout << "Ingresa coordenadas de inicio (fila y columna): ";
    cin >> inicio.first >> inicio.second;
    cout << "Ingresa coordenadas de destino (fila y columna): ";
    cin >> fin.first >> fin.second;

    if (!esValido(inicio.first, inicio.second) || !esValido(fin.first, fin.second)) {
        cout << "Coordenadas inválidas o en obstáculos.\n";
        return 1;
    }

    vector<vector<char>> mapaVisible(FILAS, vector<char>(COLUMNAS, '.'));

    for (int i = 0; i < FILAS; i++) {
        for (int j = 0; j < COLUMNAS; j++) {
            if (mapa[i][j] != LIBRE) {
                mapaVisible[i][j] = 'X';
            }
        }
    }

    if (bfs(inicio, fin, mapaVisible)) {
        cout << "Ruta encontrada:\n";
        imprimirMapaVisible(mapaVisible);
    } else {
        cout << "No se encontró ruta posible.\n";
    }

    return 0;
}
