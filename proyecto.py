"""
AUTOR: Maria Fernanda Duran Condega Y Verónica Quesada Rojas
FECHA: 17 de mayo
SEMANA: PROYECTO
"""

import random

usuarios = [{"nombreusuario": "Juan", "contraseña": "123", "tipo": "admin"},
            {"nombreusuario": "Carla", "contraseña": "123", "tipo": "user"},
            {"nombreusuario": "Marco", "contraseña": "123", "tipo": "analista"}]

personas = [{"Cedula:": "29873654", "Edad:": 15, "Rostro:": "Redondo:", "Color Piel:": "Morena:", "Grupo Etario:": "Adolescente",
                   "Genero:": "Femenino",
                   "Emocion:": "Alegría","Accesorios:": "Aretes", "Color Cabello:": "Negro",
                   "Densidad Cabello:": "Escaso","Textura cabello:": "rizado", "Forma ojos:": "Almendrados", "Color ojos:": "Castaño",
                   "Provincia:": "Alajuela"}]

"""
Description: Function that sees the main menu
Return the menu
"""


def menuPrincipal():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "1.Iniciar Sesion\n"
            "2.Salir\n"
            "\n"
            "Seleccione una opcion: ")
    return menu


"""
Description: Function that sees the administrator menu
Return the menu
"""


def menuAdmin():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "\n1.Crear persona automaticamente \n"
            "2.Crear persona manualmente \n"
            "3.Salir\n"
            "\n"
            "Seleccione una opcion: ")
    return menu


"""
Description: Function that sees the user menu.
Return the menu
"""


def menuUser():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "\n Digite 1 para Modificar una persona\n"
            "Digite 2 para Consultar personas \n"
            "Digite 3 para Volver al menu\n"
            "\n"
            "Seleccione una opción del menú")
    return menu


"""
Description: Function that sees the analyst menu.
Return the menu
"""


def menuAnalista():
    menu = ("--------------FACE ANALIZE -------------- \n"
            "***************************************** \n"
            "\n1.Estadistica por provincia\n"
            "2.Estadistica de grupo etario \n"
            "3.Estadistica por emocióm"
            "4. Volver al menú\n"
            "\n"
            "Seleccione una opcion: ")
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
    cedula = random.randrange(1000) + 1
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


def grupoEtario(edad):
    grupo = ["Niño", "Adolescente", "Adulto", "Adulto Mayor"]
    if edad > 0 and edad < 10:
        g = grupo[0]  # Gets the item in those positions
        index = grupo.index(g)  # Gets the index of the element
        return index
    elif edad > 10 and edad <= 19:
        g = grupo[1]
        index = grupo.index(g)
        return index
    elif edad >= 20 and edad < 59:
        g = grupo[2]
        index = grupo.index(g)
        return index
    elif edad >= 59:
        g = grupo[3]
        index = grupo.index(g)
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

    diccionario = {"Cedula:": cedula, "Edad:": edad, "Rostro": idRostro, "Color Piel:": idPiel, "Grupo Etario:": grupo,
                   "Genero:": idGenero,
                   "Emocion: ": idEmocion, "Accesorios:": idAccesorio, "Color Cabello:": cabelloColor,
                   "Densidad Cabello:": cabelloDensidad,
                   "Textura cabello:": cabelloTextura, "Forma ojos:": formaOjos, "Color ojos:": colorOjos,
                   "Provincia:": idProvincia}

    personas.append(diccionario)  # Copy the full dictionary into the declared list
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


def Modificar_Persona():
    print("¿QUÉ DESEA MODIFICAR?\n"
          "Digite 1 para modificar provincia \n"
          "Digite 2 para modificar las emociones \n"
          "Digite 3 para salir\n")
    Opt = input("SELECCIONE UNA OPCION")
    if Opt == "1":
        print("Usted va a modificar la provincia\n"
              "Ingrese el usuario que desea modificar")
        IDaModificar = input("Ingrese cedula")
        for usuario in personas:
            if usuario["Cedula:"] == IDaModificar:
                digito = input("Ingrese el digito que quiere reemplazar")
                print("PRUEBA 1", usuario["Cedula:"])
                newced=usuario["Cedula:"].replace(usuario["Cedula:"][0],digito,1)
                usuario["Cedula:"]=newced
                print("PRUEBA 1", usuario["Cedula:"])
                main()
            else:
                print("La cedula no existe \n"
                      "Digite una cedula existente")
                main()
    elif Opt == "2":
        print("¡Usted va a modificar una emoción!\n"
              "Las emociones disponibles son \n"
              "Enfado= 0","Disgusto= 1","Miedo= 2", "Sorpresa= 3", "Alegría= 4", "Neutral= 5", "Tristeza= 6\n")

        IDaModificar = input("Ingrese cedula")
        for usuario in personas:

            if usuario["Cedula:"] == IDaModificar:
                change = input("Seleccione el número de la emoción")
                newfeel=usuario["Emocion:"].replace(usuario["Emocion:"],change,1)
                usuario["Emocion:"]=newfeel

                print(usuario["Emocion:"])
                main()
            else:
                print("La cedula no existe \n"
                      "Digite una cedula existente")
                main()

def Consultar_Persona():
    print("Usted va a Consultar una persona")
    consulta=input("Ingrese la cedula a consultar")
    for usuario in personas:
        if usuario["Cedula:"]==consulta:
            print("La persona ",consulta," Si existe")
        else:
            print("La persona consultada no existe")
            main()


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
                    main()
                if opcion == 2:
                    print("\n-------------CREAREMOS UNA PERSONA--------------\n")
                    crearPersonaManualmente()
                    print("\n-------------SE HA CREADO LA PERSONA CORRECTAMENTE--------------\n")
                    main()
                else:
                    return
            if tipo == "user":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuUser()))
                if opcion == 1:
                    Modificar_Persona()
                elif opcion == 2:
                    Consultar_Persona()
                else:
                    main()

            if tipo == "analista":
                print("\n-------------Bienvenido", usuario, "--------------\n")
                opcion = int(input(menuAnalista()))
                if opcion == 1:
                    print("hello")
        else:
            menu==2
            return
    except ValueError:
        print("Ingrese un número del menú")
        main()
main()


