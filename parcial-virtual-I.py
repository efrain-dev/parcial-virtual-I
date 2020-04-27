clientes = {
    #Id, 0 Nombre, 1, Direccion, 2 Telefono
    '0': ['Juan Lopez','Su casa','55754832'],
    '1': ['Efrain de Leon','Una casota','55754832']
}
estados = {
    #Id, Estado
    '0': "Prueba",
    '1': "Terminado"
}
departamentos = {
     'Izabal':['Puerto Barrios', 'Morales', 'Rio Dulce','Los Amates','Livinstong'],
}
registro = {
    #id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
    '0':['0','0','Izabal','0']
}

def cleanScreen():
    print("\n"*200)
def menu():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Menu Clientes")
    print("\t\t\t\t\t2 - Menu Departamentos")
    print("\t\t\t\t\t3 - Menu Estados")
    print("\t\t\t\t\t4 - Menu Solicitudes y Reportes")
    print("\t\t\t\t\t0 - Salir")
    print("==================================================================================")
def descpripcionMenuEdicion():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Editar Registro")
    print("\t\t\t\t\t2 - Eliminar registro")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
#Seccion de cliente======================================================================================================
def descpripcionMenuClientes():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de clientes")
    print("\t\t\t\t\t2 - Visualizacion de clientes")
    print("\t\t\t\t\t3 - Consulta de clientes")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def encabezadoCliente():
    print("==================================================================================")
    print(("ID:").ljust(20, " ") + ("NOMBRE:").ljust(25, " ") + ("DIRECCION:").ljust(20, " ")
          + ("TELEFONO:").ljust(20, " "))
    print("==================================================================================")
def editarClientes(id):
    print("1. Nombre")
    print("2. Direccion")
    print("3. Telefono")
    opcionIngresada = int(input("Ingrese la opcion"))
    if opcionIngresada == 1:
        clientes[id] = [input("Ingrese el nombre"),clientes[id][1],clientes[id][2]]
    elif opcionIngresada == 2:
        clientes[id]= [clientes[id][0],input("Ingrese el direccion"),clientes[id][2]]
    elif opcionIngresada == 3:
        clientes[id] = [clientes[id][0],clientes[id][1],input("Ingrese el Telefono")]
    consultaClientes(id)
    print("Edicion Completada")
def eliminarClientes(id):
    clientes.pop(id,None)
    print("Cliente Eliminado")
def subMenuConsulaClientes(id):
    while True:
        descpripcionMenuEdicion()
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":
            opcion = "1"
            print("==================================================================================")
            while not opcion == "0":
                editarClientes(id)
                opcion = input("pulsa una 0 para Salir o Enter para continuar")
                print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            eliminarClientes(id)
            print("==================================================================================")
            input("\npulsa una tecla para continuar")
            print("==================================================================================")
            break
        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def mostrarClientes():
    encabezadoCliente()
    for k, v in clientes.items():
        print(k.ljust(20, " "), end="")
        print(v[0].ljust(25, " "), end="")
        print(v[1].ljust(20, " "), end="")
        print(v[2].ljust(20, " "), end="")
        print("")
def ingresoClientes():
    id = input("Ingrese el id")
    if id  in clientes:
        print("Ese id ya existe")
    else:
        clientes[id] = [input("Ingrese el nombre"),input("Ingrese su direccion"),input("Ingrese su telefono")]
def consultaClientes(id):
    encabezadoCliente()
    if id in clientes:
        print(id.ljust(20, " "), end="")
        print(clientes[id][0].ljust(25, " "), end="")
        print(clientes[id][1].ljust(20, " "), end="")
        print(clientes[id][2].ljust(20, " "), end="")
        print("")
        subMenuConsulaClientes(id)
    else:
        print("Este Usuario no existe")
