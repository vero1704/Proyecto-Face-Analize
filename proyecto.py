"""
AUTOR: Maria Fernanda Duran Condega Y Verónica Quesada Rojas
FECHA: 17 de mayo
SEMANA: PROYECTO
"""

import random
import operator
from builtins import len

usuarios = [{"nombreusuario": "Juan", "contraseña": "123", "tipo": "admin"},
            {"nombreusuario": "Carla", "contraseña": "123", "tipo": "user"},
            {"nombreusuario": "Marco", "contraseña": "123", "tipo": "analista"}]

personas = []

"""
Description: Function that sees the main menu
Return the menu
"""


def menuPrincipal():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "Digite 1 para iniciar Sesion\n"
            "Digite 2 para terminar\n"
            "\n"
            "Seleccione una opción del menú: ")
    return menu


"""
Description: Function that sees the administrator menu
Return the menu
"""


def menuAdmin():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "\nDigite 1 para crear persona automaticamente \n"
            "Digite 2 crear persona manualmente \n"
            "Digite 3 para volver al menú\n"
            "\n"
            "Seleccione una opción del menú: ")
    return menu


"""
Description: Function that sees the user menu.
Return the menu
"""


def menuUser():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "\nDigite 1 para modificar una persona\n"
            "Digite 2 para consultar personas \n"
            "Digite 3 para volver al menu\n"
            "\n"
            "Seleccione una opción del menú: ")
    return menu


"""
Description: Function that sees the analyst menu.
Return the menu
"""


def menuAnalista():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "\nDigite 1 para ver estadistica por provincia y grupo etario\n"
            "Digite 2 para ver estadistica por emoción\n"
            "Digite 3 para volver al menú\n"
            "\n"
            "Seleccione una opción del menú: ")
    return menu


"""
Description: Function that validates if the user exists
Returns the type of user if it is in the list or an error message
"""


def inicio_Sesión(user, contraseña):
    encontrado = False
    for usuario in usuarios:
        if usuario["nombreusuario"] == user and usuario["contraseña"] == contraseña:
            menuUser()
            return usuario["tipo"]
    if encontrado == False:
        print("-------Datos inválidos. Vuelva a intentarlo-------- \n")
        main()



"""
Description: Function that returns a random number
Returns the number, which will be the user's ID
"""

def generarCedulas():
    cedula = random.randrange(1000000,8000000) + 1
    return str(cedula)


"""
Description: Function that returns a random number
Returns the number, which will be the age of the user
"""


def generarEdad():
    edades = random.randrange(1, 100)
    return edades


"""
Description: Function that creates a list with various face shapes
Returns the list with the face types
"""


def formaRostro():
    rostro = ["Redondo", "Alargado", "Corazón", "Cuadrado", "Ovalado", "Rectangular"]
    return rostro


"""
Description: Function that creates a list with various emotions
Return the list with emotions
"""


def emociones():
    emocion = ["Enfado", "Desprecio", "Disgusto", "Miedo", "Sorpresa", "Alegría", "Neutral", "Tristeza"]
    return emocion


"""
Description: Function that creates a list with various skin colors
Returns the list with skin colors
"""


def colorPiel():
    piel = ["Negra", "Marrón", "Morena", "Clara", "Blanca"]
    return piel


"""
Description: Function that creates a list with the genres
Returns the list with the genres
"""


def generos():
    genero = ['Masculino', 'Femenino']
    return genero


"""
Description: Function that creates a list with age groups, but at the same time validates the age range to know its 
             age group.And receives as parameter the age
Returns the age group index
"""

listaNiños = []
listaAdolescente =  []
listaAdultos = []
listaMayores = []

def grupoEtario(edad):
    grupo = ["Niño", "Adolescente", "Adulto", "Adulto Mayor"]
    if edad > 0 and edad < 10:
        g = grupo[0]  # Gets the item in those positions
        index = grupo.index(g)  # Gets the index of the element
        listaNiños.append(index)
        print("Niño")
        return index

    elif edad > 10 and edad <= 19:
        g = grupo[1]
        index = grupo.index(g)
        listaAdolescente.append(index)
        print("Adolescente")
        return index

    elif edad >= 20 and edad < 59:
        g = grupo[2]
        index = grupo.index(g)
        listaAdultos.append(index)
        print("Adulto")
        return index

    elif edad >= 59:
        g = grupo[3]
        index = grupo.index(g)
        listaMayores.append(index)
        print("Adulto Mayor")
        return index


