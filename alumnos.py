alumnos = []

def letras(mensaje):
    while True:
        entrada= input(mensaje )
        if entrada.isalpha() == True:
            return entrada
        else:
            print("Solo letras")
while True:
    try:
        opcion = int(input("Ingrese que opción desea, agregar alumno (1) mostrar total de alumnos(2) salir(3)" ))
    except:
        print(f"Error, solo numeros ")
        continue

    if opcion == 1:
        while True:
            try:
                cantidadalumnos = int(input("Ingrese la cantidad de alumnos "))
                if cantidadalumnos >0:
                    break
                else:
                    print("Ingrese un numero positivo")
            except:
                print("Solo numeros")
        for p in range(cantidadalumnos):
            print(f"Ingresando alumno numero {p+1}")
            nombres = input("Ingrese el nombre del alumno")
            alumnos.append(nombres)
    elif opcion == 2:
        print(alumnos)
        
    elif opcion == 3:
        print("Programa finalizado")
        break
    else:
        print("Error opcion incorrecta")