#Seccion de cliente=======================================================================================================
#Seccion de departamento==================================================================================================
def descpripcionMenuDepartamento():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de departamentos")
    print("\t\t\t\t\t2 - Visualizacion de departamentos y municipios")
    print("\t\t\t\t\t3 - Consulta de departamento")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def editarDepartamento(nombre):
    print("Edicion departamento")
    print("1. Nombre")
    print("2. Municipios")
    opcionIngresada = int(input("Ingrese la opcion"))
    if opcionIngresada == 1:
        editNombre = input("Ingrese el nuevo nombre del departamento")
        listTemporal = departamentos[nombre]
        departamentos.pop(nombre)
        departamentos[editNombre] = listTemporal
    elif opcionIngresada == 2:
        for x in range(0, len(departamentos[nombre])):
            print(str(x)+". "+departamentos[nombre][x].ljust(60, " "))
        opcionEditar = int(input("Ingrese el indice del municipio a editar"))
        print("1. Si desea editarlo")
        print("2. Si desea Eliminarlo")
        menuOpcion =input(input("Ingrese la opcion"))
        if menuOpcion == 1:
            departamentos[nombre][opcionEditar] = input("Modificacion de municipio")
        elif menuOpcion == 2:
           del departamentos[nombre][opcionEditar]
    print("Edicion Completada")
    input("\npulsa una tecla para continuar")
    print("==================================================================================")
def eliminarDepartamento(nombre):
    departamentos.pop(nombre,None)
    print("Departamento Eliminado")
def subMenuConsultaDepartamento(nombre):
    descpripcionMenuEdicion()
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
            editarDepartamento(nombre)

    elif opcionMenu == "2":
        print("==================================================================================")
        eliminarDepartamento(nombre)
        print("==================================================================================")
        input("\npulsa una tecla para continuar")
        print("==================================================================================")
def mostrarDepartamento():
    for k, v in departamentos.items():
        print("==================================================================================")
        print(("DEPARTAMENTO").ljust(20, " "), end="")
        print(k.ljust(20, " "))
        print("==================================================================================")
        print( ("MUNICIPIOS").ljust(20, " "))
        print("==================================================================================")
        for x in range(0,len(v)):
            print(str(x)+". "+v[x].ljust(60, " "))
def ingresoDepartamento():
    cleanScreen()
    print("==================================================================================")
    nameDepartamento = input("El nombre del departamento:   ")
    print("==================================================================================")
    if nameDepartamento  in departamentos:
        print("Este de departmaento ya existe")
    else:
        listaTemporal = []
        opcion = "1"
        while not opcion == "0":
            listaTemporal.append(input("Ingrese un municipio"))
            opcion = input("pulsa una 0 para Salir o Enter para ingresar otro municipio")
            print("==================================================================================")
        departamentos[nameDepartamento] = listaTemporal
        input("Departamento ingresado Correctamenta  \nEnter para Continuar")
def consultaDepartamento(nombre):
    if nombre in departamentos:
        print("==================================================================================")
        print(("DEPARTAMENTO").ljust(20, " "), end="")
        print(nombre.ljust(20, " "))
        print("==================================================================================")
        print( ("MUNICIPIOS").ljust(20, " "))
        print("==================================================================================")
        for x in range(0, len(departamentos[nombre])):
            print(departamentos[nombre][x].ljust(60, " "))
        subMenuConsultaDepartamento(nombre)
    else:
        print("Este departamento no existe")
#Seccion de departamento==================================================================================================
#Seccion de estados=======================================================================================================
def despcripcionMenuEstados():
    cleanScreen()
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de un Nuevo Estado Proceso")
    print("\t\t\t\t\t2 - Visualizacion de los estados existentes")
    print("\t\t\t\t\t3 - Consulta de estados de proceso")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def editarEstado(id):
    print("Edicion del nombre del estado")
    nuevoNombre = input("Ingre el nuevo nombre el estado")
    estados[id] = nuevoNombre
    print("Edicion Completada")
def eliminarEstado(id):
    estados.pop(id,None)
    print("Estad Eliminado")