"""
Description: Function that creates a list with accessories
Returns the list with the elements
"""


def accesorios():
    accesorio = ["Lentes", "Aretes", "Percing", "Ninguno"]
    return accesorio


"""
Description: Function that creates a dictionary with the different keys and their attributes
Returns the dictionary with the elements
"""


def cabello():
    cabello = {}
    cabello["color"] = ["Negro", "Rubio", "Café", "Castaño", "Gris", "Invisible"]
    cabello["densidad"] = ["Escaso", "Moderado", "Abundante"]
    cabello["textura"] = ["Lacio", "Ondulado", "Rizado"]
    return cabello


"""
Description: Function that randomly gets a hair color and searches the index. And receives as a parameter
             hair which is the dictionary
Returns the index of the selected elements
"""


def colorPelo(cabello):
    pelo = random.choice(cabello["color"])  # Get random hair in color key
    index = cabello["color"].index(pelo)  # Gets the index of the item in the dictionary with the color key
    return index


"""
Description: Function that randomly gets a density of hair and searches the index. And receive as parameter
             hair which is the dictionary
Returns the index of the selected elements.
"""


def densidadCabello(cabello):
    pelo = random.choice(cabello["densidad"])  # Get random hair in density key
    index = cabello["densidad"].index(pelo)  # Gets the index of the item in the dictionary with the density key
    return index


"""
Description: Function that randomly gets a hair texture and searches the index. And receive as parameter
             hair which is the dictionary
Returns the index of the selected elements.
"""


def texturaCabello(cabello):
    pelo = random.choice(cabello["textura"])  # Get random hair in texture key
    index = cabello["textura"].index(pelo)  # Gets the index of the item in the dictionary with the texture key
    return index


"""
Description: Function that creates a dictionary with the different keys and their attributes.
Returns the dictionary with the elements.
"""


def ojos():
    ojos = {}
    ojos["forma"] = ["Almendrados", "Separados", "Redondos", "Caídos", "Saltones", "Juntos", "Profundos", "Asiático"]
    ojos["color"] = ["Negro", "Castaño", "Ámbar", "Avellana", "Verde", "Azul", "Gris"]
    return ojos


"""
Description: Function that randomly gets an eye shape and searches the index. And receive as a parameter eyes which is the dictionary
Returns the index of the selected elements.
"""


def ojosForma(ojos):
    forma = random.choice(ojos["forma"])  # Get random eyes in shape key
    index = ojos["forma"].index(forma)  # Gets the index of the item in the dictionary with the shape key
    return index


"""
Description: Function that randomly gets an eye color and searches the index. And receive as a parameter eyes which is the dictionary
Returns the index of the selected elements.
"""


def ojosColor(ojos):
    color = random.choice(ojos["color"])  # Get random eyes in color key
    index = ojos["color"].index(color)  # Gets the index of the item in the dictionary with the shape key
    return index


"""
Description: Function that creates a list with the provinces of Costa Rica
Returns the list with the elements
"""


def provincias():
    provincia = ["San José", "Alajuela", "Cartago", "Heredia", "Puntarenas", "Guanacaste", "Limón"]
    return provincia


"""
Description: Function that randomly creates a person with all attributes.
Returns the list with the different people and their attributes
"""


def crearPersonaAutomaticamente():
    cont = 0
    while cont <=15:
        diccionario = {}
        cedula = generarCedulas()
        edad = generarEdad()
        rostro = random.choice(formaRostro())  # Get a face type elements randomly
        idRostro = formaRostro().index(rostro)  # Gets the index of the element
        piel = random.choice(colorPiel())  # Get a skin type elements randomly
        idPiel = colorPiel().index(piel)  # Gets the index of the element
        grupo = grupoEtario(edad)
        genero = random.choice(generos())
        idGenero = generos().index(genero)
        emocion = random.choice(emociones())
        idEmocion = emociones().index(emocion)
        accesorio = random.choice(accesorios())
        idAccesorio = accesorios().index(accesorio)
        provincia = random.choice(provincias())
        idProvincia = provincias().index(provincia)
        cabelloColor = colorPelo(cabello())
        cabelloDensidad = densidadCabello(cabello())
        cabelloTextura = texturaCabello(cabello())
        formaOjos = ojosForma(ojos())
        colorOjos = ojosColor(ojos())

        diccionario = {"Cedula:": cedula, "Edad:": edad, "Rostro": idRostro, "Color Piel:": idPiel,
                       "Grupo Etario:": grupo, "Genero:": idGenero,
                       "Emocion:": idEmocion, "Accesorios:": idAccesorio, "Color Cabello:": cabelloColor,
                       "Densidad Cabello:": cabelloDensidad,
                       "Textura cabello:": cabelloTextura, "Forma ojos:": formaOjos, "Color ojos:": colorOjos,
                       "Provincia:": idProvincia}

        personas.append(diccionario)  # Copy the full dictionary into the declared list
        cont += 1
    return personas

