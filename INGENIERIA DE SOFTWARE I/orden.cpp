#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>

using namespace std;

int main() {
    string input;
    vector<string> strings;

    // Solicitar al usuario que ingrese las cadenas separadas por comas
    cout << "Ingresa las cadenas separadas por comas: ";
    getline(cin, input);  // Captura toda la línea de entrada

    // Crear un stringstream para dividir la cadena de entrada
    stringstream ss(input);
    string item;

    // Dividir la cadena de entrada en subcadenas usando la coma como delimitador
    while (getline(ss, item, ',')) {
        // Eliminar espacios en blanco al principio y al final de cada subcadena
        item.erase(item.begin(), find_if(item.begin(), item.end(), [](int ch) {
            return !isspace(ch);
        }));
        item.erase(find_if(item.rbegin(), item.rend(), [](int ch) {
            return !isspace(ch);
        }).base(), item.end());
        strings.push_back(item);
    }

    // Ordenar las cadenas en orden lexicográfico
    sort(strings.begin(), strings.end());

    // Mostrar el resultado
    cout << "Cadenas ordenadas: " << endl;
    for (const auto& str : strings) {
        cout << str << endl;
    }

    return 0;
}