def subMenuConsultaEstado(id):
    descpripcionMenuEdicion()
    opcionMenu = input("inserta un numero valor >> ")

    if opcionMenu == "1":
            editarEstado(id)

    elif opcionMenu == "2":
        print("==================================================================================")
        eliminarEstado(id)
        print("==================================================================================")
def mostrarEstados():
    print("==================================================================================")
    print(("ID ").ljust(20, " ")+("NOMBRE").ljust(20, " "))
    for k in estados:
        print(k.ljust(20, " "), end="")
        print(estados[k].ljust(20, " "), end="")
        print("")
def ingresoEstado():
    cleanScreen()
    print("==================================================================================")
    nameEstado = input("Ingrese el nombre del estado:        ")
    idEstado = input(  "Ingrese el id del estado: ")
    print("==================================================================================")
    if idEstado  in estados:
        print("Este estado ya esta ingreasado ")
    else:
        estados[idEstado] = nameEstado
        print("Estado ingresado Correctamente")
def consultaEstado(id):
    cleanScreen()
    if id in estados:
        print(("ID ").ljust(20, " ") + ("NOMBRE").ljust(20, " "))
        print(id.ljust(20, " "), end="")
        print(estados[id].ljust(20, " "), end="")
        print("")
        subMenuConsultaEstado(id)
    else:
        print("Este estado no existe")
#Seccion de estados======================================================================================================

#Seccion de Proyectos====================================================================================================
def descripcionMenuProeyectos():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de un nuevo Solicitud")
    print("\t\t\t\t\t2 - Visualizacion Solicitudes")
    print("\t\t\t\t\t3 - Consulta de Solicitudes")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def encabezadoProyectos():
    print("==================================================================================")
    print(("ID:").ljust(10, " ") + ("NOMBRE:").ljust(20, " ")+("ESTADO:").ljust(20, " ")  + ("DEPARTAMENTO:").ljust(15, " ")
          + ("MUNICIPIO:").ljust(20, " "))
    print("==================================================================================")
def mostrarProyecto(id):
    print(id.ljust(10, " "), end="")
    print(clientes[registro[id][0]][0].ljust(20, " "), end="")
    print(estados[registro[id][1]].ljust(20, " "), end="")
    print(registro[id][2].ljust(15, " "), end="")
    print(departamentos[registro[id][2]][int(registro[id][3])].ljust(20, " "), end="")
    print("")
def editarProyectos(id):
    print("1. Cliente")
    print("2. Estado")
    print("3. Departamento")
    print("4. Municipio")
    opcionIngresada = int(input("Ingrese la opcion"))
    #id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
    if opcionIngresada == 1:
        mostrarClientes()
        nuevoCliente = input("Ingrese el id del nuevo cliente")
        registro[id] = [nuevoCliente,registro[id][1],registro[id][2],registro[id][3]]
    elif opcionIngresada == 2:
        mostrarEstados()
        nuevoEstado = input("Ingrese el id del nuevo estado")
        registro[id]= [registro[id][0],nuevoEstado,registro[id][2],registro[id][3]]
    elif opcionIngresada == 3:
        mostrarDepartamento()
        nuevoDepartamento = input("Ingre el nombre del Nuevo departamento")
        registro[id] = [registro[id][0],registro[id][1],nuevoDepartamento,registro[id][3]]
    elif opcionIngresada == 4:
        mostrarDepartamento()
        nuevoMunicipio = input("Ingrese el Index del nuevo municipio")
        registro[id] = [registro[id][0],registro[id][1],registro[id][2],nuevoMunicipio]
    encabezadoProyectos()
    mostrarProyecto(id)
    print("==================================================================================")
    print("Edicion Completada")
def eliminarProyecto(id):
    registro.pop(id,None)
    print("Registro Eliminado")