"""
Description: Function that goes through the list of face shapes, and shows them one by one.
Returns a message to choose
"""


def elegirRostro():
    cont = 0
    for elemento in formaRostro():  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    rostro = input("Seleccione el numero de su forma de rostro: ")
    return rostro


"""
Description: Function that goes through the list of skin colors, and shows them one by one.
Returns a message to choose
"""


def elegirPiel():
    cont = 0
    for elemento in colorPiel():  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    piel = input("Seleccione el numero de su color de piel: ")
    return piel


"""
Description: Function that goes through the list of emotions, and shows them one by one.
Returns a message to choose
"""


def elegirEmocion():
    cont = 0
    for elemento in emociones():  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    emocion = input("Seleccione el numero de su emocion: ")
    return emocion


"""
Description: Function that goes through the list of genres, and shows them one by one.
Returns a message to choose
"""


def elegirGenero():
    cont = 0
    for elemento in generos():  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    genero = input("Seleccione el numero de su genero: ")
    return genero


"""
Description: Function that goes through the list of accessories, and shows them one by one.
Returns a message to choose
"""


def elegirAccesorios():
    cont = 0
    for elemento in accesorios():  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    accesorio = input("Seleccione el numero de su accesorio: ")
    return accesorio


"""
Description: Function that goes through the list of hair colors, and shows them one by one.
Returns a message to choose
"""


def elegirCabello():
    cont = 0
    cabellos = cabello()
    colores = cabellos["color"]  # Assign the variable with the key to obtain
    for elemento in colores:  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    color = input("Seleccione el numero de su color de cabello: ")
    return color


"""
Description: Function that goes through the list of hair densities, and shows them one by one.
Returns a message to choose
"""


def elegirDensidad():
    cont = 0
    cabellos = cabello()
    densidades = cabellos["densidad"]  # Assign the variable with the key to obtain
    for elemento in densidades:  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    densidad = input("Seleccione el numero de la densidad de cabello: ")
    return densidad


"""
Description: Function that goes through the list of hair textures, and shows them one by one.
Returns a message to choose
"""


def elegirTextura():
    cont = 0
    cabellos = cabello()
    texturas = cabellos["textura"]  # Assign the variable with the key to obtain
    for elemento in texturas:  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    textura = input("Seleccione el numero de textura de su cabello: ")
    return textura


"""
Description: Function that goes through the list of eye shapes, and shows them one by one.
Returns a message to choose
"""


def elegirForma():
    cont = 0
    ojo = ojos()
    formas = ojo["forma"]  # Assign the variable with the key to obtain
    for elemento in formas:  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    forma = input("Seleccione el numero de la forma de sus ojos: ")
    return forma


"""
Description: Function that goes through the list of eye colors, and shows them one by one.
Returns a message to choose
"""


def elegirOjos():
    cont = 0
    ojo = ojos()
    colores = ojo["color"]
    for elemento in colores:  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    color = input("Seleccione el numero del color de sus ojos: ")
    return color


"""
Description: Function that goes through the list of provinces, and shows them one by one.
Returns a message to choose
"""


def elegirProvincia():
    cont = 0
    for elemento in provincias():  # Scroll through the list
        print(cont, " -", elemento)  # Print a number and the element that is going through the list
        cont += 1
    provincia = input("Seleccione el numero de su provincia: ")
    return provincia


