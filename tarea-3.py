datos = {
    'codigo': [],
    'nombre': [],
    'seccion': [],
    'curso': [],
    'nota': []
}
contador = 0

def menu():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de datos")
    print("\t\t\t\t\t2 - Visualizacion de datos")
    print("\t\t\t\t\t3 - Consulta de datos")
    print("\t\t\t\t\t0 - Salir")
    print("==================================================================================")


def mostrar(x):
    print(datos['codigo'][x].ljust(20, " "), end="")
    print(datos['nombre'][x].ljust(25, " "), end="")
    print(datos['seccion'][x].ljust(10, " "), end="")
    print(datos['curso'][x].ljust(20, " "), end="")
    print(datos['nota'][x].ljust(10, " "), end="")
    print("")



def ingreso():
    print("Registro Numero    #" + str(contador))
    datos['codigo'].append(input("Ingrese Su codigo"))
    datos['nombre'].append(input("Ingrese el Nombre"))
    datos['seccion'].append(input("Ingrese el Seccion"))
    datos['curso'].append(input("Ingrese el Curso"))
    datos['nota'].append(input("Ingrese el Nota"))


def visualizacion():
    print("==================================================================================")
    print(("CODIGO:").ljust(20, " ") + ("NOMBRE:").ljust(25, " ") + ("SECCION:").ljust(10, " ")
          + ("CURSO:").ljust(20," ") + ("NOTA:").ljust(10, " "))
    print("==================================================================================")
    for x in range(0, contador):
        mostrar(x)
    print("==================================================================================")


def consulta(num1):
    encontrado = False
    for x in range(0, contador):
        if datos['codigo'][x] == num1:
            print("==================================================================================")
            print(("CODIGO:").ljust(20, " ") + ("NOMBRE:").ljust(25, " ") + ("SECCION:").ljust(10, " ")
                  + ("CURSO:").ljust(20, " ") + ("NOTA:").ljust(10, " "))
            print("==================================================================================")
            mostrar(x)
            print("==================================================================================")
            encontrado = True
    if encontrado == False:
        print("No se encontro el registro")
    else:
        print("Si se encontro el registro")

while True:
    menu()

    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
        opcion = "1"
        print("==================================================================================")
        while not opcion == "0":
            ingreso()
            contador = contador + 1
            opcion = input("pulsa una 0 para Salir o Enter para continuar")
            print("==================================================================================")

    elif opcionMenu == "2":
        print("==================================================================================")
        visualizacion()
        print("==================================================================================")
        input("\npulsa una tecla para continuar")
        print("==================================================================================")

    elif opcionMenu == "3":
        print("==================================================================================")
        num1 = input("Ingrese el codigo del estudante a buscar")
        consulta(num1)
        print("==================================================================================")
        input("\npulsa una tecla para continuar")
        print("==================================================================================")


    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")