def subMenuConsultaProyectos(id):
    while True:
        descpripcionMenuEdicion()
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":

            print("==================================================================================")
            editarProyectos(id)
            print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            eliminarProyecto(id)
            print("==================================================================================")
            break
        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def mostrarProyectos():
    encabezadoProyectos()
    # id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
    for k, v in registro.items():
        print(k.ljust(10, " "), end="")
        print(clientes[v[0]][0].ljust(20, " "), end="")
        print(estados[v[1]].ljust(20, " "), end="")
        print(v[2].ljust(15, " "), end="")
        print(departamentos[v[2]][int(v[3])].ljust(20, " "), end="")
        print("")
def ingresoProyectos():
    id = input("Ingrese el id del registro")
    if id  in registro:
        print("Ese id ya existe")
    else:
        mostrarClientes()
        idCliente = input("Ingrese el id del Cliente")
        mostrarEstados()
        idEstado = input("Ingrese el id de Estado")
        mostrarDepartamento()
        nombreDepartamento = input("Ingrese el Nombre del departamento")
        idMunicipio = input("Ingrese el Indice del municipio")
        # id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
        registro[id] = [idCliente,idEstado,nombreDepartamento,idMunicipio]
def consultaProyectos(id):
    encabezadoProyectos()
    if id in registro:
        mostrarProyecto(id)
        subMenuConsultaProyectos(id)
    else:
        print("Este Usuario no existe")
#Seccion de Proyectos==================================================================================================
def menuPrincipal():
    while True:
        cleanScreen()
        menu()
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":
            opcion = "1"
            print("==================================================================================")
            while not opcion == "0":
                menuCliente()
                opcion = input("pulsa una 0 para Salir o Enter para continuar")
                print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            menuDepartamento()
            print("==================================================================================")


        elif opcionMenu == "3":
            print("==================================================================================")
            menuEstados()
        elif opcionMenu == "4":
            print("==================================================================================")
            menuRegistros()
            print("==================================================================================")



        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuCliente():
    while True:
        cleanScreen()
        descpripcionMenuClientes()
        opcionMenu = input("inserta un numero valor >> ")
        if opcionMenu == "1":
            opcion = "1"
            print("==================================================================================")
            while not opcion == "0":
                ingresoClientes()
                opcion = input("pulsa una 0 para Salir o Enter para continuar")
                print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            mostrarClientes()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")


        elif opcionMenu == "3":
            print("==================================================================================")
            id = input("Ingrese el codigo del estudante a buscar")
            consultaClientes(id)
            print("==================================================================================")



        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuDepartamento():

    while True:
        cleanScreen()
        descpripcionMenuDepartamento()
        opcionMenu = input("inserta un numero valor >> ")
        if opcionMenu == "1":
            opcion = "1"
            print("==================================================================================")
            ingresoDepartamento()



        elif opcionMenu == "2":
            print("==================================================================================")
            mostrarDepartamento()
            input("Presione 0 Para Salir\nPulsa una tecla para continuar")
            print("==================================================================================")

        elif opcionMenu == "3":
            print("==================================================================================")
            nameDepartamento = input("Ingrese nombre del departamento  ")
            consultaDepartamento(nameDepartamento)


        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuEstados():
    while True:
        cleanScreen()
        despcripcionMenuEstados()
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":
            opcion = "1"
            while not  opcion == "0":
                ingresoEstado()
                print("==================================================================================")
                opcion = input("Presione 0 Para Salir\nPulsa una tecla para continuar Ingresando")
                print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            mostrarEstados()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")

        elif opcionMenu == "3":
            print("==================================================================================")
            id = input("Ingrese el id del estado a buscar")
            print("==================================================================================")
            consultaEstado(id)
            print("==================================================================================")


        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuRegistros():
    while True:
        cleanScreen()
        descripcionMenuProeyectos()
        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu == "1":
            print("==================================================================================")
            ingresoProyectos()
            print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            mostrarProyectos()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")


        elif opcionMenu == "3":
            print("==================================================================================")
            id = input("Ingrese el id del registro")
            consultaProyectos(id)
            print("==================================================================================")



        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


menuPrincipal()