def crearPersonaManualmente():
    diccionario = {}
    cedula = generarCedulas()
    edad = generarEdad()
    print("\n--- Formas de rostro ---")  # Print the attribute title
    idRostro = elegirRostro()  # Assign the function to a variable
    print("\n--- Color de piel -----")
    idPiel = elegirPiel()
    print("\n--- Emoción -------")
    idEmocion = elegirEmocion()
    print("\n--- Genero -------")
    idGenero = elegirGenero()
    idGrupo = grupoEtario(edad)
    print("\n--- Accesorios ----")
    idAccesorios = elegirAccesorios()
    print("\n--- Color de cabello ----")
    idCabello = elegirCabello()
    print("\n--- Densidad de cabello ----")
    idDensidad = elegirDensidad()
    print("\n--- Textura de cabello ----")
    idTextura = elegirTextura()
    print("\n--- Forma de ojos ----")
    idForma = elegirForma()
    print("\n--- Color de ojos ----")
    idColor = elegirOjos()
    print("\n--- Provincias ----")
    idProvincia = elegirProvincia()

    diccionario = {"Cedula:": cedula, "Edad:": edad, "Rostro": idRostro, "Color Piel:": idPiel,
                   "Grupo Etario:": idGrupo,
                   "Genero:": idGenero, "Emocion: ": idEmocion, "Accesorios:": idAccesorios,
                   "Color Cabello:": idCabello,
                   "Densidad Cabello:": idDensidad, "Textura cabello:": idDensidad, "Forma ojos:": idForma,
                   "Color ojos:": idColor, "Provincia:": idProvincia}

    personas.append(diccionario)  # Copy the full dictionary into the declared list
    return personas

def mostrarCedulas():
    print("------------LISTA DE CEDULAS -------------- \n")
    for id in personas:
        print("---",id["Cedula:"])

def Modificar_Persona():

    print("\n¿QUÉ DESEA MODIFICAR?\n")
    print("Digite 1 para modificar provincia \n"            #Menu shows all the functions for modify a person
          "Digite 2 para modificar las emociones \n"
          "Digite 3 para salir\n")
    Opt = input("Seleccione una opción: ")
    if Opt == "1":
        print("\n-------------Modificar  Provincia-------------\n")
        mostrarCedulas()

        IDaModificar = input("\nIngrese la cedula: ")                                                                #Requires the ID to access the person
        for usuario in personas:
            if usuario["Cedula:"] == IDaModificar:                  #Validate if the person exists
                print("El primer digito de a cedula equivale a la provincia")
                print("SAN JOSÉ=1, ALAJUELA=2, CARTAGO=3, HEREDIA=4, GUANACASTE=5, PUNTARENAS=6, LIMÓN=7") #Shows all the provinces
                digito = input("Ingrese el digito de la provincia que quiere cambiar")
                newced=usuario["Cedula:"].replace(usuario["Cedula:"][0],digito,1)                          #uses the first digit of the ID because it equals province and changes it once
                usuario["Cedula:"]=newced                                                                  #Changes the first ID´s digit
                if  digito=="1":
                    usuario["Provincia:"]="1"                                                               #Saves "1" in the key "Provincia"
                    print("La provincia ha sido cambiada a San José")
                    main()
                if digito== "2":
                    usuario["Provincia:"]="2"
                    print("La provincia ha sido cambiada a Alajuela")                                       #Saves "2" in the key "Provincia"
                    main()
                if digito== "3":
                    usuario["Provincia:"]="3"
                    print("La provincia ha sido cambiada a Cartago")                                        #Saves "3" in the key "Provincia"
                    main()
                if digito== "4":
                    usuario["Provincia:"]="4"
                    print("La provincia ha sido cambiada a Heredia")                                        #Saves "4" in the key "Provincia"
                    main()
                if digito== "5":
                    usuario["Provincia:"]="5"
                    print("La provincia ha sido cambiada a Guanacaste")                                     #Saves "5" in the key "Provincia"
                    main()
                if digito== "6":
                    usuario["Provincia:"]="6"
                    print("La provincia ha sido cambiada a Puntarenas")                                     #Saves "6" in the key "Provincia"
                    main()
                if digito== "7":
                    usuario["Provincia:"]="7"
                    print("La provincia ha sido cambiada a Limón")                                          #Saves "7" in the key "Provincia"
                    print(usuario["Provincia:"])
                    main()
                      
        print("La cedula no existe \n"                  
                      "Digite una cedula existente")
        Modificar_Persona()
    elif Opt == "2":
        print("\n-------------Modificar  emoción-------------\n")
        mostrarCedulas()
        IDaModificar = input("\nIngrese la cedula: ")                                                                #Requires the ID to access the person
        for usuario in personas:
            while usuario["Cedula:"] == IDaModificar:
                print("Las emociones disponibles son: ")
                print("Enfado = 0", "Disgusto = 1", "Miedo = 2", "Sorpresa = 3", "Alegría = 4", "Neutral = 5",
                      "Tristeza = 6", sep='\t')
                if usuario["Cedula:"] == IDaModificar:
                    change = int(input("Seleccione el número de la emoción: "))
                    print("\n")
                    usuario["Emocion:"] = change                                                 #Saves "CHANGE" in the key "Emocion:"
                    if  change == 0:
                        print("La emoción ha sido cambiada a Enfado \n")
                        main()
                    elif change == 1:
                        print("La emoción ha sido cambiada a Disgusto \n")
                        main()
                    elif change == 2 :
                        print("La emoción ha sido cambiada a Miedo \n")
                        main()
                    elif change == 3:
                        print("La emoción ha sido cambiada a Sorpresa \n")
                        main()
                    elif change== 4:
                        print("La emoción ha sido cambiada a Alegría \n")
                        main()
                    elif change== "5":
                        print("La emoción ha sido cambiada a Neutral \n")
                        main()
                    elif change== "6":
                        print("La emoción ha sido cambiada a Tristeza \n")
                        main()
                    main()
                
            else:
                print("La cedula no existe \n"
                      "Digite una cedula existente")                                                    # If the ID is wrong. Asks to enter a valid ID
                main()



