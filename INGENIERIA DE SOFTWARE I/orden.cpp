#include <iostream>
#include <vector>
#include <string>

using namespace std;

void burbuja(vector<string> &arr) {
    int n = arr.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main() {
    vector<string> strings;
    string cadena;

    cout << "Ingresa las cadenas una por una. Para finalizar, presiona Enter sin ingresar una cadena." << endl;
    
    while (true) {
        cout << "Cadena: ";
        getline(cin, cadena);
        if (cadena.empty()) {
            break;
        }
        strings.push_back(cadena);
    }

    // Llamada a la función de ordenamiento burbuja
    burbuja(strings);

    // Imprimir las cadenas ordenadas
    cout << "\nCadenas ordenadas:" << endl;
    for (const string &str : strings) {
        cout << "ORDEN: " << str << endl;
    }

    return 0;
}
