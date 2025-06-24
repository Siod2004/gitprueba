alumnos = []

def es_rut(cadena_texto):
    largo = len(cadena_texto)
    contador = 0
    tiene_guion = False
    tiene_digito_verificador = False
    tiene_numeros = False

    for i in cadena_texto:
        if contador == largo-1 and (i.isnumeric() or i == "k"):
            tiene_digito_verificador = True     
        elif contador == largo-1 and i == "-":
            tiene_guion = True
        elif contador < largo-1:
            if i.isnumeric():
                tiene_numeros = True
            else:
                return False
        contador+=1

    if tiene_numeros and tiene_guion and tiene_digito_verificador:
        return True
    else:
        return False

def letras(mensaje):
    while True:
        entrada= input(mensaje)
        if entrada.isalpha() == True:
            return entrada
        else:
            print("Solo letras")

while True:
    try:
        opcion = int(input("Ingrese que opción desea, agregar alumno (1), mostrar total de alumnos(2), eliminar alumno(3), salir(4): "))
    except:
        print(f"Error, solo numeros ")
        continue

    if opcion == 1:
        while True:
            try:
                cantidadalumnos = int(input("Ingrese la cantidad de alumnos "))
                if cantidadalumnos > 0:
                    break
                else:
                    print("Ingrese un numero positivo")
            except:
                print("Solo numeros")
        for p in range(cantidadalumnos):
            print(f"Ingresando alumno numero {p+1}")
            nombres = letras("Ingrese el nombre del alumno: ")  # Validación con la función letras
            alumnos.append(nombres)

    elif opcion == 2:
        print("Lista de alumnos:")
        print(alumnos)

    elif opcion == 3:
        if len(alumnos) == 0:
            print("No hay alumnos para eliminar.")
            continue
        eliminar = letras("Ingrese el nombre del alumno a eliminar: ")
        if eliminar in alumnos:
            alumnos.remove(eliminar)
            print(f"Alumno '{eliminar}' eliminado.")
        else:
            print("Alumno no encontrado.")

    elif opcion == 4:
        print("Programa finalizado")
        break

    else:
        print("Error opcion incorrecta")