def Consultar_Persona():
    print("-------------Consultar una persona-------------'\n'")
    consulta=input("Ingrese la cedula a consultar: ")
    for usuario in personas:
        if usuario["Cedula:"]==consulta:
            print("La persona ",consulta," si existe")
            return True

def mostrarDatos(claves):
    cedula = claves["Cedula:"]

    inde = claves["Color Piel:"]
    piel = colorPiel()

    indexEmocion = claves["Emocion:"]
    emocion = emociones()
    indexGenero = claves["Genero:"]
    genero = generos()

    indexColor= claves["Color Cabello:"]
    ojitos = ojos()
    ojo= ojitos["color"][indexColor]

    indexCabello = claves["Textura cabello:"]
    cabellos = cabello()
    textura = cabellos["textura"][indexCabello]

    print(cedula, genero[indexGenero], piel[inde], emocion[indexEmocion],textura,ojo, sep='\t \t \t')


def estadisticaProvinciaEtario():
    contador = 0
    contadorPersonasProvincia = 0
    listaNiño = []
    listaAdolescentes = []
    listaAdulto = []
    listaMayor = []
    imprimiendoNombreDeProvincia = False
    index = provincias()
    while contador < 7 :                                                    #Porque tengo 7 provincias
        for claves in personas:
            if claves["Provincia:"] == contador:
                provincia = claves["Provincia:"]
                contadorPersonasProvincia += 1
                if imprimiendoNombreDeProvincia == False:
                    print("\n----------------------------- PROVINCIA: ", index[provincia], "-----------------------------")
                    imprimiendoNombreDeProvincia = True
                if claves["Grupo Etario:"] == 0:
                    listaNiño.append(claves)
                elif claves["Grupo Etario:"] == 1:
                    listaAdolescentes.append(claves)
                elif claves["Grupo Etario:"] == 2:
                    listaAdulto.append(claves)
                elif claves["Grupo Etario:"] == 3:
                    listaMayor.append(claves)

        print("\n°° Niño ", len(listaNiño),"\n")
        print("Cedula", "Genero", "Piel", "Emocion", "Cabello", "Color", sep='\t \t \t')
        print(
            "******************************************************************************************************** \n")
        for i in listaNiño:
            mostrarDatos(i)
        listaNiño = []

        print("\n°° Adolescentes ",len(listaAdolescentes),"\n")
        print("Cedula", "Genero", "Piel", "Emocion", "Cabello", "Color", sep='\t \t \t')
        print(
            "******************************************************************************************************** \n")
        for i in listaAdolescentes:
            mostrarDatos(i)
        listaAdolescentes = []

        print("\n°° Adulto ", len(listaAdulto),"\n")
        print("Cedula", "Genero", "Piel", "Emocion", "Cabello", "Color", sep='\t \t \t')
        print(
            "******************************************************************************************************** \n")
        for i in listaAdulto:
            mostrarDatos(i)
        listaAdulto = []

        print("\n°° Adulto Mayor ", len(listaMayor),"\n")
        print("Cedula", "Genero", "Piel", "Emocion", "Cabello", "Color", sep='\t \t \t')
        print(
            "******************************************************************************************************** \n")
        for i in listaMayor:
            mostrarDatos(i)
        listaMayor = []

        contador += 1
        imprimiendoNombreDeProvincia = False
        print("\n°°°°°°Personas por provincia: ", contadorPersonasProvincia)
        contadorPersonasProvincia = 0

    totalPersonas = len(listaNiños) + len(listaAdolescente) + len(listaAdultos) + len(listaMayores)
    porcentajeNiños = (len(listaNiños) * 100) / totalPersonas
    porcentajeAdolescentes = (len(listaAdolescente) * 100) / totalPersonas
    porcentajeAdultos = (len(listaAdultos) * 100) / totalPersonas
    porcentajeAdultosMayor = (len(listaMayores) * 100) / totalPersonas

    print("\n -------------------ESTADISTICA TOTALES-------------------\n")
    print("Total niños en Costa Rica: ",len(listaNiños),"                  Porcentaje de Niños en Costa Rica: ",porcentajeNiños,"%")
    print("Total adolescentes en Costa Rica: ",len(listaAdolescente),"     Porcentaje de adolscentes en Costa Rica: ",porcentajeAdolescentes,"%")
    print("Total adultos en Costa Rica: ", len(listaAdultos),"             Porcentaje de adultos en Costa Rica: ",porcentajeAdultos, "%")
    print("Total adultos mayores en Costa Rica: ", len(listaMayores),"     Porcentaje de adultos mayores en Costa Rica: ",porcentajeAdultosMayor, "%")


