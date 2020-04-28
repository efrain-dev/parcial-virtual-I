client = {
    #Id, 0 Nombre, 1, Direccion, 2 Telefono
    '0': ['Juan Lopez','Su casa','55754832'],
    '1': ['Efrain de Leon','Una casota','55754832']
}
status = {
    #Id, Estado
    '0': "Prueba",
    '1': "Terminado"
}
departments = {
     'Izabal':['Puerto Barrios', 'Morales', 'Rio Dulce','Los Amates','Livinstong'],
}
projects = {
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
    print("\t\t\t\t\t4 - Menu Proyectos")
    print("\t\t\t\t\t0 - Salir")
    print("==================================================================================")
def descriptionMenuEdit():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Editar Registro")
    print("\t\t\t\t\t2 - Eliminar registro")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
#Section the Client======================================================================================================
def descriptionMenuClient():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de clientes")
    print("\t\t\t\t\t2 - Visualizacion de clientes")
    print("\t\t\t\t\t3 - Consulta de clientes")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def headerClient():
    print("==================================================================================")
    print(("ID:").ljust(20, " ") + ("NOMBRE:").ljust(25, " ") + ("DIRECCION:").ljust(20, " ")
          + ("TELEFONO:").ljust(20, " "))
    print("==================================================================================")
def editClient(id):
    print("Seleccione el campo")
    print("1. Nombre")
    print("2. Direccion")
    print("3. Telefono")
    optionInsert = int(input("Ingrese la opcion: "))
    if optionInsert == 1:
        client[id] = [input("Ingrese el nombre: "), client[id][1], client[id][2]]
    elif optionInsert == 2:
        client[id]= [client[id][0], input("Ingrese el direccion: "), client[id][2]]
    elif optionInsert == 3:
        client[id] = [client[id][0], client[id][1], input("Ingrese el Telefono: ")]
    print("Edicion Completada")
def deleteClient(id):
    client.pop(id, None)
    print("Cliente Eliminado")
def subMenuConsultClient(id):
    while True:
        descriptionMenuEdit()
        optionMenu = input("inserta un numero valor >> ")

        if optionMenu == "1":
            print("==================================================================================")
            editClient(id)
            print("==================================================================================")
            consultClient(id)
            break
        elif optionMenu == "2":
            print("==================================================================================")
            deleteClient(id)
            print("==================================================================================")
            break
        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def viewClient():
    headerClient()
    for k, v in client.items():
        print(k.ljust(20, " "), end="")
        print(v[0].ljust(25, " "), end="")
        print(v[1].ljust(20, " "), end="")
        print(v[2].ljust(20, " "), end="")
        print("")
def insertClient():
    id = input("Ingrese el id: ")
    if id  in client:
        print("Ese id ya existe")
    else:
        client[id] = [input("Ingrese el nombre: "), input("Ingrese su direccion: "), input("Ingrese su telefono: ")]
def consultClient(id):
    headerClient()
    if id in client:
        print(id.ljust(20, " "), end="")
        print(client[id][0].ljust(25, " "), end="")
        print(client[id][1].ljust(20, " "), end="")
        print(client[id][2].ljust(20, " "), end="")
        print("")
        subMenuConsultClient(id)
    else:
        print("Este Usuario no existe")
#Section the Client=======================================================================================================
#Section the Departament==================================================================================================
def descriptionMenuDepartament():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de departamentos")
    print("\t\t\t\t\t2 - Visualizacion de departamentos y municipios")
    print("\t\t\t\t\t3 - Consulta de departamento")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def editDepartament(name):
    print("Edicion departamento")
    print("1. Nombre")
    print("2. Municipios")
    optionInsert = int(input("Ingrese la opcion: "))
    if optionInsert == 1:
        editNombre = input("Ingrese el nuevo nombre del departamento: ")
        listTemporal = departments[name]
        departments.pop(name)
        departments[editNombre] = listTemporal
    elif optionInsert == 2:
        for x in range(0, len(departments[name])):
            print(str(x) +". " + departments[name][x].ljust(60, " "))
        optionEdit = int(input("Ingrese el indice del municipio a editar: "))
        print("1. Si desea editarlo")
        print("2. Si desea Eliminarlo")
        menuOption =input(input("Ingrese la opcion: "))
        if menuOption == 1:
            departments[name][optionEdit] = input("Modificacion de municipio: ")
        elif menuOption == 2:
           del departments[name][optionEdit]
    print("Edicion Completada")
    input("\nPulsa una tecla para continuar")
    print("==================================================================================")
def deleteDepartament(name):
    departments.pop(name, None)
    print("Departamento Eliminado")
def subMenuConsultDepartament(name):
    descriptionMenuEdit()
    optionInsert = input("Inserte la opcion>> ")

    if optionInsert == "1":
            editDepartament(name)

    elif optionInsert == "2":
        print("==================================================================================")
        deleteClient(name)
        print("==================================================================================")
        input("\nPulsa una tecla para continuar")
        print("==================================================================================")
def viewDepartament():
    for k, v in departments.items():
        print("==================================================================================")
        print(("DEPARTAMENTO").ljust(20, " "), end="")
        print(k.ljust(20, " "))
        print("==================================================================================")
        print( ("MUNICIPIOS").ljust(20, " "))
        print("==================================================================================")
        for x in range(0,len(v)):
            print(str(x)+". "+v[x].ljust(60, " "))
def insertDepartament():
    cleanScreen()
    print("==================================================================================")
    nameDepartament = input("El nombre del departamento: ")
    print("==================================================================================")
    if nameDepartament  in departments:
        print("Este de departmaento ya existe")
    else:
        listaTemporal = []
        opcion = "1"
        while not opcion == "0":
            listaTemporal.append(input("Ingrese un municipio: "))
            opcion = input("Pulsa una 0 para Salir o Enter para ingresar otro municipio")
            print("==================================================================================")
        departments[nameDepartament] = listaTemporal
        input("Departamento ingresado Correctamenta  \nEnter para Continuar")
def consultDepartament(name):
    if name in departments:
        print("==================================================================================")
        print(("DEPARTAMENTO").ljust(20, " "), end="")
        print(name.ljust(20, " "))
        print("==================================================================================")
        print( ("MUNICIPIOS").ljust(20, " "))
        print("==================================================================================")
        for x in range(0, len(departments[name])):
            print(departments[name][x].ljust(60, " "))
        subMenuConsultDepartament(name)
    else:
        print("Este departamento no existe")
#Sectioin the Departament==================================================================================================
#Section the Status=======================================================================================================
def descriptionMenuStatus():
    cleanScreen()
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de un Nuevo Estado Proceso")
    print("\t\t\t\t\t2 - Visualizacion de los estados existentes")
    print("\t\t\t\t\t3 - Consulta de estados de proceso")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def editStatus(id):
    print("Edicion del nombre del estado")
    newName = input("Ingrese el nuevo nombre del estado: ")
    status[id] = newName
    print("Edicion Completada")
def deleteStatus(id):
    status.pop(id, None)
    print("Estad Eliminado")
def subMenuConsultStatus(id):
    descriptionMenuEdit()
    optionMenu = input("Inserte la opcion>> ")

    if optionMenu == "1":
            editStatus(id)

    elif optionMenu == "2":
        print("==================================================================================")
        deleteStatus(id)
        print("==================================================================================")
def viewStatus():
    print("==================================================================================")
    print(("ID ").ljust(20, " ")+("NOMBRE").ljust(20, " "))
    for k in status:
        print(k.ljust(20, " "), end="")
        print(status[k].ljust(20, " "), end="")
        print("")
def insertStatus():
    cleanScreen()
    print("==================================================================================")
    nameStatus = input("Ingrese el nombre del estado: ")
    idStatus = input( "Ingrese el id del estado: ")
    print("==================================================================================")
    if idStatus  in status:
        print("Este estado ya esta ingreasado ")
    else:
        status[idStatus] = nameStatus
        print("Estado ingresado Correctamente")
def consultStatus(id):
    cleanScreen()
    if id in status:
        print(("ID ").ljust(20, " ") + ("NOMBRE").ljust(20, " "))
        print(id.ljust(20, " "), end="")
        print(status[id].ljust(20, " "), end="")
        print("")
        subMenuConsultStatus(id)
    else:
        print("Este estado no existe")
#Section the Status======================================================================================================

#Section the Proyects====================================================================================================
def despcriptionMenuProject():
    print("==================================================================================")
    print("\t\t\t\t\t\t\t\tSelecciona una opción")
    print("\t\t\t\t\t1 - Ingreso de un nuevo Proeycto")
    print("\t\t\t\t\t2 - Visualizacion de los Proyectos")
    print("\t\t\t\t\t3 - Consulta de Proyectos")
    print("\t\t\t\t\t0 - Regresar")
    print("==================================================================================")
def headerProject():
    print("==================================================================================")
    print(("ID:").ljust(10, " ") + ("NOMBRE:").ljust(20, " ")+("ESTADO:").ljust(20, " ")  + ("DEPARTAMENTO:").ljust(15, " ")
          + ("MUNICIPIO:").ljust(20, " "))
    print("==================================================================================")
def viewProject(id):
    print(id.ljust(10, " "), end="")
    print(client[projects[id][0]][0].ljust(20, " "), end="")
    print(status[projects[id][1]].ljust(20, " "), end="")
    print(projects[id][2].ljust(15, " "), end="")
    print(departments[projects[id][2]][int(projects[id][3])].ljust(20, " "), end="")
    print("")
def editProject(id):
    print("1. Cliente")
    print("2. Estado")
    print("3. Departamento")
    print("4. Municipio")
    optionInsert = int(input("Ingrese la opcion: "))
    #id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
    if optionInsert == 1:
        viewClient()
        newClient = input("Ingrese el id del nuevo cliente: ")
        projects[id] = [newClient, projects[id][1], projects[id][2], projects[id][3]]
    elif optionInsert == 2:
        viewStatus()
        newStatus = input("Ingrese el id del nuevo estado: ")
        projects[id]= [projects[id][0], newStatus, projects[id][2], projects[id][3]]
    elif optionInsert == 3:
        viewDepartament()
        newState = input("Ingre el nombre del Nuevo departamento: ")
        projects[id] = [projects[id][0], projects[id][1], newState, projects[id][3]]
    elif optionInsert == 4:
        viewDepartament()
        newState = input("Ingrese el Index del nuevo municipio: ")
        projects[id] = [projects[id][0], projects[id][1], projects[id][2], newState]
    headerProject()
    viewProject(id)
    print("==================================================================================")
    print("Edicion Completada")
    input("Presione cualquier tecla para continuar")

def deleteProject(id):
    projects.pop(id, None)
    print("Registro Eliminado")
def subMenuConsultProject(id):
    while True:
        descriptionMenuEdit()
        opcionMenu = input("Inserte la opcion>> ")

        if opcionMenu == "1":

            print("==================================================================================")
            editProject(id)
            break
            print("==================================================================================")

        elif opcionMenu == "2":
            print("==================================================================================")
            deleteProject(id)
            print("==================================================================================")
            break
        elif opcionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def viewProjects():
    headerProject()
    # id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
    for k, v in projects.items():
        print(k.ljust(10, " "), end="")
        print(client[v[0]][0].ljust(20, " "), end="")
        print(status[v[1]].ljust(20, " "), end="")
        print(v[2].ljust(15, " "), end="")
        print(departments[v[2]][int(v[3])].ljust(20, " "), end="")
        print("")
def insertProjetc():
    id = input("Ingrese el id del registro: ")
    if id  in projects:
        print("Ese id ya existe")
    else:
        viewClient()
        idCliente = input("Ingrese el id del Cliente: ")
        viewStatus()
        idEstado = input("Ingrese el id del Estado actual del Proyecto: ")
        viewDepartament()
        nameDepartament = input("Ingrese el Nombre del departamento: ")
        idState = input("Ingrese el Indice del municipio: ")
        # id, idCliente, idEstado, nombreDepartamento, IndiceMunicipio
        projects[id] = [idCliente, idEstado, nameDepartament, idState]
def consultProyect(id):
    headerProject()
    if id in projects:
        viewProject(id)
        subMenuConsultProject(id)
    else:
        print("Este Usuario no existe")
#Section the Proyects==================================================================================================
def menuPrincipal():
    while True:
        cleanScreen()
        menu()
        optionMenu = input("Inserte la opcion>> ")
        if optionMenu == "1":
            option = "1"
            print("==================================================================================")

            menuClient()


        elif optionMenu == "2":
            print("==================================================================================")
            menuDepartament()
            print("==================================================================================")

        elif optionMenu == "3":
            print("==================================================================================")
            menuStatus()
        elif optionMenu == "4":
            print("==================================================================================")
            menuProject()
            print("==================================================================================")



        elif optionMenu == "0":
            break
        else:
            print("")
            input("Pulsa una tecla para continuar")
def menuClient():
    while True:
        cleanScreen()
        descriptionMenuClient()
        optionMenu = input("Inserte la opcion>> ")
        if optionMenu == "1":
            opcion = "1"
            print("==================================================================================")
            while not opcion == "0":
                insertClient()
                opcion = input("pulsa una 0 para Salir o Enter para continuar")
                print("==================================================================================")

        elif optionMenu == "2":
            print("==================================================================================")
            viewClient()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")

        elif optionMenu == "3":
            print("==================================================================================")
            id = input("Ingrese id del cliente: ")
            consultClient(id)
            print("==================================================================================")

        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuDepartament():

    while True:
        cleanScreen()
        descriptionMenuDepartament()
        optionMenu = input("Inserte la opcion>>  ")
        if optionMenu == "1":
            opcion = "1"
            print("==================================================================================")
            insertDepartament()

        elif optionMenu == "2":
            print("==================================================================================")
            viewDepartament()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")

        elif optionMenu == "3":
            print("==================================================================================")
            nameDepartament = input("Ingrese nombre del departamento:  ")
            consultDepartament(nameDepartament)


        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuStatus():
    while True:
        cleanScreen()
        descriptionMenuStatus()
        optionMenu = input("Inserte la opcion>>  ")

        if optionMenu == "1":
            option = "1"
            while not  option == "0":
                insertStatus()
                print("==================================================================================")
                option = input("Presione 0 Para Salir\nPulsa una tecla para continuar Ingresando")
                print("==================================================================================")

        elif optionMenu == "2":
            print("==================================================================================")
            viewStatus()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")

        elif optionMenu == "3":
            print("==================================================================================")
            id = input("Ingrese el id del estado a buscar: ")
            print("==================================================================================")
            consultStatus(id)
            print("==================================================================================")


        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
def menuProject():
    while True:
        cleanScreen()
        despcriptionMenuProject()
        optionMenu = input("Inserte la opcion>> ")

        if optionMenu == "1":
            print("==================================================================================")
            insertProjetc()
            print("==================================================================================")

        elif optionMenu == "2":
            print("==================================================================================")
            viewProjects()
            input("Pulsa una tecla para continuar")
            print("==================================================================================")


        elif optionMenu == "3":
            print("==================================================================================")
            id = input("Ingrese el id del registro: ")
            consultProyect(id)
            print("==================================================================================")



        elif optionMenu == "0":
            break
        else:
            print("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


menuPrincipal()



