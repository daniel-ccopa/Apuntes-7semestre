import struct
import os

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def crear(ape, nom, notas):
    prom = sum(notas) / len(notas)
    return struct.pack(f'20s 20s {len(notas)}f f', ape.encode(), nom.encode(), *notas, prom)

def lectura(data, num_notas):
    unpacked_data = struct.unpack(f'20s 20s {num_notas}f f', data)
    ape, nom = unpacked_data[:2]
    notas = unpacked_data[2:2+num_notas]
    prom = unpacked_data[-1]
    return ape.decode().strip(), nom.decode().strip(), notas, prom

def clasificar(prom):
    if prom <= 7:
        return "Dediacte a otra cosa"
    elif prom <= 11:
        return "Deficiente"
    elif prom <= 14:
        return "Regular"
    elif prom <= 17:
        return "Bueno"
    else:
        return "Excelente"

def grabar(archivo, cursos):
    alumnos = []
    num_notas = len(cursos)

    while True:
        limpiar()
        print("\nPara terminar los registros, Presione ENTER.\n")
        ape = input("\nAPELLIDOS: ")
        if not ape:
            break
        nom = input("NOMBRES: ")

        notas = []
        for i, curso in enumerate(cursos):
            while True:
                try:
                    nota = float(input(f"Nota de {curso}: "))
                    if 0 <= nota <= 20:
                        notas.append(nota)
                        break
                    else:
                        print("La nota es inválida.")
                except ValueError:
                    print("Entrada inválida. Ingrese una nota verdadera.")

        alumnos.append(crear(ape, nom, notas))

    alumnos.sort(key=lambda x: struct.unpack(f'f', x[-4:])[0], reverse=True)

    with open(archivo, 'wb') as pf:
        pf.write(struct.pack('i', num_notas))  # Guardar el número de notas
        for curso in cursos:  # Guardar los nombres de los cursos
            pf.write(struct.pack('20s', curso.encode()))  
        pf.writelines(alumnos)  # Grabar todos los registros en el archivo

def recuperar(archivo):
    with open(archivo, 'rb') as pf:
        num_notas = struct.unpack('i', pf.read(4))[0]  # Leer el número de notas

        # Leer los cursos
        cursos = []
        for _ in range(num_notas):
            curso = struct.unpack('20s', pf.read(20))[0].decode().strip()
            cursos.append(curso)

        alumno_size = struct.calcsize(f'20s 20s {num_notas}f f')
        while True:
            data = pf.read(alumno_size)
            if not data:
                break
            ape, nom, notas, prom = lectura(data, num_notas)
            desempeno = clasificar(prom)

            # Mostrar los cursos con las notas correspondientes
            print(f"\nApellidos: {ape}\nNombres: {nom}")
            for i, nota in enumerate(notas):
                print(f"{cursos[i]}: {nota:.2f}")
            print(f"Promedio: {prom:.2f}\nDesempeño: {desempeno}")
            
def listar():
    archivos = [f for f in os.listdir() if f.endswith('.bin')]
    if archivos:
        for i, archivo in enumerate(archivos, 1):
            print(f"{i}. {archivo}")
    else:
        print("No hay archivos binarios en el directorio.")
    return archivos

def menu():
    while True:
        limpiar()
        print("-----MENU DE ARCHIVO BINARIOS-----")
        print("\n1. Grabar un archivo binario")
        print("2. Recuperar un archivo binario")
        print("3. Salir")
        print("===================================")
        opcion = input("\nSeleccione una opción: ")
        limpiar()

        if opcion == '1':
            arch = input("Nombre del archivo: ") + ".bin"
            cursos = []
            limpiar()

            print("\nPRESIONE ENTER PARA TERMINAR\n")
            while True:
                curso = input("Nuevo curso:  ")
                if not curso:
                    break
                cursos.append(curso)

            if cursos:
                grabar(arch, cursos)
            else:
                input("Debe ingresar al menos un curso. Presione Enter para continuar...")

        elif opcion == '2':
            limpiar()
            archivos = listar()
            if archivos:
                try:
                    num = int(input("\nSeleccione el número de archivo que desea recuperar: "))
                    if 1 <= num <= len(archivos):
                        limpiar()
                        print(f"\nREGISTROS GUARDADOS\n")
                        recuperar(archivos[num-1])
                        input("\nPresione Enter para finalizar la lectura...")
                    else:
                        input("Número inválido. Presione Enter para continuar...")
                except ValueError:
                    input("Entrada inválida. Debe ingresar un número. Presione Enter para continuar...")
            else:
                input("Presione Enter para continuar...")
        elif opcion == '3':
            limpiar()
            break
        else:
            input("Opción no válida. Presione Enter para intentar nuevamente...")

menu()  