def estadisticaEmocion():
   diccionario = {}
   enfadado = 0
   desprecio = 0
   disgusto = 0
   miedo = 0
   sorpresa = 0
   alegria = 0
   neutral = 0
   tristeza = 0
   for i in personas:
       if i["Emocion:"] == 0:
           enfadado += 1
       elif i["Emocion:"] == 1:
           desprecio += 1
       elif i["Emocion:"] == 2:
           disgusto += 1
       elif i["Emocion:"] == 3:
           miedo += 1
       elif i["Emocion:"] == 4:
           sorpresa += 1
       elif i["Emocion:"] == 5:
           alegria += 1
       elif i["Emocion:"] == 6:
           neutral += 1
       elif i["Emocion:"] == 7:
           tristeza += 1
   total = len(personas)
   diccionario["Enfandado"] = enfadado
   diccionario["Desprecio"] = desprecio
   diccionario["Disgusto"] = disgusto
   diccionario["Miedo"] = miedo
   diccionario["Sorpresa"] = sorpresa
   diccionario["Alegria"] = alegria
   diccionario["Neutral"] = neutral
   diccionario["Tristeza"] = tristeza
   lis = []
   lista = []
   ordenado = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
   for i in ordenado:
       lis.append(i[0])
       lista.append(i[1])

   print("          ",end='\t')
   for j in lis:
       print(j,end='\t \t')

   print('\n')
   print("Total     ",end='\t')

   for k in lista:
       print(k,end='\t \t \t \t')

   print('\n')

   print("Porcentaje ",end='\t')
   for j in lista:
       porcentaje = (j * 100) / total
       print(porcentaje,end='\t \t \t')

   print('\n')


def main():
    try:
        menu = int(input(menuPrincipal()))
        if menu == 1:
            usuario = input("Digite su usuario: ")
            contra = input("Digite su contraseña: ")
            tipo = inicio_Sesión(usuario, contra)
            if tipo == "admin":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuAdmin()))
                if opcion == 1:
                    crearPersonaAutomaticamente()
                    print("\n-------------SE HA CREADO LA PERSONA CORRECTAMENTE--------------\n")
                    menuAdmin()
                if opcion == 2:
                    crearPersonaManualmente()
                    print("\n-------------SE HA CREADO LA PERSONA CORRECTAMENTE--------------\n")
                    menuAdmin()
                else:
                    main()
            if tipo == "user":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuUser()))
                if opcion == 1:
                    Modificar_Persona()
                    main()
                elif opcion == 2:
                    consultar = Consultar_Persona()
                    if consultar == True:
                        print("\n-------------LA PERSONA SI EXISTE EN EL REGISTRO--------------\n")
                        return menuUser()
                    else:
                        print("\n-------------LA PERSONA NO EXISTE EN EL REGISTRO--------------\n")
                        main()
                else:
                    main()
            if tipo == "analista":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuAnalista()))
                if opcion == 1:
                    estadisticaProvinciaEtario()
                    main()
                elif opcion == 2:
                    estadisticaEmocion()
                    main()
        else:
            menu==2
            return
    except ValueError:
        print("---------Ingrese un número del menú-----------")
        main()


main()


