# Solicitar al usuario que ingrese las cadenas una por una
strings = []
print("Ingresa las cadenas una por una: ")

while True:
    cadena = input("Ingresa una cadena: ").strip()
    if cadena == "":
        break
    strings.append(cadena)

# Implementar el algoritmo de ordenamiento de burbuja
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            # Comparar y cambiar si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ordenar las cadenas usando el algoritmo de burbuja
bubble_sort(strings)

# Mostrar el resultado
print("Cadenas ordenadas:", strings)
