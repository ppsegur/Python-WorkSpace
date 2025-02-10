f = "notas.csv"

def cargar_datos():
    alumnos = []
    try:
        with open(f, "r", encoding="utf-8") as file:
            for linea in file:
                nombre, apellidos, curso, notas = linea.strip().split(",")
                notas = {nota.split(":")[0]: int(nota.split(":")[1]) for nota in notas.split(";")}
                alumnos.append({"nombre": nombre, "apellidos": apellidos, "curso": curso, "notas": notas})
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {f}")
    return alumnos

def calcular_nota_media(notas):
    return sum(notas.values()) / len(notas)

def listado_alumnos_con_nota_media(alumnos):
    for alumno in alumnos:
        print(f"{alumno['nombre']} {alumno['apellidos']} - Nota media: {calcular_nota_media(alumno['notas']):.2f}")

def alumnos_de_curso_con_notas_asignatura(alumnos):
    curso = input("Introduce el curso: ").strip()
    asignatura = input("Introduce la asignatura: ").strip()

    for alumno in alumnos:
        if alumno["curso"] == curso and asignatura in alumno["notas"]:
            print(f"{alumno['nombre']} {alumno['apellidos']} - {asignatura}: {alumno['notas'][asignatura]}")
    
def porcentaje_aprobados_por_asignatura(alumnos):
    curso = input("Introduce el curso: ").strip()
    alumnos_curso = [alumno for alumno in alumnos if alumno["curso"] == curso]

    if not alumnos_curso:
        print("No hay alumnos en ese curso.")
        return
    
    asignaturas = alumnos_curso[0]["notas"].keys()
    for asignatura in asignaturas:
        aprobados = sum(1 for alumno in alumnos_curso if alumno["notas"][asignatura] >= 5)
        porcentaje = (aprobados / len(alumnos_curso)) * 100
        print(f"{asignatura}: {porcentaje:.2f}% aprobados")

def nombre_curso_fichero_nota_media(alumnos):
    curso = input("Introduce el curso: ").strip()
    alumnos_curso = [alumno for alumno in alumnos if alumno["curso"] == curso]

    if not alumnos_curso:
        print("No hay alumnos en ese curso.")
        return

    nombre_archivo = f"{curso}.txt"
    with open(nombre_archivo, "w", encoding="utf-8") as file:
        for alumno in alumnos_curso:
            file.write(f"{alumno['nombre']} {alumno['apellidos']} - Nota media: {calcular_nota_media(alumno['notas']):.2f}\n")
    
    print(f"Fichero '{nombre_archivo}' creado correctamente.")

# Cargar datos antes de mostrar el menú
alumnos = cargar_datos()

while True:
    print("\nMenú de opciones:")
    print("1. Listado de alumnos con nota media")
    print("2. Alumnos de un curso con nota en una asignatura")
    print("3. Porcentaje de aprobados por asignatura en un curso")
    print("4. Guardar listado de alumnos y nota media en un fichero")
    print("5. Salir")

    option = input("Introduce una opción: ").strip()

    if option == "1":
        listado_alumnos_con_nota_media(alumnos)
        cargar_datos()
    elif option == "2":
        alumnos_de_curso_con_notas_asignatura(alumnos)
        cargar_datos()
    elif option == "3":
        porcentaje_aprobados_por_asignatura(alumnos)
        cargar_datos()
    elif option == "4":
        nombre_curso_fichero_nota_media(alumnos)
        cargar_datos()
    elif option == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
