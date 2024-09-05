strings = []
print("Ingresa las cadenas una por una.")

while True:
    cadena = input(f"Cadena: ").strip()
    if cadena == "":
        break
    strings.append(cadena)

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

burbuja(strings)

print("Cadenas ordenadas:")
for string in strings:
    print(f'ORDEN: {string}')